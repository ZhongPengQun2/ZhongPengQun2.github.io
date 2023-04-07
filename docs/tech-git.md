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