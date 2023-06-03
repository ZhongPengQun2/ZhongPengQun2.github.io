# /bin/sh

# todo, 有点问题，run不起来
# Docker run it, it is the best! refer to https://medium.com/@edsonalcalamx/running-nethereum-docs-with-docker-5b8a4c25d42f
# docker rmi -f blog
# ocker rm -f $(docker ps |grep mkdocs |awk '{ print $1 }')
# docker build -t blog .
# docker run -d blog

# pip install mkdocs

mkdocs serve -a 0.0.0.0:7777

