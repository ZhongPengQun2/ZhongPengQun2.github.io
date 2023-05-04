#### docker-compose services


#### docker-compose network
- network_mode

- eth 0



- 如何让remote的机器上的端口能被访问，即设置为0.0.0.0这种，在remote上curl http://localhost:5000可以访问，但是curl 类似http://139.196.8.9:5000没用



```
↓ 为什么 PORTS 这列是空的 ？

CONTAINER ID   IMAGE                                                                                        COMMAND                  CREATED          STATUS                  PORTS                                                                                                                                NAMES
ace91934cb7b   internationaldjangoedition_flask                                                             "python app.py runse…"   30 seconds ago   Up 29 seconds                                                                                                                                                internationaldjangoedition_flask_1
c3a63f84aaa5   public.ecr.aws/y5z1i2v3/zhongpengqun:postgres9.6                                             "docker-entrypoint.s…"   31 seconds ago   Up 30 seconds           0.0.0.0:6432->5432/tcp, :::6432->5432/tcp                                                                                            postgresql
```