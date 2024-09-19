FROM python:3.10-alpine
# Install psycopg requirements
RUN apk update && apk add postgresql-dev build-base


RUN pip install --upgrade pip
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY src src

# (informative) port the container should expose
EXPOSE 5000
ENV FLASK_APP=/src/app:create_app
# TODO: run with WSGI server, this is dev server
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
