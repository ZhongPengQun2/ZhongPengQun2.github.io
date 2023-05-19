### Makefile
- references:
    - https://zhuanlan.zhihu.com/p/499175729
- Terms
    - target
    - recipe
- make --dry-run
- =,:=,?=
    - ?= indicates to set a variable only if it's not set/doesn't have a value.
        For example:
        ```
        KDIR ?= "foo"
        KDIR ?= "bar"

        echo $(KDIR)
        Would print "foo"
        ```

- .PHONY
```
这样，即使再有名为clean的文件存在，make也会执行clean后面的命令
```
- firstword， wildcard, patsubst
    - wildcard
    ```
    wildcard 用来明确表示通配符。因为在 Makefile 里，变量实质上就是 C/C++ 中的宏，也就是说，如果一个表达式如 objs = *.o ，则 objs 的值就是 *.o ，而不是表示所有的 .o 文件。若果要使用通配符，那么就要使用 wildcard 来声明 * 这个符号，使 * 符号具有通配符的功能
    ```
- CMake    https://www.hahack.com/codes/cmake/
- Makefile variables
    - `MAKEFILE_LIST` make程序在读取makefile文件的时候将文件名加入此变量，多个文件用空格隔开
- Makefile函数
    - abspath
    - patsubst
    ```shell
    $(patsubst %.c,%.o, a.c b.c)
    把字串“a.c b.c”符合模式[%.c]的单词替换成[%.o]，返回结果是“a.o b.o”
    ```
- include
```
为什么要include其他文件呢?

    对于一些通用的变量定义、通用规则，写在一个文件中，任意目录结构中的makefile想要使用这些通用的变量或规则时，include指定的文件就好了，而不用在每个makefile中又重写一遍。
    对于源文件自动生成依赖文件(makefile之目录搜索＆自动依赖)时，将这些个依赖关系保存成文件，在需要使用时include进来，这样少了人为的干预，同时也减少的错误的发生。
```
- If not find variable, it may in the include makefile, e.g. $(CP), $(ZIP)
- all
- makefile中打印变量

- 条件判断
    - ifndef
        - 貌似c++也有该关键字







#### Tutorials
- Makefile简明教程
    - https://www.zhaixue.cc/makefile/makefile-ifeq.html
