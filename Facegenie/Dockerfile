    
#pull official base image
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install cmake
RUN apt-get update && apt-get -y install cmake
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get update && apt-get install -y python3-opencv
RUN mkdir /code

WORKDIR /code
COPY  requirements.txt /code/
RUN pip install --upgrade -I setuptools
#RUN pip install -r requirement.txt
RUN pip3 install -r requirements.txt
COPY . /code/
#RUN python manage.py makemigrations
#Run python manage.py migrate


EXPOSE 50001


 
