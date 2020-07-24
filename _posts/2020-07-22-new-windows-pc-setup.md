---
# optional when the title is not the file name
title: new windows pc setup
tags: comma, separated, tags
---

How I set up a Windows (10) PC when I first get it.
Note: all `preformatted text` are package names for chocolatey.

## basic
- Unbox, physical inspection and setup, charge!
- Boot up and go though the Windows initial setup
- create restore point
- windows update, manufacturer (hardware driver, BIOS) update
- enable bitLocker (since some BIOS update might need to decrypt the drive etc)
- install [chocolatey].
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))```
- Debloat windows
    - [Windows10Debloat][win10debloat]
    - [Windows 10 Setup Script][win10 Setup] (for winver>= 2004)
    - [OOSU10][O&O Shutup 10]
    - Uninstaller `bulk-crap-uninstaller ccleaner`
- Disable windows store update

## Additional Programmes
### utility
- Browser `firefox`
    - Sign in to sync stuff
    - or set up yourself everytime
    - [Dark mode for firefox](2020-06-2020-06-22-dark-fox.md)
    - plugin settings (stylus)
- Cloud sync `owncloud-client dropbox googledrive`
- Office tools, Outlook

### transfer from another PC
- Greenshot + sync util to screenshot settings
- `mousewithoutborders`
- sync `sqlitebrowser`
- environment variables

### Work
- VPN
- IDE
    - Visual Studio (C++)
    - JetBrains
    - VS Code
        - `code --list-extensions` and `code --install-extension`

### All programmes in categories
#### util
- `chocolateygui`
- `shexview`
- `shmnview`
- `mousewithoutborders`
- `path-copy-copy`
- `coretemp`
- `treesizefree`
- `linkshellextension`
#### cloud
- `cryptomator`
- `cyberduck`
- `owncloud-client`
- `dropbox`
- `googledrive`
#### alternatives
- `qttabbar`
- `ditto`
- `greenshot`
- `7zip`
- `peazip`
- `everything`
- `powertoys`
- `sumatrapdf`
- `irfanview`
- `mpc-hc`
- `paint.net`
#### misc
- `inkscape`
- `speedtest`
- `microsoft-teams`
- `signal`
- `zoom`
#### Latex
- `miktex`
- `texstudio`
- `texmaker`

#### programming
- `FiraCode`
- `notepadplusplus`
- `powershell-core`
- `ConEmu`
- `procexp`
- `winmerge`
- `git`
- `tortoisesvn`
- `cmake`
- `ninja`
- `python3`
- `swig`
- `vscode`
- visual-studio
- CLion
- Intel Parallel Studio

### tmp
- `teamviewer`

## later on
- Settings -> Update & Security -> For developers
    - Developer mode
    - File Explorer options
- Windows indexing
    - _Advanced -> Index location_ so that when I run TreeSize, I know to ignore it directly
    - Clean up unnecessary locations
        - If you use PowerToys Run, you still need windows indexing
        - If you want Outlook and search function, do not disable it entirely
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

### from old notes
- remove cortana
  - comp/admin/wind/DataCollection/search -> disable cortana
- [privacy on Chris titus](https://www.youtube.com/watch?v=yXaYszT11CA) or just use [third party](https://www.oo-software.com/en/shutup10)
  - services
    - Connected User Experiences
    - dmwappushservice
  - gp editor / registry
    - comp/admin/wind/DataCollection/Telemetry -> 0
  - task
    - Microsoft/wind/Application Experience & Customer Experience -> disable all
- setting
  - system
    - power & sleep
      - adjust sleep time
    - storage (in case have multiple hard disc)
  - devices
    - mouse size!
    - Typing
      - [ ] autocorrect misspelt words
    - Pan & windows Ink - uncheck all
  - personalisation
    - colours -> dark theme
    - start
      - remove show more tiles

## Sauces
[Chris Titus Tech debloats Windows 10][CTT debloat 2020]

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
