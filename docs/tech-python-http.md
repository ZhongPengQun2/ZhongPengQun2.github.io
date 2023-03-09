### Django doc notes
```
https://www.django-rest-framework.org/api-guide/serializers/

Expanding the usefulness of the serializers is something that we would like to address. However, it's not a trivial problem, and it will take some serious design work
扩展序列化程序的有用性是我们想要解决的问题。然而，这不是一个微不足道的问题，它需要一些认真的设计工作
```

- django serializer & drf serializer
- what should a serializer be ? i mean how to design a suitable serializer ?


#### Software lifecycle
- product & release
- release
    - refers: https://en.wikipedia.org/wiki/Software_release_life_cycle
    - alpha & beta & RC & GA release
        - RC
    - milestone release



#### jekyll
```shell
docker run -it  --rm jekyll/jekyll:3.5 bash

bundle exec jekyll serve

# gem sources -a http://gems.ruby-china.org
Error fetching http://gems.ruby-china.org:
        no such name (http://gems.ruby-china.org/specs.4.8.gz)



install ruby in ubuntu18.04 container by source code
https://tool.4xseo.com/article/501208.html
```


```shell
# kubectl get pods
The connection to the server localhost:8080 was refused - did you specify the right host or port?

[resolve] https://blog.csdn.net/a506681571/article/details/86086005

systemctl start etcd
systemctl start docker
systemctl start kube-apiserver
systemctl start kube-controller-manager
systemctl start kube-scheduler
systemctl start kubelet
systemctl start kube-proxy
----------------

```shell
# minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Stopped
kubeconfig: Configured

- 如何查看 apiserver 的 log ?
```

  - Django
      - Develop django project by docker.
      - safe url
      - url endswith '/' & not endswith
      - Path Parameters
      - setup project from legacy database
      - ALLOWED_HOSTS
        - HTTP Host header attacks
  - Django-rest-framework
      - 2种url参数的区别，为什么要这样？