# pull official base image
FROM python:3.7

# set work directory
RUN mkdir /code
WORKDIR /code


ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
