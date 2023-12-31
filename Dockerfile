FROM --platform=linux/amd64 public.ecr.aws/docker/library/python:3.9.17-slim-bullseye

RUN mkdir -p /app
COPY . main.py /app/
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]