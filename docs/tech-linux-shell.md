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

```Shell
python3 -m ensurepip
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
