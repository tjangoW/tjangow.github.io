---
# optional when the title is not the file name
tags: wakeonlan, windows
---

Trying to configure wake on lan. Good chunk of setting the remote pc 
from [this post at PCMag](https://www.pcmag.com/how-to/turn-on-computer-from-across-the-house-with-wake-on-lan).

To get the information for sending magic packet, run ``ipconfig /all`` on cmd.
Here I would recommend a trick: ``ping -a <IP-Address>`` and get the PC name.
This way, you would be able to connect to it even if it does not have a static IP.

As for sending the package, I tried NirSoft, but doesn't quite work.
At least with [python WakeOnLan package](https://pypi.org/project/wakeonlan/),
I could check it's working with this [WakeOnLan Monitor](https://www.depicus.com/wake-on-lan/wake-on-lan-monitor).

However, somehow I just could not wake it on Lan :/ Attempted with port 7 and 9.
