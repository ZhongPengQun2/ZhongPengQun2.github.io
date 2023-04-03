FROM python:2.7
COPY . /
WORKDIR /
RUN pip install --default-timeout=100 mkdocs
#EXPOSE 7777
#CMD [ "mkdocs", "serve"， "-a",  "0.0.0.0:7777" ]
EXPOSE 8080
CMD [ "mkdocs", "serve" ]