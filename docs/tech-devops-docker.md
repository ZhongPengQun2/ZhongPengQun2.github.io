### Docker
- Docker
    - Use case of docker tags
    - Is it possible that 2 same pods run on one k8s node ?
    - What is overlay ?
    - Network
      - Bridge
      - Host
      - ...
    - docker manifest
    - `Docker Orchestration Files`
    - docker sbom command
    - Configmap
    - 进入pod与进入container的区别？
    - How to get docker disk usage ?  `docker system df`
    - docker export & docker save ?
    - docker import & docker load ?
    - docker export -o english-db-`date +%Y%m%d-%H:%M:%S`.tar c7962a4fee17
    - docker stop then remove all containers
        - `docker stop $(docker ps -aq)`
    - run container from dockerfile
    ```shell
    docker build -t xxx .
    docker run -d xxx
    ```
    - `docker ps` vs `docker ps -a`

    - docker --detach
    - delete a container file from outside of container.
    - docker exec -it -u 0 osstpmgt_websvc_1 bash  以root用户进入container
    - docker如何实现重新打tag并删除原tag的镜像?  https://blog.csdn.net/Dontla/article/details/122868804
    - 如果pg_restore一个db.dump到docker container中，如果这个container stop了，这个数据库的内容是否也消失了?
    - `Sending build context to Docker daemon  26.44GB`
        - 考虑当前目录下是否有大文件

    - 实现docker run mycmd, 然后mycmd可以在host上执行，这样的dockerfile怎么写？
    - /var/lib/docker/containers
    - container的log保存在container内部的什么位置?是否保存在container的内部？

    - 在阿里云中看到有`容器运行时`--containerd 1.5.13 与 安全沙箱2.2.2的字样，什么意思？
        - https://cs.console.aliyun.com/?spm=a2c6h.12873639.article-detail.4.6ade4960sj8Igz#/k8s/cluster/createV2/managed?template=pro-standard

#### Dockerfile
    - USER
    - ARG
    - ENTRYPOINT
    - COPY --chown
    - RUN & CMD & ENTRYPOINT
        - CMD命令是当Docker镜像被启动后Docker容器将会默认执行的命令。一个Dockerfile仅仅最后一个CMD起作用
    - `$PATH`
    - `ENV PYTHONIOENCODING UTF-8`

```yaml
Here is an example from skaffold examples:
My questions:
- Why 2 `FROM` ?
- COPY --from
- Can you explain each line ?
references: https://blog.csdn.net/a772304419/article/details/126644409

---------------
FROM golang:1.18 as builder
WORKDIR /code
COPY main.go .
COPY go.mod .
# `skaffold debug` sets SKAFFOLD_GO_GCFLAGS to disable compiler optimizations
ARG SKAFFOLD_GO_GCFLAGS
RUN go build -gcflags="${SKAFFOLD_GO_GCFLAGS}" -trimpath -o /app main.go

FROM alpine:3
# Define GOTRACEBACK to mark this container as using the Go language runtime
# for `skaffold debug` (https://skaffold.dev/docs/workflows/debug/).
ENV GOTRACEBACK=single
CMD ["./app"]
COPY --from=builder /app .
```

```shell
$ systemctl restart docker
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===
Authentication is required to restart 'docker.service'.
Authenticating as: vz
Password: 
==== AUTHENTICATION COMPLETE ===
Job for docker.service failed because the control process exited with error code.
See "systemctl status docker.service" and "journalctl -xe" for details.
-----
solution:
https://ithelp.ithome.com.tw/m/articles/10294103
https://blog.51cto.com/u_15162069/2743910
```

- systemd

- Docker-compose
- kubectl
  - kubectl create & kubectl apply
  - Services
    - ClusterIp (Default)
    - NodePort
    - 
  - restart: unless-stopped
  - kubectl diff

- Dockerfile
  - VOLUME
    - When do we need VOLUME 
    - 3 docker volume types
  - COPY --from=builder /opt/static static

- Docker stop all containers
    - stop all containers: `docker stop $(docker ps -aq)`
    - remove all containers: `docker rm $(docker ps -aq)`
    - delete all images `docker rmi $(docker images -q)`
- Why during my usage of docker, the docker disk usage is bigger and bigger ?
- docker network
- docker-compose `ports`, left or right is container port ?
- Host-port:Container-port

- Which command both in docker and docker-compose, is there any difference in usage in docker and docker-compose ?
- docker save & docker export

- save docker running container and push to dockerhub
```shell
docker commit 0a887a75b48b centos5.8-pkgs-and-tools-preinstalled:v1
docker tag centos5.8-pkgs-and-tools-preinstalled:v1 zhongpengqun/centos5.8-pkgs-and-tools-preinstalled:v1
docker push zhongpengqun/centos5.8-pkgs-and-tools-preinstalled:v1
```

### docker-compose
- Why `links` ? Is it has any association with `depends_on` ?

- `docker-compose build` 的作用是什么？
    - 由 dockerfile 构建一个docker image ？

