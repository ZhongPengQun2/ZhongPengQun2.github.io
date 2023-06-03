FROM python:3.10
COPY . /
WORKDIR /
RUN pip3 install -r requirements.txt
#EXPOSE 7777
#CMD [ "mkdocs", "serve"， "-a",  "0.0.0.0:7777" ]
EXPOSE 8080
CMD [ "mkdocs", "serve" ]