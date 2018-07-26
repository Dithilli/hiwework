FROM python:3.6.5-slim
WORKDIR /hiwe_docker
ADD . /hiwe_docker
RUN pip3 install --upgrade pip 
RUN pip3 install bottle
EXPOSE 8080
CMD ["python3", "hiwe.py"]

