FROM python:3.8-alpine

WORKDIR /myapp

COPY Pipfile* ./

RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear

COPY . .
CMD ["python3.8", "-m", "flask", "run"]
