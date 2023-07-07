- Shell有哪些数据类型?
	- 数组
		- 如何操作数组？获取某个item，获取整个数组length，获取所有items

- 各个标点符号在shell中的含义..
	- ()
	- (())
	- []
	- [[]]
	- {}	

- 单引号与双引号的区别
- linux shell file中cd到某个目录，然后当前路径变化，怎么弄？

- How to write POSIX compliant shell script ? To avoid bash-isms.

### man 命令的使用
- 如何快速查看某个flag的用法？
- `使用man命令查看etc下的文件不需要给出完整地路径，只需要给出文件名即可`
	- man password
	- man 5 password


### Shell
- bash VS zsh
- Is it possible to write a game by shell script ?
	- Yes, tetris by shell, https://github.com/liungkejin/Bash-Games/blob/master/tetris.sh
- $(1) means ?
- What does colon do in path ?
- eval
- chmod u+x
	-
- make -p
- tar
  - `--strip-components`
- declare
	- https://www.runoob.com/linux/linux-comm-declare.html


```shell
curl --unix-socket /var/run/docker.sock http://localhost/version
```

- whatis

```
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

## Shell
```Shell
tar zcvf dist.tar.gz -C dist 
```

Shell 中的 `:=` ?

make all

```shell
ldconfig
```

```
symbolic links & hard links
```


```shell
vzhong@vzhong-vm-2:~/osspi-cli$ sudo ln -s /home/vzhong/osspi-cli/build/resources/openssl/Openssl-3.0.5/lib64/libcrypto.so.3 /usr/lib/libcrypto.so.3
```

```shell
$ sudo ln -s /home/vzhong/osspi-cli/build/resources/openssl/Openssl-3.0.5/lib64/libssl.so.3 /usr/lib/libssl.so.3
```

- 软连接(symbolic link aka soft link)与硬链接(hard link)的区别
	- inode
		- A file in the file system is basically a link to an inode.
		- A hard link, then, just creates another file with a link to the same underlying inode.
	- just like shortcut in windows
	- softlink's inode number is different from origin file's inode number
		- shortcut will be invalid when origin file is deleted, as well as softlink
	- why soft link ?
	- Hard link
		- Different name of the same file
		- same inode number, same file size
		- just like a copy of origin file
		- if origin file is deleted, hard link still contains the data.
	- How to create a hard link ?
	```
	ln sfile1file link1file
	```

- /usr/bin/aws vs /usr/local/bin/aws

```shell
openssl: error while loading shared libraries: libssl.so.3
```


```shell
/usr/bin/install -c /home/vzhong/glibc/glibc-2.36/build/elf/ld.so /lib64/ld-linux-x86-64.so.2.new
mv -f /lib64/ld-linux-x86-64.so.2.new /lib64/ld-linux-x86-64.so.2
rm -f /usr/bin/ld.so.new
Inconsistency detected by ld.so: dl-call-libc-early-init.c: 37: _dl_call_libc_early_init: Assertion `sym != NULL' failed!
Makefile:1390: recipe for target '/usr/bin/ld.so' failed
make[2]: *** [/usr/bin/ld.so] Error 127
make[2]: Leaving directory '/home/vzhong/glibc/glibc-2.36/elf'
Makefile:484: recipe for target 'elf/subdir_install' failed
make[1]: *** [elf/subdir_install] Error 2
make[1]: Leaving directory '/home/vzhong/glibc/glibc-2.36'
Makefile:12: recipe for target 'install' failed
make: *** [install] Error 2
```

```shell
Inconsistency detected by ld.so: dl-call-libc-early-init.c: 37: _dl_call_libc_early_init: Assertion `sym != NULL' failed!
```

- echo $?

- OS
  - Lock
  - linux cpio

- xrdb
- build-essential
- ttyd

### Alpine Linux

### busybox
- busybox包含的400多个常用命令，是哪400个？



- 各个不同type shell之间的语法区别

```
$ VERSION_DIFF=`git diff master..develop | VERSION.txt`
fatal: ..: '..' is outside repository
VERSION.txt: command not found
```

```
set +x
```

- grep

- function的参数怎么传？比如传个path /tmp/xx.sh 时


- set -e
	- 在shell脚本开头加上set -e，这句话告诉bash 如果任何语句的执行结果不是true，就直接退出shell脚本
- set +e
	- set +e 表示关闭 -e选项，即使出错也依然向下执行脚本
- set -x

- echo $?
	- 取的上条命令的返回值


- 单引号 & 双引号
```shell
$ echo $mm1
master_python3

$ echo $mm2
develop

$ git branch | grep -vw "$mm1\|$mm2"
  develop_python3
  master
  topic/vzhong/PORSCHE-5409-Push-versioned-osstpclients-bundle-to-Artifactory
  topic/vzhong/PORSCHE-5770-Remove-confusing-log-output-from-the-osstp-load
  topic/vzhong/PORSCHE-5836-Confusing-output-in-osstp-load-Skipped-creation-of-129-requests
  vz-test
  vz-test-2
  vzhong-production-mock

$ git branch | grep -vw '$mm1\|$mm2'
  develop
  develop_python3
  master
* master_python3
  topic/vzhong/PORSCHE-5409-Push-versioned-osstpclients-bundle-to-Artifactory
  topic/vzhong/PORSCHE-5770-Remove-confusing-log-output-from-the-osstp-load
  topic/vzhong/PORSCHE-5836-Confusing-output-in-osstp-load-Skipped-creation-of-129-requests
  vz-test
  vz-test-2
  vzhong-production-mock
  ```


- To copy ownership of one file to another
	- chown --reference=greek1 greek2
		- changed ownership of 'greek2' from root:root to root:group1
		

- curl -X DELETE

- $ tar -zcf /tmp/ttest/ff.tar.gz /tmp/ttest/*
  tar: Removing leading `/' from member names
	- 去除文件名中前导的根目录“/”，tar 命令在压缩文件时，默认会取相对路径，不会取从根路径下来的绝对路径，所以，如果待压缩的源路径是绝对路径，便会报该错误

- .tar.bz2  VS .tar.gz
	- .tar.gz (or shorter .tgz)
	- bzip2是一个压缩能力更强的压缩程序，.bz2结尾的文件就是bzip2压缩的结果。与bzip2相对的解压程序是bunzip2。tar中使用-j这个参数来调用gzip。下面来举例说明一下：
	tar -cjf all.tar.bz2 *.jpg
	解压： tar -xjf all.tar.bz2


- lsof
	- lsof 没任何显示，或没有期望的显示，也有可能是没用sudo

有没有这样的工具，比如我在一个shell文件里输入 cp -, 然后会有参数提示 ？

- sed
	- 提取 xx 和 yy 之间的字符
		- 

- $ curl -G -d 'g=publish' -d 'a=osstpclients3' https://microhard.com/api/test/latestVersion

```
 [[: not found

bash有[[, 但是sh没有该语法
```

- mount
	- 查看已经mount的目录
		- 要查看当前系统中的所有挂载点，可以直接在终端中输入 mount 命令
	- sudo mount -t nfs -o nolock x.si01.oc.xxx.com:/xxx /tmp/yyy
		- sudo umount /tmp/yyy