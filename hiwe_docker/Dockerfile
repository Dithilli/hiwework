FROM python:3.6.5-slim
RUN pip3 install --upgrade pip 
RUN pip3 install bottle
WORKDIR /hiwe_docker
ADD . /hiwe_docker
EXPOSE 8080
CMD ["python3", "hiwe.py"]
