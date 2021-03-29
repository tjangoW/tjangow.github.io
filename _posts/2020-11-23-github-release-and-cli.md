---
# optional when the title is not the file name
title: GitHub Release and CLI
tags: github
---

For some reasons, I had to deal with uploading large assets (>600MB) on moderate internet (~10 Mbps) to Github,
which was totally a disaster using the website.
Just an accidental mouse press or for some unknown reasons, the upload fails and has to start over and over again.

Somehow I stumbled upon GitHub CLI (`choco install gh`),
which is a true life saver!
The exact same job that I was trying over hours is done reliably in about 10 minutes
(Not to bad since [TechInternets][calc] estimation is around 9mins)!!
A word on the gh-cli, it is actually something similar to git, 
but manages Github's *specific* stuff like issues, pr, releases etc.

## Sources
- [Github CLI Manual/Docs for Release Upload][gh upload ref]
- [Transfer time calculator from TechInternets][calc]

[gh upload ref]: https://cli.github.com/manual/gh_release_upload
[calc]: https://techinternets.com/copy_calc
