比较适合什么领域？
https://www.zhihu.com/question/57404512


Go 包管理工具 dep 和 go module 的对比
https://liqiang.io/post/golang-package-manager-compare-module-vs-dep-d1b2db90
    - 从 dep 迁移到了 go module


- go build
    - 将 .go 文件build成可执行文件
    
- GOPATH vs GOROOT vs GOBIN
    - 我们开发 Golang 项目时，需要依赖一些别的代码包，这些包的存放路径就与 GOPATH 有关。
    - GOROOT 表示 Go 的安装根目录，也就是 Go 的安装路径
    - `然后将可执行文件安装在$GOBIN的位置`

- go.mod
    - 使用go mod
        - 首先，必须升级go到1.11,目前版本是1.14

- 升级go版本
    - ubuntu下安装指定版本, e.g go1.20.2
```
wget  https://go.dev/dl/go1.20.2.linux-amd64.tar.gz
tar -xvf go1.20.2.linux-amd64.tar.gz 
mv go /usr/local
export GOROOT=/usr/local/go 
export PATH=$GOROOT/bin:$PATH
go version 
```

- GO111MODULE
```
GO111MODULE 有三个值：off, on和auto（默认值）。

GO111MODULE=off，go命令行将不会支持module功能，寻找依赖包的方式将会沿用旧版本那种通过vendor目录或者GOPATH模式来查找。
GO111MODULE=on，go命令行会使用modules，而一点也不会去GOPATH目录下查找。

```

- GOPROXY



```
error obtaining VCS status: exit status 128

- 原因：是因为我们的go版本太高了！因为之前安装的go版本是1.18的，是最新版，我们将go的版本降至1.16之后，再执行就可以成功了！
    - 原因可能是对的，但我不想这样解决，治标不治本

- go env -w GOFLAGS="-buildvcs=false"
    - OK,可以
```