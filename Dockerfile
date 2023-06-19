FROM python:3.8.8-slim-buster

RUN mkdir -p /app
COPY . main.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]