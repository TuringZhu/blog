# cd


```
cd --help
cd: ussage: cd [-L|[-P [-e]]] [dir]
```



- `cd` change to home direcotry(default dir is home)
- `cd -` change to old path


```
Change the current directory to dir. The variable HOME is the default dir. The variable CDPATH defines the search path for the directory containing dir. Alternative directory names in CDPATH are separated by a colon (:). A null directory name in CDPATH is the same as the current directory, i.e., ''.''. If dir begins with a slash (/), then CDPATH is not used. The -P option says to use the physical directory structure instead of following symbolic links (see also the -P option to the set builtin command); the -L option forces symbolic links to be followed. An argument of - is equivalent to $OLDPWD. If a non-empty directory name from CDPATH is used, or if - is the first argument, and the directory change is successful, the absolute pathname of the new working directory is written to the standard output. The return value is true if the directory was successfully changed; false otherwise.
```