`depends_on` determines the order of create containers.

An example
```yaml
version: '3.6'     # version of format of this yaml file, it can be 1, 2.x, 3.x, it's matter of the compatible with docker
services:
    nginx:
        build:
            context: fish        
            dockerfile: Dockerfile.nginx    # dockerfile is located at fish/Dockerfile.nginx
        restart: always     # it's equal to `docker run --restart always`, it is one kind of `restart policies`, 
                            # docker daemon will always try to restart the container infinitely until container starts successfully.
        links:          
            - gunicorn    # By links, gunicorn:80 will works, same as 10.0.0.4:80
        volumes:
            - nfs-storage:/build/toolchain    # `nfs-storage` is defined in below high level `volumes` block.
            - "./runtime/fish_nginx.conf:/etc/nginx/sites-available/fish.conf:ro"     # mount local file into container
        ports:
            - "80:80"   # host-port: container-port

    gunicorn:
        image: "fish_django_backend"    # my guess: 
        build:
            context: fish
            dockerfile: Dockerfile.django
        command: ["./bin/gunicorn_entrypoint.sh"]
        restart: always
        links:
            - db
            - couchdb
            - rabbitmq
        volumes:
            - nfs-storage:/build/toolchain
        expose:
            - "8000"
        ports:
            - "8001:8000"
        secrets:
            - host_ssh_key    # `host_ssh_key` is declared below, in high level block `secrets`

    coder_manager:
        image: "fish_django_backend"
        build:
            context: buildaudit
            dockerfile: Dockerfile.django
        command: ["./manage.py", "service_appcheck_manager"]
        restart: always
        links:
            - db
            - rabbitmq
        volumes:
            - "./runtime/buildaudit.yaml:/opt/buildaudit.yaml"

    coder:
        build:
            context: coder
            # here no `dockerfile` argument, so it will run the default `Dockerfile` file, i guess..
        links:
            - rabbitmq
        restart: always

    rabbitmq:
        build:
            context: ./rabbitmq
        expose:
            - "5672"
            - "15672"
        ports:
            - "15673:15672"
            - "5673:5672"
        environment:
            - RABBITMQ_DEFAULT_USER=admin
            - RABBITMQ_DEFAULT_PASS=123456

    db:
        image: postgres:11.9
        expose:
            - "5432"
        ports:
            - "5433:5432"
        environment:
            - POSTGRES_USER=root
            - POSTGRES_PASSWORD=123456
        command: "-c config_file=/etc/postgresql/postgresql.conf"
        volumes:
            - "./runtime/fish-postgres.conf:/etc/postgresql/postgresql.conf"

    couchdb:
        build:
            context: couchdb
            dockerfile: Dockerfile
        restart: always
        environment:
            - COUCHDB_USER=123456
            - COUCHDB_PASSWORD=123456
        expose:
            - "5984"
        ports:
            - "5984:5984"
        volumes:
            - "./db/couchdb_data:/opt/couchdb/data"

volumes:      # Declare all volumes in this list, it's convenient to be referred by many places
    nfs-storage:
        driver: local
        driver_opts:
            type: nfs
            o: "addr=storage.micro-hard.com,ro,nolock"
            device: ":/storage1"

secrets:
    host_ssh_key:
        file: ~/.ssh/id_rsa
```

# docker-compose up -d
[+] Running 0/0
 ⠿ Network concourse_default  Error                                                                                                                                        0.0s
failed to create network concourse_default: Error response from daemon: Failed to Setup IP tables: Unable to enable SKIP DNAT rule:  (iptables failed: iptables --wait -t nat -I DOCKER -i br-7b98d6e4dcfd -j RETURN: iptables: No chain/target/match by that name.
 (exit status 1))

[resolved]
# systemctl restart docker.service
# docker-compose up -d
```

```shell
docker-compose up --detach --build gunicorn
docker-compose up --build gunicorn
```

- How to Rebuild and restart container ?
- How do I run a docker instance from a DockerFile?


install docker on ubuntu
```shell
apt-get install docker.io
```

linux install docker-compose

```shell
https://github.com/docker/compose/releases/tag/v2.10.2
https://github.com/docker/compose/releases/download/v2.10.2/docker-compose-linux-x86_64
```



```shell
$ docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: zhongpengqun
Password: 
** Message: 16:34:45.997: Remote error from secret service: org.freedesktop.DBus.Error.ServiceUnknown: The name org.freedesktop.secrets was not provided by any .service files
Error saving credentials: error storing credentials - err: exit status 1, out: `The name org.freedesktop.secrets was not provided by any .service files`


s:
sudo apt install gnupg2 pass

```


- docker pull from private registry ?
    - how to deploy a private registry ?
        - https://www.youtube.com/watch?v=O_NMIZJ1qvw
        ```
        docker run -d -p 5000:5000 --restart=always --name registry -v $(pwd)/docker-registry:/var/lib/registry registry:latest
        ```
