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
- `vscode`
- visual-studio
- CLion

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
- Disable animations

## Sauces
[Chris Titus Tech debloats Windows 10][CTT debloat 2020]

[win10debloat]: https://github.com/Sycnex/Windows10Debloater
[chocolatey]: https://chocolatey.org/install
[win10 Setup]: https://github.com/farag2/Windows-10-Setup-Script/releases
[O&O Shutup 10]: https://www.oo-software.com/en/shutup10
[CTT startup]: https://christitus.com/clean-up-windows-10/#step-2-clean-up-windows-10-startupfigure-classwp-block-image
[CTT debloat 2020]: https://christitus.com/debloat-windows-10-2020/
