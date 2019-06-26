# git hooks

## format golang code before commit

the following code auto format go source code.

```shell
#!/bin/bash

source ~/.bash_profile


# get changed go files
# https://git-scm.com/docs/git-diff#Documentation/git-diff.txt---diff-filterACDMRTUXB82308203
# Add Copy Modify
gofiles=$(git diff --cached --name-only --diff-filter=ACM | grep '.go$')
[ -z "$gofiles" ] && exit 0

# get unformatted go files
unformatted=$(gofmt -l $gofiles)
[ -z "$unformatted" ] && exit 0

# format go files and auto add to cache
for fn in $unformatted;do
    echo "format file: ${fn}"
    gofmt -w "${PWD}/${fn}"
    [[ $? -ne 0 ]] && exit 1
    git add ${fn}
done
```

### git rebase: merge commits

- git rebase -i HEAD~2
- select Strategy
- git push origin branch-name --force

```text
pick c586193 [fix] fix bug 1
pick 48dbe49 [feat] add new feature

# Rebase 96bbce5..48dbe49 onto 96bbce5 (2 commands)
#
# Commands:
# p, pick = use commit
# r, reword = use commit, but edit the commit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup = like "squash", but discard this commit's log message
# x, exec = run command (the rest of the line) using shell
# d, drop = remove commit
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
# Note that empty commits are commented out
```

other option 
- abort: git rebase --abort
