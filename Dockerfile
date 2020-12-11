############Dockerfile###########
FROM openjdk:8

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y git 
RUN apt-get install -y curl
RUN apt-get install -y vim
RUN apt-get install -y tar

RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip

###
RUN pip3 install chatterbot==1.1.0

RUN python3 -m spacy download en

RUN git clone https://github.com/gaoyuanliang/chatterbot-corpus.git
RUN mv chatterbot-corpus/chatterbot_corpus/data/english/*.yml ./

RUN git clone https://github.com/gaoyuanliang/flask-chatterbot.git
RUN mv flask-chatterbot/* ./
RUN pip3 install -r requirements.txt
EXPOSE 5000

RUN cat *.yml > corpus.yml

RUN echo "dsgdsnkg"

RUN git clone https://github.com/gaoyuanliang/jessica_chatbot.git
RUN mv jessica_chatbot/* ./

############Dockerfile###########
