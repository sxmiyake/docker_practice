FROM ubuntu:18.04

RUN apt update
RUN apt upgrade
RUN apt install python3-pip
RUN pip3 install flask

ENV HOME=/root

WORKDIR $HOME