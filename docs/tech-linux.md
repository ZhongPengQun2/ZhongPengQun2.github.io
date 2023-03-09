###
- 标准输出和标准错误流
  - 标准输出流是流向标准输出设备（显示器）的数据。ostream类定义了三个输出流对象：cout，cerr，clog。
    - 来源：https://blog.csdn.net/qq_40456669/article/details/83690636
    - Linux中标准输出和标准错误的重导向： https://zhuanlan.zhihu.com/p/360549100


### Linux
- Kernel Headers
https://unix.stackexchange.com/questions/47330/what-exactly-are-linux-kernel-headers
  - Install kernel headers https://linuxhint.com/install-kernel-headers-debian/
  - History: https://blog.csdn.net/trochiluses/article/details/9390855?spm=1001.2101.3001.6650.14&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-14-9390855-blog-54137564.pc_relevant_3mothn_strategy_and_data_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-14-9390855-blog-54137564.pc_relevant_3mothn_strategy_and_data_recovery&utm_relevant_index=14


### Shell
- bash VS zsh
- Is it possible to write a game by shell script ?
- $(1) means ?
- What does colon do in path ?
- eval
- chmod u+x
- make -p
- tar
  - `--strip-components`




```shell
curl --unix-socket /var/run/docker.sock http://localhost/version
```

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
