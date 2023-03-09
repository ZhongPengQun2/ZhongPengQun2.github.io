### Helm
- Install Helm
    - 
- Charts & release & repo
  ```
  Release 是运行在 Kubernetes 集群中的 chart 的实例。一个 chart 通常可以在同一个集群中安装多次。每一次安装都会创建一个新的 release。以 MySQL chart为例，如果你想在你的集群中运行两个数据库，你可以安装该chart两次。每一个数据库都会拥有它自己的 release 和 release name。
  ```

- https://artifacthub.io/
- repo
  ```shell
  # helm repo list
  NAME    URL                                                    
  splunk  https://splunk.github.io/splunk-connect-for-kubernetes/
  ```



```shell
$ helm install my-splunk-connect -f values.yaml splunk/splunk-connect-for-kubernetes
Error: INSTALLATION FAILED: cannot re-use a name that is still in use

solution:
$ helm delete my-splunk-connect
release "my-splunk-connect" uninstalled
```

- helm3 hello world

- helm lint

