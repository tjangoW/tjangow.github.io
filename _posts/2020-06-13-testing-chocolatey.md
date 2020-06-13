---
# optional when the title is not the file name
title: testing chocolatey
tags: chocolatey, windows
---

[Chocolatey](https://chocolatey.org) is one of the package manager under Windows operating system.
I have known it long time ago but have not been using it because I will most probably customise the install (e.g. no context menu, no desktop shortcut, deselect some options and so on), which is the same reason why I do not use something like [Ninite](https://ninite.com/) after I reset my pc.
Instead, I was leaning towards the path of portable versions, which has the advantage of preserving settings (though some may become invalid).

Anyway, after getting tired of updating software one by one for all these while, I decided go to package manager.
One package that would be useful is [chocolateyGUI](https://chocolatey.org/packages/ChocolateyGUI), which I use to mainly show the installed packages.
Btw, if there is an error uninstalling package via the GUI (for my case, there were `visualstudio2017buildtools` and `visualstudio-installer`), just reinstall and uninstall will do.

Minor complain perhaps: the search (`choco list blabla`) is not as nice as [yay](https://github.com/Jguer/yay) (a package manager for Arch-based Linux), in the sense that it only shows list of package names without any (brief) description.
For example, when I search for `obs`, this is what I get:
```
PS C:\Users\tjango> choco find obs
Chocolatey v0.10.15
obs 0.659.20200402 [Approved]
obs-virtualcam 2.0.5 [Approved]
obs-studio 25.0.8 [Approved]
obs-studio-wiiplayer2-scripts 0.4.6657.3109 [Approved]
obs-ndi 4.9.0 [Approved] Downloads cached for licensed users
obs-studio.portable 25.0.8 [Approved]
obs-studio.install 25.0.8 [Approved]
streamlabs-obs 0.22.3 [Approved] Downloads cached for licensed users
obs-mp 0.14.2.2202107 [Approved]
mobswitcher 1.3.3 [Approved]
GitReleaseNotes 0.6.1 [Approved]
GitVersion 1.0.0.1
12 packages found.
```
So how do i know the difference between `obs` abd `obs-studio`?
Yay, on the other hand, has nicer interface for this:
![yay linux (i guess)](https://camo.githubusercontent.com/68ac43d20140c1f4bef038e18860639454556e42/68747470733a2f2f72617763646e2e6769746861636b2e636f6d2f4a677565722f6a677565722e6769746875622e696f2f373736343766333936636237313536666433326533303937306462656166366436646337663938332f7961792f7961792d792e706e67)
