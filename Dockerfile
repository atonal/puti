FROM python:3.6

RUN pip install pipenv

RUN apt-get update && apt-get install -y \
        curl \
        && rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -

RUN apt-get update && apt-get install -y \
        nodejs \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY blog-generator ./blog-generator
COPY webapp ./webapp
COPY crawler ./crawler

WORKDIR /usr/src/app/crawler
RUN npm install
RUN node --version
RUN node index.js 2>/dev/null

WORKDIR /usr/src/app/webapp
RUN pipenv install

CMD [ "/usr/src/app/webapp/start-server.sh" ]
