FROM spark:4.0.1-scala2.13-java17-ubuntu
USER root
RUN apt-get update && apt-get install -y python3-venv
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN apt-get install -y python3 python3-pip
RUN apt-get update && apt-get install -y \
    wget \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libgbm1 \
    libglib2.0-0 \
    libgtk-3-0 \
    libpango-1.0-0 \
    libvulkan1 \
    libx11-6 \
    libxcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    libnss3 \
    libnspr4 \
    --no-install-recommends
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN wget https://github.com/allure-framework/allure2/releases/download/2.35.1/allure-2.35.1.tgz && \
    tar -zxvf allure-2.35.1.tgz -C /opt/ && \
    ln -s /opt/allure-2.35.1/bin/allure /usr/bin/allure && \
    rm allure-2.35.1.tgz
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
USER spark