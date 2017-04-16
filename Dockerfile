FROM python:3-alpine

VOLUME /code
WORKDIR /code

RUN pip3 install bandit

ENTRYPOINT ["bandit"]
CMD ["-r", "/code"]
