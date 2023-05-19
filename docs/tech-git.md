- git refs & tags
    - 经典: http://itmyhome.com/progit/eb04be8dd776142cd3fbb52e27694746/92abc307328bd414f4cd589a4400994b.html
        - 你可以执行像 git log 1a410e 这样的命令来查看完整的历史，但是这样你就要记得 1a410e 是你最后一次提交，这样才能在提交历史中找到这些对象。你需要一个文件来用一个简单的名字来记录这些 SHA-1 值，这样你就可以用这些指针而不是原来的 SHA-1 值去检索了。

        - 每当你执行 git branch (分支名称) 这样的命令，Git 基本上就是执行 update-ref 命令，把你现在所在分支中最后一次提交的 SHA-1 值，添加到你要创建的分支的引用。

        - tags
        Tag 对象非常像一个 commit 对象——包含一个标签，一组数据，一个消息和一个指针。最主要的区别就是 Tag 对象指向一个 commit 而不是一个 tree。
        它就像是一个分支引用，但是不会变化——永远指向同一个 commit，仅仅是提供一个更加友好的名字。
        ```
        $ cat .git/refs/tags/v1.1
        9585191f37f7b0fb9444f35a9bf50de191beadc2
        ```


- tag与commit的关系

- 打标签
    - 何时需要打
    - 怎么打

- 查看有哪些branch merged到了vt2
```
checkout to the branch you want to check, then
$ git pull
$ git branch --merged vt2
```

- head
    - 查看当前head
    - git checkout 到一个新的branch，但是head却是原来的，是这样的吗？

- merge也是一个commit吗？


### Git
- Git
    - git submodule [Chinese: https://www.youtube.com/watch?v=jhl7ruTPV-o]
    - Git branch strategy


- 为什么刚pull下来的repo，git branch却不显示全部的branch，只显示一个branch
```
$ git branch
* develop_python3
```
    - https://git-scm.com/book/en/v2/Git-Branching-Branch-Management
        - If you run it with no arguments, you get a simple listing of your current branches


```shell
$ git branch --merged
* vz-test
$ git merge vz-test-8
Updating fff3cff..af2c4ba
Fast-forward
 VERSION.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
vzhongPG3QC:osstpclients vzhong$ cat VERSION.txt
v88
vzhongPG3QC:osstpclients vzhong$ git merge vz-test-8
Already up to date.
vzhongPG3QC:osstpclients vzhong$ git branch --merged      <--- show local merged
* vz-test
  vz-test-8
vzhongPG3QC:osstpclients vzhong$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 257 bytes | 257.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote:
remote: To create a merge request for vz-test, visit:
remote:   https://gitlab.eng.vmware.com/core-build/osstpclients/-/merge_requests/new?merge_request%5Bsource_branch%5D=vz-test
remote:
To https://gitlab.eng.vmware.com/core-build/osstpclients.git
   fff3cff..af2c4ba  vz-test -> vz-test
vzhongPG3QC:osstpclients vzhong$ git branch -r --merged
  ...
  origin/topic/zhiwew/download_source_for_rpm
  origin/vz-test
  origin/vz-test-3
  origin/vz-test-4
  origin/vz-test-6
vzhongPG3QC:osstpclients vzhong$ git branch
  develop_python3
* vz-test
  vz-test-8
  xxxx
vzhongPG3QC:osstpclients vzhong$ git status
On branch vz-test
Your branch is up to date with 'origin/vz-test'.

nothing to commit, working tree clean
vzhongPG3QC:osstpclients vzhong$ git push
Everything up-to-date
vzhongPG3QC:osstpclients vzhong$ git checkout vz-test-8
Switched to branch 'vz-test-8'
vzhongPG3QC:osstpclients vzhong$ git push
fatal: The current branch vz-test-8 has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin vz-test-8

vzhongPG3QC:osstpclients vzhong$ git push --set-upstream origin vz-test-8
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: To create a merge request for vz-test-8, visit:
remote:   https://gitlab.eng.vmware.com/core-build/osstpclients/-/merge_requests/new?merge_request%5Bsource_branch%5D=vz-test-8
remote:
To https://gitlab.eng.vmware.com/core-build/osstpclients.git
 * [new branch]      vz-test-8 -> vz-test-8
Branch 'vz-test-8' set up to track remote branch 'vz-test-8' from 'origin'.
vzhongPG3QC:osstpclients vzhong$
vzhongPG3QC:osstpclients vzhong$ git checkout vz-test
Switched to branch 'vz-test'
Your branch is up to date with 'origin/vz-test'.
vzhongPG3QC:osstpclients vzhong$
vzhongPG3QC:osstpclients vzhong$ git pull
Already up to date.
vzhongPG3QC:osstpclients vzhong$ git branch -r --merged
  ...
  origin/topic/zhiwew/download_source_for_rpm
  origin/vz-test
  origin/vz-test-3
  origin/vz-test-4
  origin/vz-test-6
  origin/vz-test-8     <-----
```

- gitlab squash
- fast-forward
- git revert

- git 3D
  - Gource

- 丁哥： git merge和git rebase的区别, 切记：永远用rebase

- git pull是针对当前分支还是所有分支？
  - 只针对当前分支，只会拉当前的分支，这种东西一次性更新所有分支，万一有冲突，够你吃一壶。所以基本都是只更新当前分支
    - 你说的不准确，是同步所有的远程分支到本地，只不过只对当前分支进行merge

- How to squash multi commits as one ? when MR merged, we can squash them as one so that to pretty the commit log.

- git clone repo to specific path
  - 

Squash multi commits as one, in this case, what the comment will be like ?


- What is a changeset in Git?
  - source: https://stackoverflow.com/questions/38648491/what-is-a-changeset-in-git
    - 提问者问题：5个files一次commit，是否这5个文件的修改算一个changeset ?
      - https://en.wikipedia.org/wiki/Changeset
        - In version control software, a changeset (also known as commit and revision)