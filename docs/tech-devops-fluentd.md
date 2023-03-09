### kerberos
- https://www.youtube.com/watch?v=5N242XcKAsM


- fluentd splunk
    - fluentd send k8s pods logs to splunk
        - 参考：https://cloud.tencent.com/developer/ask/sof/477135
    
    - TODO: 搭建日志系统之 Fluentd
        - https://www.bilibili.com/video/BV15y4y1m7Fe/?spm_id_from=333.337.search-card.all.click&vd_source=f209dde1a1d76e06b060a034f36bb756

### fluentd
- Installation
- Run
```shell
helm install kfo ${CHART_URL} \
  --set rbac.create=true \
  --set image.tag=v1.16.8 \
  --set image.repository=vmware/kube-fluentd-operator
```

```shell
$ helm install kfo ${CHART_URL}   --set rbac.create=true   --set image.tag=v1.16.8   --set image.repository=vmware/kube-fluentd-operator  --set datasource=crd

$ kubectl logs -f kfo-log-router-5rw5l

2023-03-06 09:14:16 +0000 [warn]: #0 [in_systemd_docker] Systemd::JournalError: No such file or directory retrying in 1s
2023-03-06 09:14:17 +0000 [warn]: #0 [in_systemd_bootkube] Systemd::JournalError: No such file or directory retrying in 1s
2023-03-06 09:14:17 +0000 [warn]: #0 [in_systemd_kubelet] Systemd::JournalError: No such file or directory retrying in 1s
```


For locally investigation, you can register a fluentd cloud log. e.g https://www.loggly.com/
    - loggly
        - token: https://zhongpengqun.loggly.com/tokens


- 如何使用 fluentd plugin

- https://github.com/marcel-dempers/docker-development-youtube-series/blob/master/monitoring/logging/fluentd/introduction/readme.md



- elasticsearch & kibana
    - reference: https://levelup.gitconnected.com/docker-compose-made-easy-with-elasticsearch-and-kibana-4cb4110a80dd
        - `docker-compose.yml`

        ```shell
        version: "3.0"
        services:
        elasticsearch:
            container_name: es-container
            image: docker.elastic.co/elasticsearch/elasticsearch:7.11.0
            environment:
            - xpack.security.enabled=false
            - "discovery.type=single-node"
            networks:
            - es-net
            ports:
            - 9200:9200
        kibana:
            container_name: kb-container
            image: docker.elastic.co/kibana/kibana:7.11.0
            environment:
            - ELASTICSEARCH_HOSTS=http://es-container:9200
            networks:
            - es-net
            depends_on:
            - elasticsearch
            ports:
            - 5601:5601
        networks:
        es-net:
            driver: bridge
        ```


- @type tail

- match标签




#### plan
- create a docker image that print 'hello world' continously.
- push this image to docker.io



- forward to external elaticsearch ?