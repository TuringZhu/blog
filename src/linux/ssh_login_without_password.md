# SSH login without password

## geneate public and private key

- check public & private key

run `ls ~/.ssh/` command, if you saw the following output:

```text
id_rsa      id_rsa.pub  known_hosts

```

it tell you that you have generated public and private key, then you can skip to the second section and ignore the following part in this section.

- generate public and private key 

```
$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/Turing/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /tmp/id_rsa.
Your public key has been saved in /tmp/id_rsa.pub.
The key fingerprint is:
SHA256:9lmlaZp0pPuiug+Vdq0ltHKCEQbhSzQLR2IXVi5Tdcg Turing@zxd
The key's randomart image is:
+---[RSA 2048]----+
|  +.@==o...      |
| . O * .E.       |
|    * o   . . .  |
|   . + o o = +   |
|    . . S B O    |
|       + B %     |
|      .   B      |
|       .  ..     |
|      o+o. ..    |
+----[SHA256]-----+
```

## add public key to remote host

- login remote host with password 

```shell
ssh -p 222 root@1.1.1.1
```

- create `~/.ssh/` path

if you have `~/.ssh/` on remote host, please skip this step

```shell
mkdir -p ~/.ssh/
```

- add public key to `authorized_key`

`echo {{you local host id_rsa.pub content}} >> ~/.ssh/authorized_key`

- logout remote host
- login without password for check