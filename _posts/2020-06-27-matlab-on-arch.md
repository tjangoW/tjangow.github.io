---
# optional when the title is not the file name
title: Setting up Matlab on Arch (Manjaro) without AUR
tags: Linux, Matlab, install
---

This is my experience setting up Matlab (R2020) on Manjaro without using AUR,
as there were a little hiccups during the installation process.
Hope this may be helpful for those facing the same issues.

Before going into the installation, you might be asking: _why the hell am I using Matlab?_
Well, more often than not, the choice is not up to you.
For instance, in my case, the project has started in Matlab before I joined in and it would be too much to switch language at that time.

Anyway, let's move on to the installation.
For this installation, I didn't use [AUR][AUR-matlab] package because it had the version R2019b but I wanted version R2020a.
Therefore, I went back to the standard method of downloading the installation file from the official website.
After extracting the download, As I prefer a system-wide install, I went for `sudo ./install`.
However, I have gotten the following error:
```txt
terminate called after throwing an instance of 'std::runtime_error'
  what():  Unable to launch the MATLABWindow application
zsh: abort      sudo ./install
```
A [quick google][matlabcentral-matlab window] told me that there are some missing shared library that MATLABWindow requires.
Running `./bin/glnxa64/MATLABWindow` told me that I do not have SELinux installed.
After fixing this issue, another came up The GUI as usual, but a dialog popped out telling me that there is not enough space in /tmp ?
I was kinda shocked as I have just reset the entire PC not long ago.
Had a quick look at GParted (I am still more of a graphical than terminal guy) and even looked at /tmp folder (with only 21.3MB used).
So I naively ignored the warning and proceed, so as to bang on the wall later on.

**Small segue to /tmp**:
just learnt that /tmp amongst others has sort of fixed sizes.
I assumed that it was designed so that you can create separate partitions for them.
Sadly, it backfired on me this time.
It can be easily increased by `mount -o remount,size=10G /tmp/` (from [stackExchange][se-increase mount]).

For unknown reasons, now I got the rubbish error "Unable to locate required installation files".
Didn't follow the [instruction from Matlab][matlabcentral-unable to locate] and restarted my PC and it works!

Almost forgot about the activation.

create .desktop
First will be change the scheme using [Matlab-Schemer][schemer]
Change keyboard shortcut back to Windows than the default Emacs.
pathdef.m

set mouse thing

## Sources
- [AUR-matlab]: https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=matlab
- [matlabcentral-matlab window]: https://www.mathworks.com/matlabcentral/answers/364551-why-is-matlab-unable-to-run-the-matlabwindow-application-on-linux
- [matlabcentral-temp dir]: https://www.mathworks.com/matlabcentral/answers/388570-how-can-i-change-the-temp-directory-the-matlab-installer-uses
- [se-increase mount]: https://unix.stackexchange.com/a/400140
- [matlabcentral-unable to locate]: https://www.mathworks.com/matlabcentral/answers/98390-when-running-the-matlab-installer-why-do-i-see-the-error-unable-to-locate-required-installation-fil
- [schemer]: https://github.com/scottclowe/matlab-schemer
