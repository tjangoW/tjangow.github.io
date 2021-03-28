---
# optional when the title is not the file name
title: Ignore .GitIgnore
tags: git
---

It is possible to nullify existing ignore entries in `.gitignore` with **negation** with `!`. 
However, in order for this to work, the existing ignore entries should ignore items only with `somedir/*` 
and not the directory `somedir`.


## Sources
- [poke's post on stackoverflow][poke's post on stackoverflow]

[poke's post on stackoverflow]: [www.test.com](https://stackoverflow.com/a/35279076/11837276)
