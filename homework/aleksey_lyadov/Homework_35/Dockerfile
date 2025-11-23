FROM jenkins/jenkins:lts-jdk17
USER root
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
USER jenkins