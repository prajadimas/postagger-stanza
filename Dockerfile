FROM python:3.8-alpine

WORKDIR /myapp

COPY Pipfile* ./

RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear

COPY . .
EXPOSE 5000
CMD ["flask", "run"]
