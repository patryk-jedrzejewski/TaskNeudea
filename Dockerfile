FROM python:3.8.4-slim-buster
MAINTAINER Patryk

COPY search_dir.py search_dir.py
ENTRYPOINT ["python", "search_dir.py"]