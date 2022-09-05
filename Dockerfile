FROM python:3.8-slim-buster

ADD ./ /home/test
RUN chmod +x /home/test/action-a/entrypoint.sh
ENTRYPOINT ["/home/test/action-a/entrypoint.sh"]
