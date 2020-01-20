---
title: Safety and security gone crazy (ip_address::port in firefox)
tags: firefox
---

So why firefox directs to the default browser when I enter an ip address with port e.g. `123.45.6.789::8888` in the address bar??
Just to be clear, I was trying to access jupyter lab instance of another computer.
This feature is greatly *appreciated*.
Well, to be fair, I am not at all up-to-date with networking security stuff and sorts,
but seriously?

Anyway, fix for firefox (version 72.0.1): go to [about:config](about:config) (yes, let's live dangerously) 
and set the **keyword.enabled** to **false** (by double-clicking it).

*Sauce*: [some not so related mozilla support post](https://support.mozilla.org/en-US/questions/1213978)
