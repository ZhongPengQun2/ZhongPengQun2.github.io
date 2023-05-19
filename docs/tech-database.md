### PostgreSQL

```
docker run -it --name postgres --restart always -e POSTGRES_PASSWORD='abc123' -e ALLOW_IP_RANGE=0.0.0.0/0 -v /home/postgres/data:/var/lib/postgresql -p 55433:5432 -d osstp-docker-local.artifactory.eng.vmware.com/mirrors/dockerhub/postgres:9.6
```



## SQL
- select mt where 
    - Join