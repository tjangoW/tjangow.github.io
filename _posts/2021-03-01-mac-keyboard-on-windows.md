---
# optional when the title is not the file name
title: Configure Mac keyboard for use on Windows
tags: windows, keyboard, hardware
---

Unsurprisingly, Mac UK keyboard has different layout than standard (Windows) UK keyboard layout for some symbols.
Unsurprisingly because Mac keyboard in OSX is not friendly for shortcuts users: 
copy uses `cmd + c`, I am totally fine with renaming and reordering, only if it is for better usability, 
BUTTTT seriously, I could not find any finger combinations that can press `cmd` which is just below the `x` key 
comfortably and press other keys simultaneously.

Anyway, here is my steps to getting a near normal windows keyboard experience with Mac keyboard:
1. install [microsoft keyboard layout creator (MKLC)][layout creator download], as there is no Mac keyboard layout in any of its languages.
2. find and download the layout (a `klc` file) for your Mac keyboard. I found the UK keyboard from [Nick's post][klc source].
3. open the MKLC and load the file. If it's all good, build DLL and packages for that.
   - Just a matter of personal preference, I changed the language to EN-US (different from my existing EN-dialect) 
     as the change in language can be done and seen more easily for me.
     Also because the first time I installed and changed the layout, I think on my subsequent reboot, the layout wasn't there in the setting menu, 
     but upon reinstallation I got a message saying it is already there.
     So, the best is either switch your OS, or not fight against it, not like you are gaining anything for uncovering these nonessential bugs.
4. Click on the installer you just created and there you go!
5. (my preference) Remap special keys (with [PowerToys][powertoys gh] or something similar).
   - I did not dig too much into the MKLC, but I think MKLC cannot remap special keys like `ctrl, win, alt`.
     The Mac keyboard somehow have `ctrl-alt-win-space-win-altGr` from left to right, whereas I am used to `ctrl-win-alt` on the left,
     and prefer a `menu` key on the right.
     Only limit: cannot remap `fn` key at the very corner because windows just does not register that.


[klc source]: https://www.linickx.com/macbook-pro-uk-keyboard-layout
[layout creator download]: https://www.microsoft.com/en-us/download/details.aspx?id=102134
[powertoys gh]: https://github.com/microsoft/PowerToys
