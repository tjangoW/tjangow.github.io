---
tags: git
---


So after a file has been committed, even if it's later added into the `.gitignore`, its modification will be still visible. 
For it to be really ignored, you need:
```sh
$ git rm --cached tmp.log
```

*Sauce*: [atlassian](https://www.atlassian.com/git/tutorials/saving-changes/gitignore#ignoring-a-previously-committed)
