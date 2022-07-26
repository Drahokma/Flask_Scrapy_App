FROM python:3.6

LABEL maintainer "MD"
# includes setuptools and wheel

ENV PATH="/usr/local/mysql/bin:${PATH}"

# scrapy and selenium
RUN BUILD_DEPS='autoconf \
                build-essential \
                git \
                libssl-dev' && \
    RUN_DEPS='default-libmysqlclient-dev \
              ca-certificates \
              ssl-cert' && \
    apt-get update && \
    apt-get install -yqq $RUN_DEPS $BUILD_DEPS --no-install-recommends && \
    apt-get purge -y --auto-remove $BUILD_DEPS && \
    rm -rf /var/lib/apt/lists/*

# chrome
RUN BUILD_DEPS='gnupg unzip' && \
    RUN_DEPS='wget' && \
    apt-get update && \
    apt-get install -yqq $RUN_DEPS $BUILD_DEPS --no-install-recommends && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list && \
    wget https://dl-ssl.google.com/linux/linux_signing_key.pub && \
    apt-key add linux_signing_key.pub && \
    apt-get update && \
    apt-get install -yqq google-chrome-stable --no-install-recommends && \
    rm -rf linux_signing_key.pub && \
    apt-get purge -y --auto-remove $BUILD_DEPS && \
    rm -rf /var/lib/apt/lists/*

# chromedriver
RUN BUILD_DEPS='unzip' && \
    RUN_DEPS='wget' && \
    apt-get update && \
    apt-get install -yqq $RUN_DEPS $BUILD_DEPS --no-install-recommends && \
    wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    chmod 755 chromedriver && \
    mv chromedriver /usr/local/bin/chromedriver && \
    rm -rf chromedriver_linux64.zip && \
    apt-get purge -y --auto-remove $BUILD_DEPS && \
    rm -rf /var/lib/apt/lists/*

ENV DISPLAY :20.0
ENV SCREEN_GEOMETRY "1440x900x24"
ENV CHROMEDRIVER_PORT 4444
ENV CHROMEDRIVER_WHITELISTED_IPS "127.0.0.1"
ENV CHROMEDRIVER_URL_BASE ''

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

COPY . /app

ENV FLASK_ENV="docker"

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

