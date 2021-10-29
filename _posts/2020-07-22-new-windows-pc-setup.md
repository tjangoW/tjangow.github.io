---
# optional when the title is not the file name
title: new windows pc setup
tags: windows, setup
---

How I set up a Windows (10) PC when I first get it.
Note: all `preformatted text` are mostly package names for chocolatey.

**There are some new updates from [Chris Titus Tech](https://christitus.com/debloat-windows-10-2020/), but I haven't got the time to go through them.**

## basic
- Unbox, physical inspection and setup, charge!
- Boot up and go though the Windows initial setup
- create restore point
- windows update, manufacturer (hardware driver, BIOS) update
- enable bitLocker (since some BIOS update might need to decrypt the drive etc)
- install [chocolatey]
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))```
- Debloat windows
    - [Windows10Debloat][win10debloat]
    - [Windows 10 Setup Script][win10 Setup] (for winver>= 2004)
    - [OOSU10][O&O Shutup 10] `shutup10`
    - Uninstaller `bulk-crap-uninstaller ccleaner`
- Disable windows store update

## Additional Programmes
### Utility
- Browser `firefox`
    - Sign in to sync stuff
    - or set up yourself everytime
    - [Dark mode for firefox](2020-06-2020-06-22-dark-fox.md)
    - plugins/add-ons (uBlock Origin, Privacy Badger, BitWarden, Auto Tab Discard, Facebook Container, Flagfox, Simple Tab Groups, VirusTotal scan etc)
- [Cloud sync](#cloud)
- Office tools, Email client

### Transfer from another PC
- Greenshot `greenshot` + sync util to screenshot settings
- `mousewithoutborders` Windows only or `barrier` for cross platform 
- environment variables

### Work
- VPNs
- IDE
  - Visual Studio (C++)
  - JetBrains
  - VS Code
    ```sh
    code --list-extensions    # to save all extensions and
    code --install-extension  # on new pc
    ```
[More programmes](#all-programmes-in-categories) somewhat sorted at the end of the page.

## later on
- Settings -> Update & Security -> For developers
  - Developer mode
  - File Explorer options
- Startup
  - Good guide from [ChrisTitusTech][CTT startup]
- Disable animations _Adjust the appearance and performance of Windows_
  - What I leave activated are _Enable Peek, Show thumbnails, Show windows contents, smooth edges, Smooth-scroll_
- re-enable windows media player [Microsoft help][MS media player help] (for Preview in QTTabBar)
  - Apparently, just activating in the new windows settings won't work.
    Go to the very bottom of _Optional features_ -> _More Windows features_ to get the old _Windows Features_, activate _Media Features->Windows Media Player_
- set up git credentials
  - if you want to have multiple SSH keys, take a look at this [post][Multiple SSH keys guide]
- default app
- disable web search at Start Menu ([Guide from howtogeek][HTG Disable web search], check the *.reg file!)
- Settings
  - System
    - Storage: Turn off Storage Sense
    - Shared experiences
    - Clipboard
    - Remote Desktop
    - power & sleep: adjust sleep time
  - Networking -> WiFi
    - on random hardware addresses
    - off Hotspot 2.0 networks
  - Devices
    - Mouse: theme & size
    - Typing: auto-correction
    - Pan & windows Ink - uncheck all
  - Search
    - Permission & History
    - Searching Windows -> Advance Search Indexer Settings
      - _Advanced -> Index location_ so that when I run TreeSize, I know to ignore it directly
      - Clean up unnecessary locations
          - If you use PowerToys Run, you still need windows indexing
          - If you want Outlook and search function, do not disable it entirely
  - Privacy
  - Update -> Delivery Optimisation
- Mouse theme & size
- Save battery: dim screen but not sleep directly!
  - Settings -> Personalisation -> Lock Screen: set to Slideshow temporarily, then Advanced settings
    - disable 'When my PC is inactive, show lock screen instead of turning off the screen'
  - Settings -> System -> Power & sleep: 
- clean up services.msc
- create symbolic link privilege
  - local security policy -> security settings -> local policies -> User rights assignment -> Create symbolic links
    - check `Groups` in object type, then type in `Users`

---
## All programmes in categories
### util
- `chocolateygui`
- `choco-cleaner`
- `shexview`
- `shmnview`
- `mousewithoutborders`
- `barrier`
- `path-copy-copy`
- `coretemp`
- `treesizefree`
- `LinkShellExtension`
- `hashmyfiles`
- `kde-mover-sizer`
### cloud
- `cryptomator`
- `cyberduck`
- `owncloud-client`
- `dropbox`
- `googledrive`
- `megasync`
### alternatives
- `qttabbar`
- `ditto`
- `greenshot`
- `7zip`
- `peazip`
- `everything` instead of Windows search
- `powertoys`
- `sumatrapdf` and `foxitreader`
- `irfanview` and `irfanviewplugins` to browse picture
- `mpc-hc`
  - Go to _View->Options->Player->Formats_ and associate the format you what
- `paint.net`
### misc
- `inkscape`
- `speedtest`
- `microsoft-teams`
- `signal`
- `zoom`
- `teamviewer`
#### Latex
- `miktex`
- `texstudio`
#### programming
- `git`
- `tortoisesvn`
- `winmerge`
- `notepadplusplus`
- `nano`
- `powershell-core`
- `ConEmu`
- `procexp`
- `vscode`
- `FiraCode`
- `cmake`
- `ninja`
- `python3`
- `swig`
- `jdk8`
- `miniconda3`
- `sqlitebrowser`
- visual-studio
- CLion
- Intel Parallel Studio

---
## Sources
- [Chris Titus Tech debloats Windows 10][CTT debloat 2020]

[win10debloat]: https://github.com/Sycnex/Windows10Debloater
[chocolatey]: https://chocolatey.org/install
[win10 Setup]: https://github.com/farag2/Windows-10-Setup-Script/releases
[O&O Shutup 10]: https://www.oo-software.com/en/shutup10
[CTT startup]: https://christitus.com/clean-up-windows-10/#step-2-clean-up-windows-10-startupfigure-classwp-block-image
[CTT debloat 2020]: https://christitus.com/debloat-windows-10-2020/
[MS media player help]: https://support.microsoft.com/en-gb/help/14209/get-windows-media-player
[Multiple SSH keys guide]: https://medium.com/@thucnc/how-to-specify-different-ssh-keys-for-git-push-for-a-given-domain-bef56639dc02
[Github RSA fingerprint]: https://docs.github.com/en/github/authenticating-to-github/githubs-ssh-key-fingerprints
[Bitbucket RSA fingerprint]: https://community.atlassian.com/t5/Bitbucket-articles/RSA-key-fingerprint-confirmation/ba-p/1114799
[HTG Disable web search]: https://www.howtogeek.com/224159/how-to-disable-bing-in-the-windows-10-start-menu/
