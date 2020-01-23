---
title: Accidental Step into Build Systems
tags: make, ninja, cmake, c++
---

Out of frustration with visual studio build, where it does only parallel build of projects 
but **NOT** within each project (*.vcxproj file) by default (or maybe someone set so in the cmake), 
I was looking for ways to speed up this.

Found some articles regarding cmake integration within VS2019, tried it out but I'll say there are still 
quite some work for the developers to make it really good.
I had encountered several problems such as not able to stop the build (somehow it is not registered properly i guess),
and a deadly one: for debug and release you will need two configurations, 
which is kind of against the conventions (not to say conventions are good, 
but at least provide a better way to switch between config.
Maybe I was doing it wrong, but I would have to open the CMakeSettings.json, 
select the one I want, and freaking *generate*, which is not something I want everytime I switch between debug and rel yo!).

Anyway, enough complain with Microsoft. Still though this process, I got to know other build tool/toolchain/whichever terms they use
like ninja and hooking them together: cmake-ninja|msbuild-clang|msvc!
After looking up abit, ninja seems to be a tool with performance as its main focus.
Tried to use CMake GUI on Windows to configurate it but was unsuccessful.
There was this error saying that the cl.exe is not able to build the sample tests, which left me to start with cmd stuff.

Within `vcvars64.bat` and `cmake -GNinja` does bring it to work.
At first sight, it is already better telling you how many files are left to be compiled 
(saw somewhere that it can be further customised but will try it later).
One improvement will be to have better integration with IDE. 
Currently by running in the terminal of VSCode, I can click on the links to the error locations.
Would be nicer to somehow scrap the output and display it together like in VS.

Anyway, currently stuck at error C4716 with boost. Am I supposed to change the boost headers? ¯\_(ツ)_/¯

Interesting read on Ninja: https://www.aosabook.org/en/posa/ninja.html
