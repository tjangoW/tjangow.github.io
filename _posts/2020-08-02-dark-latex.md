---
# optional when the title is not the file name
title: TexStudio in Dark Mode
tags: LaTeX, dark-theme
---

This time I will talk about customizing (darkify) $\LaTeX$ writing environment.
Obviously there are two parts to these: editor and PDF viewer.

## Editor
The editor of my choice is TexStudio, which supports dark theme starting from v3.
It can be changed under _Options -> Configure TexStudio... -> General -> Appearance -> Style_, Adwaita Dark (txs) is just fine for me.
I guess they are adapting this colour theme from the GTK-theme in Linux desktop.

Prior to this, I was using a custom theme from [pmaroco][custom texstudio dark], which if I recall correctly, changes only the editor area.

## PDF Viewer
I have started dark themed LaTeX experience with external viewer.
However, it is not always a smooth experience. The exact same command worked fine at the beginning, but right now the forward search (from *.tex to the line in PDF) is buggy: works for some documents but not the other.
I had enough of interruption with this coupling and hence now switch back to use internal viewer.

In short, if it is fine for you to change the PDF colour, I suggest go with the path of internal viewer.
Otherwise, try your luck with external viewer.

### Internal Viewer
With the following lines in preamble (before the line `\begin{document}`), 
you have a single point to switch between light and dark mode.
The code below are separated into several files as I personally prefer to have some (false) sense of organisation in the preamble.
```tex
%% START default_preamble.tex
\usepackage{ifthen}
\newboolean{RELEASE}
\setboolean{RELEASE}{false}
%% END default_preamble.tex


%% START default_preamble_last.tex
% initially split for hyperref as there could be some problems to \input them too early
\usepackage{xcolor}
\ifthenelse{\boolean{RELEASE}} {
	\colorlet{hrefColor}{blue}
}
{
	\definecolor{page_dark}{HTML}{333333}
	\pagecolor{page_dark}
	\color{white}
	\colorlet{hrefColor}{cyan}
}

\usepackage[]{hyperref}
\hypersetup
{
	colorlinks=true,
	allcolors=hrefColor, 
}
%% END default_preamble_last.tex


%% START main.tex
\input{default_preamble.tex}
\setboolean{RELEASE}{false} % switch the boolean here
\input{default_preamble_last.tex}

\begin{document}
%...
%% END main.tex
```

### External Viewer (SumatraPDF)
I have been using SumatraPDF as my default viewer (not editor/"signer") for quite a while, as it is way lighter than those typical one like Acrobat Reader or Foxit Reader (though i like its fill-in options very much).
I achieve this by inverting the overall colour scheme for SumatraPDF in _Settings -> Advanced Options..._ with these 3 items:
```
MainWindowBackground = #555555
FixedPageUI [
	TextColor = #eeeeee
	BackgroundColor = #333333
]
```
As for the reverse search in SumatraPDF settings (`InverseSearchCmdLine` in _Advanced Options..._), it has to be changed to 
`"C:\Program Files (x86)\texstudio\texstudio.exe" "%f" -line %l`.

On the other hand, TexStudio as to be configured at 2 places:
1. _Options -> Configure TexStudio... -> Commands -> External PDF Viewer_: 
    ```
    "C:/Program (x86) Files/SumatraPDF/SumatraPDF.exe" -reuse-instance ?am".pdf -forward-search ?c:ame" @
    dde:///"C:/Program (x86) Files/SumatraPDF/SumatraPDF.exe":SUMATRA/control/ [ForwardSearch("?am.pdf","?c:ame",@,0,0,1)]
    ```
    Try the second one if the first command does not work (according to [this site][forward search command], TexStudio v2.3 needs have to use the second command).
2. _Options -> Configure TexStudio... -> Build -> PDF Viewer_: `txs:///view-pdf-external`


## Sources
- [TexStudio Release Notes][texstudio release notes]
- [pmaroco GitHub repo][custom texstudio dark]
- [Latexgrucad website][forward search command]


[forward search command]: https://sites.google.com/site/latexgrucad/tex-studio
[custom texstudio dark]: https://github.com/pmaroco/dark-texstudio
[texstudio release notes]: https://github.com/texstudio-org/texstudio/blob/master/utilities/manual/CHANGELOG.txt
