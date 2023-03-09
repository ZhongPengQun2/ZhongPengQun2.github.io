### Setup a Splunk server

Run a Splunk server container

```shell
docker run --name splunk -p 8000:8000 -p 8088:8088 -d outcoldman/splunk:6.3.3
```



- Splunk
    - https://www.youtube.com/watch?v=m95GiTF0zd0
    - https://www.youtube.com/watch?v=bO_-fv6e7u4
    - https://medium.com/airwalk/log-aggregation-in-kubernetes-and-transporting-logs-to-splunk-for-analysis-ad8599607372
    - https://cloud.google.com/architecture/logging-anthos-with-splunk-connect?hl=zh-cn
    - k8s logs
        - objects
        - metrics


setup a splunk server:
```shell
docker run --name splunk -p 8000:8000 -p 8088:8088 -d outcoldman/splunk:6.3.3


docker run --name hello --log-driver=splunk --log-opt splunk-token=AEB5A127-3AC2-447C-8E3F-D7027AFE31D1 --log-opt splunk-url=http://139.196.39.92:8088 --log-opt splunk-sourcetype=Docker rickfast/hello-oreilly


docker run --name hello --log-driver=splunk --log-opt splunk-token=A3260AEC-672D-41D2-9B64-8BAB933EA5DE --log-opt splunk-url=http://139.196.39.92:8088 --log-opt splunk-sourcetype=Docker rickfast/hello-oreilly



docker run --name hello --log-driver=splunk --log-opt splunk-token=1620a639-5064-43dc-8d81-72ae38ec639b --log-opt splunk-url=http://10.79.128.59:8088 --log-opt splunk-sourcetype=Docker rickfast/hello-oreilly

minikube start --nodes 4 --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 1

minikube start --nodes 4 --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 1 --driver=docker
```

- vmware kube-fluentd-operator
    - https://pkg.go.dev/github.com/vmware/kube-fluentd-operator#section-readme





```shell
$ curl -k http://139.196.39.92:8088/services/collector/event -H "Authorization: Splunk AEB5A127-3AC2-447C-8E3F-D7027AFE31D1" -d '{"event": "hello world"}'
{"text":"Success","code":0}
```

=============

splunk log success: https://www.youtube.com/watch?v=qROXrFGqWAU&t=11s

curl https://10.79.128.59:8088/services/collector/event -H "Authorization: Splunk 1620a639-5064-43dc-8d81-72ae38ec639b" -d '{"event": "hello world"}'

docker built-in send log to splunk ?
https://www.w3cschool.cn/doc_docker_1_13/docker_1_13-engine-admin-logging-splunk-index.html

install splunk by cmd
https://www.inmotionhosting.com/support/security/install-splunk/

9ED0A79E-F7B8-43DC-B7A0-7B49AE7450B9

```shell
root@iZuf6bpc1lt9qlf2ma9p2lZ:~# helm install anthos-splunk -f values.yaml --namespace splunk-connect https://github.com/splunk/splunk-connect-for-kubernetes/releases/download/1.4.1/splunk-connect-for-kubernetes-1.4.1.tgz

Error: INSTALLATION FAILED: Get "https://github.com/splunk/splunk-connect-for-kubernetes/releases/download/1.4.1/splunk-connect-for-kubernetes-1.4.1.tgz": unexpected EOF
```


```shell
$ kubectl create namespace splunk-connect
$ kubectl config set-context --current --namespace=splunk-connect
$ 
helm install anthos-splunk -f values.yaml --namespace splunk-connect https://github.com/splunk/splunk-connect-for-kubernetes/releases/download/1.4.1/splunk-connect-for-kubernetes-1.4.1.tgz
```

- Splunk indexer


- fluent-plugin-splunk-hec
    - https://github.com/splunk/fluent-plugin-splunk-hec
- kube-fluentd-operator
    - https://github.com/vmware/kube-fluentd-operator