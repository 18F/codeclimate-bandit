FROM python:3-alpine

VOLUME /code
WORKDIR /code

RUN pip3 install bandit

COPY config.json /config.json

ENTRYPOINT ["bandit"]
CMD ["-r", "/code", "-f", "csv"]
