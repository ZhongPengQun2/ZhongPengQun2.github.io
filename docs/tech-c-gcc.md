## Assembly Language
- Visualization
  - EMU8086
    - Download: http://course.xmu.edu.cn/meol/common/script/download.jsp;jsessionid=A9DD7AB654462FCB2B8E6F0DB734473B.TM2?fileid=287937&resid=53034&lid=12751
- 从零开始实现一个汇编模拟器——初 https://juejin.cn/post/6910914774582689800
- 8051 simulator https://www.google.com.hk/search?q=51+single+chip+emulator&newwindow=1&hl=zh-CN&tbm=vid&ei=R4CDY4_NELWrz7sPw42vgAw&start=10&sa=N&ved=2ahUKEwjPjP7g1M77AhW11XMBHcPGC8AQ8NMDegQIDRAW&biw=1645&bih=788&dpr=2#fpstate=ive&vld=cid:29eaeca1,vid:nO3KrnogwEo

- 用8086汇编写一个hello-world
- 8086汇编语言适用的cpu，51单片机适合吗？
  - references: https://www.zhihu.com/question/485929480

- 8051 汇编语言

## linux 0.11
- linux lab https://gitee.com/tinylab/linux-lab#https://gitee.com/link?target=https%3A%2F%2Ftinylab.org%2Fcloud-lab
- 运行linux 0.11

## How to use Linux command `man`
- Man a specific option ?
  ```shell
  press `/-O` to search `man -O`
  ```

- 假如不想提供源码给别人可以有哪些操作？

## Some C open source projects
https://zhuanlan.zhihu.com/p/584992915

## GCC
- Bilibili 小布老师gcc https://www.bilibili.com/video/BV1rJ411V7EV?p=4&vd_source=397a53882c67614973bf614e08b1047f
	- 系统头文件与目录
		- /usr/local/include/
		- /usr/include/
		- /usr/local/lib/
		- /usr/lib/
	- search path
		- `-I`
			- 有了`-I`,可以提供compatible, #include</tmp/myhead.h>可以写成#include<myhead.h>
		- `-L`
	- archiver: ar
		- `.a`文件(库文件)是 archive文件的缩写吧？即多个.o文件的打包
		- ar cr libhello.a func1.o func2.o
	- 看到了 https://www.bilibili.com/video/BV1rJ411V7EV?p=7&vd_source=f209dde1a1d76e06b060a034f36bb756 16分

- 4 stages of compiling a c program
  - pre-processing
    - 预处理阶段主要工作是删除程序中所有的注释、处理以# 开头的命令，如：头文件的展开、宏定义的替换
	- 头文件的作用
		- 头文件就是像 #include<stdio.h> 这样的以 .h结束的文件
    - `gcc -E hello.c -o hello.i` 
  - Compiling
    - process `.i` into assembly language file
    - `gcc -S hello.i -o hello.s`
  - Assembling
    - process assembly language file to object file(binary file)
    - `gcc -c hello.s -o hello.o`
  - Linking
    - 汇编阶段将代码编译成了二进制文件，还需要和系统其他组件（比如标准库、动态链接库等）结合起来才能正常运行，比如调用print函数打印，在预处理阶段也只是将“stdio.h”头文件中的申明引入进来，没有函数的实现，那怎么调用它的呢？这就是链接的工作了，链接之前的操作都是对一个文件进行处理，而链接可以看作是对多个文件进行“打包”的过程，它将所有的目标文件以及系统组件组合成一个可执行文件。
    - `gcc hello.o -o hello`
  - What is `a.out` ? Which stage does it stuatide at ?

- key options
  - For `CFLAGS`
    - `-l`, `-L`
      ```shell
      gcc -l links with a library file.
      gcc -L looks in directory for library files.
      ```
    - `-O`
    - `-fPIC`
    - `-D
  - For `LDFLAGS`
    - `-lxxx`
    - `-Ldir`
    - `-WL, option`
    - `-static`
    - `-s`
  - `LIBS`

- https://www.bilibili.com/video/BV1RV411v75E/?spm_id_from=333.337.search-card.all.click
below are my notes of this video tutorial.

- Configure
  - CPPFLAGS
  - LDFLAGS

- 链接器 ld
- ldd
- ldconfig

- https://www.cnblogs.com/god-of-death/p/12767113.html

### C++
- 项目列表：https://www.zhihu.com/question/332778359/answer/2266754313
- 项目学习：https://github.com/SamyPesse/How-to-Make-a-Computer-Operating-System
           https://github.com/wanttobeno/Screenshot
           https://github.com/tangziwen/CubeMiniGame
- NB: https://github.com/OneLoneCoder

- void 类型
  - https://www.runoob.com/cplusplus/cpp-data-types.html
- wchar_t 宽字符型
- 泛型编程
  - 何谓泛型编程？其伟大之处何在？ https://zhuanlan.zhihu.com/p/356871099
- STL


### note

```
    In file included from src/kerberos.c:19:0:
    src/kerberosbasic.h:17:10: fatal error: gssapi/gssapi.h: No such file or directory
     #include <gssapi/gssapi.h>
              ^~~~~~~~~~~~~~~~~
    compilation terminated.
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

google搜索：   src/kerberosbasic.h:17:10: fatal error: gssapi/gssapi.h: No such file or directory
```    

### Make
- references:
    - https://zhuanlan.zhihu.com/p/499175729
- make --dry-run
- =,:=,?=
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


`LD_RUN_PATH和LD_LIBRARY_PATH是干什么的?`

- What's runtime ?

- /etc/localtime
- apt-get update
- 动态库 & 静态库
- 向下兼容、向后兼容、向上兼容、向前兼容

- 动态库与静态库
- 动态编译和静态编译
- what's standard output standard input ?

GCC编译选项CFLAGS参数
https://www.cnblogs.com/god-of-death/p/12767113.html

- gcc -Wall main.c /usr/lib/libm.a -o calc
	- 等同于 gcc -Wall main.c -lm -o calc
		- `-lm` will attempt to link object files with a lib file `libName.a` in the standard lib directories
		- 这种约定有点让人难以理解
		- 如果该lib不在standard lib directory又会如何处理?


linux编译参数CPPFLAGS、CFLAGS、LDFLAGS参数的理解
https://blog.csdn.net/lailaiquququ11/article/details/126691913

### EMU8086
### 嵌入式
- DSP VS CPU
    - https://baijiahao.baidu.com/s?id=1745189115970588604&wfr=spider&for=pc
- Compile
    - 编译的种类
- 哪种汇编语言好学 ?


Assembly language playground:
- https://homes.cs.washington.edu/~kaedenb/courses/cse351/x86-viz/
