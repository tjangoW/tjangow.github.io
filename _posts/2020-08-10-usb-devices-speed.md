---
# optional when the title is not the file name
title: Measure USB Device Speed
tags: usb, hardware
---

How to know which USB flash drive is the fastest?

A quick approach is to use [USB Device Tree Viewer][usbTreeView] by following the guide on a [superuser post by Vinayak][Vinayak post].
With this, you will be able to see the "protocol" that the USB device can operate 
(make sure you plug the USB into blue USB port as well).

If you have a bit more time to spare, there are methods to get the exact read/write speed
based on some benchmark tests.
There are a number of benchmark tools recommended by various authors (e.g. [PcWorld][pcWorld list] and [MakeUseOf][makeUseOf list]).
I will just mentioned a few that I have tried:
1. [USB flash benchmark][usb flash benchmark] seems to be the most popular one (the website seems a bit sketchy but it is fine, I have check VirusTotal for it).
2. [usbflashspeed.com on wayback machine][web.archive usbflashspeed].
    In theory, it should be something like https://cpu.userbenchmark.com/ for USB, 
    but it is not maintained anymore.
3. [Crystal Disk Mark][Crystal disk mark], which has chocolatey package `crystaldiskmark` as well as dark theme!



[usb flash benchmark]: https://www.majorgeeks.com/mg/getmirror/usb_flash_benchmark,1.html
[makeUseOf list]: https://www.makeuseof.com/tag/5-lightweight-tools-to-check-the-speed-of-your-usb-flash-drive-windows/
[usbTreeView]: https://www.uwe-sieber.de/usbtreeview_e.html
[pcWorld list]: https://www.pcworld.com/article/2455205/test-the-speed-of-your-usb-drives.html
[Vinayak post]: https://superuser.com/a/700326
[web.archive usbflashspeed]: https://web.archive.org/web/20190218044149/http://usbflashspeed.com:80/
[Crystal disk mark]: https://crystalmark.info/en/software/crystaldiskmark/
