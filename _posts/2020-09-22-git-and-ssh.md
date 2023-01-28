---
# optional when the title is not the file name
title: Configuring SSH (keys) and Git
tags: git, ssh
---

This post is about configuring SSH so that you can e.g. login into remote computer with terminal only, use git without password (a bit of controversy here, because the ssh-keys are password in another form IMO).
Actually, for remote terminal, it is possible to login with username as password unless it is restricted.
However, I prefer fancier way of life using SSH keys.

## 1. SSH Key Generation
The first step is generating the so called private-public key pair for this asymmetric encryption.
The public key is what you can share with the whole internet without endangering your secret,
whereas private key should be kept secured just like your everyday passwords.

To generate a private-public key pair, one of the following command can be used:
```bash
$ ssh-keygen -t rsa -b 4096 -C tjango@thisLaptop
$ ssh-keygen -t ed25519 -C tjango@thatDesktop
```
- Not a security expert here, but AFAIK, RSA should have key length >= 3072-bit to be sufficiently secure in current age.
  - To avoid thinking about these, I therefore prefer **ED25519** whenever it is supported.
- My personal preference is to add a comment with the `-C` option as I have multiple identities in a computer.
  Note that this comment does not have to be the email this used for the login specifically.
- As a lazy person, I just leave the *Passphrase* blank
- If the created key has an uncommon name, it (the private key) needs to add to ssh-agent manually as follow:
  ```bash
  $ ssh-add ~/.ssh/id_rsa_whatever_name
  ```

## 2. Remote Side
The next step is to get the public key (with extension `.pub`) to the remote computer somehow.

### Remote Shell with SSH
This is what I presume to be the original intent of SSH.
For this purpose, we have to get the content in our public key into `~/.ssh/authorized_keys` of the remote computer by hook or by crook.
1. the simple way with `ssh-copy-id` utility
    ```bash
    $ ssh-copy-id [-i ~/.ssh/id_some_key.pub] yourLoginName@remoteName
    ```
2. manually, either
   - using SCP and so on as described in [this wiki][archlinux manual key to remote]
   - or simply just SSH to remote, nano/vim the `~/.ssh/authorized_keys`, and paste the content

### Git (GitHub etc)
This is relatively straight forward.
Usually you just need to go to _Settings -> SSH (and GPG) Keys_ and add a new key there.


## 3. Test Connection etc
After all has been set up, I will usually perform a connectivity check to make sure everything is working properly.
```bash
$ ssh -vT yourLoginName@remoteName  # for remote SSH
$ ssh -vT git@github.com            # for git at GitHub. For other host, change accordingly
```
- For the first connection, you will be prompted with a dialogue about the host key fingerprint.
  Do check their websites to verify it.
- If it is not working, check the messages on the terminal to see which keys have been tried for the connection (verbose option is on with the `-v` switch).

## 4. Others
### SSH-Agent
SSH-Agent is a tool to manage SSH-keys (mostly for keys with atypical filenames).
Here are some commands that I have used:
```bash
$ ssh-agent -s  # start the agent
$ ssh-add -l    # show fingerprints of keys
$ ssh-add -L    # show public keys
```
Another way to show fingerprint is with ssh-keygen, which works with both public and private keys.
```bash
$ ssh-keygen -lvf ~/.ssh/id_key  # -v for randomart.
```

### Manage Multiple Git Identities with SSH_Config
In the event where you have multiple identities (e.g. public and personal) on the same host (e.g. Github.com),
it would be a better idea to have a way to manage them so that I would not accidentally use my public personality to push to my private repo.
This is where [ssh_config][man ssh config] comes into play.
In the file `~/.ssh/config`, add the following lines:
```
# private tjango account
Host github-tjango
  HostName github.com
  User tjango
  IdentityFile ~/.ssh/id_ed25519_tjango
  IdentitiesOnly yes

# work account
Host github-work
  HostName github.com
  User workname
  IdentityFile ~/.ssh/id_ed25519_workname
  IdentitiesOnly yes
```
And remember for the remote url, it has to be changed to `github-tjango` and `github-work` respectively (either via git CLI, GUI or directly in `.git/config` file).


### GPG
GPG stands for GnuPG, which is a way to sign digitally.
This way, git can add a verified tag besides your commits, saying that you personally done that.
I am a bit too lazy for this so maybe next time.

---
## References
- [Archlinux Wiki on SSH][archlinux wiki ssh key]
- [Man Page on SSH_Config][man ssh config]
- [GitLab Help][gitlab help]
- [Github Help][github help]
- [jexchan's Gist on Multiple SSH][jexchan multiple SSH]

[GPG signing commit]: https://help.github.com/en/articles/signing-commits
[github help]: https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
[gitlab help]: https://docs.gitlab.com/ee/ssh/README.html
[jexchan multiple SSH]: https://gist.github.com/jexchan/2351996
[archlinux manual key to remote]: https://wiki.archlinux.org/index.php/SSH_keys#Manual_method
[archlinux wiki ssh key]: https://wiki.archlinux.org/index.php/SSH_keys
[man ssh config]: https://man7.org/linux/man-pages/man5/ssh_config.5.html
