LingExRef plugin
=============================================

![[demo.gif]]

This Sublime Text 3 and 4 plugin allows you quickly insert references to surrounding LaTeX linguistic examples. Inspired by [quick-latex-ref](https://github.com/enricoflor/quick-latex-ref) which offers a similar functionality for Emacs.

## Usage

 Press <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Down</kbd> to insert a reference to the next example.  Press <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Up</kbd> to insert a reference to the previous example. 

 If the example already has a `\label{someexample}`, a reference to `\cref{someexample}` is inserted where the cursor is ; if it does not, a label is inserted right after `\ex` with name `example` and reference is inserted with name `example` and both names are then selected so you can change the name of the reference.
 

## Why not use `\nextx` or `\cnextx`?

The following works and achieves the same result after compilation, so why do we need a plugin?

```latex
Example \cnextx shows that subjunctive conditionals need not be counterfactual

\ex
If Alice was allergic to penicillin, she would show exactly the symptoms she's showing right now.
\xe
```

Answer from [*enricoflor*](https://github.com/enricoflor/quick-latex-ref):

> this is somewhat of an antipattern: it is a convenient feature (because so often you want to refer to something close to point), but it can cause serious headaches if you happen to restructure the text where these references occur. It may be very hard to notice that the reference you intended is now different because a different \label than the one you intended to refer to intervenes between the \Next macro and the item it should refer to. The convenience provided by these macros is better delivered by your text editor (ideally, GNU Emacs).


## Limitations

  - Currently only works with `\ex .. \xe` or `\pex .. \xe` of the `expex` package
  - Does not allow to cycle through next examples with repeated keystrokes

