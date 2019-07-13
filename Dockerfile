FROM python:3.6-alpine

RUN pip install pipenv

RUN apk --no-cache add \
        bash \
        nodejs \
        nodejs-npm

WORKDIR /usr/src/app
COPY blog-generator ./blog-generator
COPY putisplain ./putisplain
COPY webapp ./webapp
COPY crawler ./crawler

WORKDIR /usr/src/app/crawler
RUN npm install
RUN node --version
RUN node index.js 2>/dev/null

WORKDIR /usr/src/app/webapp
RUN pipenv install

CMD [ "/usr/src/app/webapp/start-server.sh" ]
