FROM python:2.7
COPY . /
WORKDIR /
RUN pip install mkdocs
EXPOSE 8080
CMD ["mkdocs", "serve"]
