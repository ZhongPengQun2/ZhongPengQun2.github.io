#### Steps
```
$ go mod init hello
go: creating new go.mod: module hello
go: to add module requirements and sums:
	go mod tidy

$ go mod tidy
go: finding module for package github.com/gopxl/pixel
go: finding module for package github.com/gopxl/pixel/pixelgl
go: finding module for package golang.org/x/image/colornames
go: downloading golang.org/x/image v0.14.0
go: found github.com/gopxl/pixel in github.com/gopxl/pixel v1.0.0
go: found github.com/gopxl/pixel/pixelgl in github.com/gopxl/pixel v1.0.0
go: found golang.org/x/image/colornames in golang.org/x/image v0.14.0

$ go run main.go
```