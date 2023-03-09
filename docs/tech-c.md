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

## How to use Linux command `man`
- Man a specific option ?
  ```shell
  press `/-O` to search `man -O`
  ```

## Some C open source projects
https://zhuanlan.zhihu.com/p/584992915

## GCC
- Bilibili 小布老师gcc https://www.bilibili.com/video/BV1rJ411V7EV?p=4&vd_source=397a53882c67614973bf614e08b1047f
- 4 stages of 

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
    - https://www.zhihu.com/question/20607178
```
再举几个非常常见的例子：
负责数学运算的 math.h：很多精简指令集或嵌入式的低端 CPU 未必会提供做 sin 和 cos 这类三角函数运算的指令，这时它们需要软件实现。
负责字符串的 string.h：你觉得硬件和操作系统会内置「比较字符串长度」这种功能吗？当然也是靠软件实现啦。
负责内存分配的 stdlib.h：直接通过 mmap 这类 OS 系统调用来分配内存是过于底层的，一般也需要有人帮你封装。

换句话说，虽然 C 的 if、for 和函数等语言特性都可以很朴素且优雅地映射（lowering）到汇编，但必然会有些没法直接映射到系统调用和汇编指令的常用功能，比如上面介绍的那几项。对于这些脏活累活，它们就需要由运行时库（例如 Linux 上的 glibc 和 Windows 上的 CRT）来实现。
```


- /etc/localtime
- apt-get update
- 动态库 & 静态库
- 向下兼容、向后兼容、向上兼容、向前兼容

- 动态库与静态库
- what's standard output standard input ?

GCC编译选项CFLAGS参数
https://www.cnblogs.com/god-of-death/p/12767113.html



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

- glibc

### xx
- `.h`文件
  - 是什么，为什么需要`.h`文件？
  - extern
- `.hh`文件
  - .hh 是为了区别 .h，表示 C++ 头文件
- `.cc`文件
  - .cc 是为了区别 .c，表示 C++ 源文件
- C语言关键字