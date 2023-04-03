# /bin/sh

# Docker run it, it is the best! refer to https://medium.com/@edsonalcalamx/running-nethereum-docs-with-docker-5b8a4c25d42f
docker build -t blog .
docker run -d blog

#mkdocs serve -a 0.0.0.0:7777

