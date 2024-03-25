import re
import sublime
import sublime_plugin

class AddRefToExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit, reverse = False):
		first_selection = self.view.sel()[0]

		begin_ref_str = r"\cref{"
		end_ref_str = r"}"
		default_name_str = r"example"
		ref_str = begin_ref_str + default_name_str + end_ref_str

		
		flags = 0
		if reverse:
			flags = flags | sublime.REVERSE
		example_begin_tag = self.view.find(r"((\\ex)|(\\pex))(?![a-zA-Z])", first_selection.begin(), flags)


		if example_begin_tag:
			example_end_tag = self.view.find(r"((\\a)|(\\xe))(?![a-zA-Z])", example_begin_tag.end())
			example_label_tag = self.view.find(r"\\label\{([^\}]*)\}", example_begin_tag.end())

			if example_end_tag and example_label_tag and example_label_tag < example_end_tag:
				label_tag = self.view.substr(example_label_tag)
				label_name_match = re.search(r'\\label{(.*)}', label_tag)
				if label_name_match:
					namelabel = label_name_match.group(1)
					self.view.window().status_message("label:" + namelabel)
					self.view.insert(edit, first_selection.end(), begin_ref_str + namelabel + end_ref_str)


				else:
					self.view.window().status_message("Impossible state occurred")
			else:
				self.view.insert(edit, first_selection.end(), ref_str)
				region_ref = sublime.Region(
					first_selection.end() + len(begin_ref_str), 
					first_selection.end() + len(begin_ref_str) + len(default_name_str),
				)

				if not reverse:
					# We adjust example_begin_tag, now that we've inserted some text before it
					example_begin_tag.a += len(ref_str)
					example_begin_tag.b += len(ref_str)

				# Insert "bla" after the found "\ex"
				begin_label_str = r"\label{"
				end_label_str = r"}"
				label_str = begin_label_str + default_name_str + end_label_str
				self.view.insert(
					edit, example_begin_tag.end(), 
					label_str
				)

				if reverse:
					# We adjust region_ref, now that we've inserted some text before it
					region_ref.a += len(label_str)
					region_ref.b += len(label_str)



				region_label = sublime.Region(
					example_begin_tag.end() + len(begin_label_str), 
					example_begin_tag.end() + len(begin_label_str) + len(default_name_str),
				)

				self.view.sel().clear()
				self.view.sel().add(region_label)
				self.view.sel().add(region_ref)
		else:
			self.view.window().status_message("No example found after cursor")



