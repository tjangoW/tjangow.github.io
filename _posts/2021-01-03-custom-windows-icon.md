---
# optional when the title is not the file name
title: Custom Windows Icon
tags: windows
---

While sorting through my documents during the holidays, 
I have found this instructions to create an `.ico` file which can be used to customise icon in Windows.

1. Start InkScape with a layout of 256px x 256px and transparent background ([my template is here][inkscape template]).
    - larger size will not do any good as icons are rather small.
    100% zoom will give you a good feel as how the icon will become.
    - transparent background to avoid overseeing any white objects.
1. Draw whatever you like and save the the file as `.svg` would be sufficient.
1. Open the `.svg` file with GIMP and go to _File->Export As (Shift+Ctrl+E)_.
    - I just take the default options (1.25px/pt) when importing.
1. Change the extension to `.ico` and choose 32bpp for the highest quality icon file.

Now you just need to right click on the folders/shortcuts to change their icons.
For folders on Quick Access, the File Explorer probably has to be restarted for the changes to take effect.


[inkscape template]: https://github.com/tjangoW/tjangow.github.io/blob/master/assets/icon-template.svg?short_path=1a51a0c
