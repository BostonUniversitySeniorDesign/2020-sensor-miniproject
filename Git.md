# Git basics

When working on almost any software project, including solo projects,
we typically use Git "branches" to be able to try out features and
fix bugs without breaking the "main" default branch code.
For this project, you likely have "forked" this project via the
GitHub "fork" webpage button at the top right.

To keep your miniproject up to date with bug fixes and clarifications from the class:

1. set this repo as "upstream":

    ```sh
    git remote add upstream https://github.com/BostonUniversitySeniorDesign/2020-sensor-miniproject.git
    ```
2. sync your fork to upstream (each time you want to sync)

    ```sh
    git switch main

    git fetch upstream
    git rebase upstream/main
    ```

If there are merge conflicts, you can
[resolve the conflicts](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line).
if you'd rather not resolve the conflicts right now you can abort the process by

```sh
git rebase --abort
```

## Git commands to be careful with

Git is not a backup system, and some Git commands can irrecoverably erase large amounts of work, including on the remote server.
These commands are useful for experienced users but can cause trouble if not used carefully.
Such commands include:

```
git reset
git push --force
git push --mirror
```
