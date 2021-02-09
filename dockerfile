FROM python:3.6-slim
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get install git -y \
&& apt-get install make -y \
&& apt-get clean

COPY ./requirements.txt .

ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY . .
