FROM ubuntu

RUN sed -i.bal 's/main$/main universe/' /etc/apt/sources.list
RUN apt-get update

ADD http://archive.scrapy.org/ubuntu/archive.key /tmp/scrapy.key
RUN apt-key add /tmp/scrapy.key
RUN echo "deb http://archive.scrapy.org/ubuntu precise main" > /etc/apt/sources.list.d/scrapy.list
RUN apt-get update

RUN apt-get install -y scrapy-0.23
