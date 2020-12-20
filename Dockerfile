FROM python:3.8-alpine

WORKDIR /myapp

COPY Pipfile* ./

RUN python3.8 -m pip install pip --upgrade && \
    python3.8 -m pip install --no-cache-dir pipenv && \
    pipenv install --python 3.8 && \
    pipenv install --system --deploy --clear

COPY . .
EXPOSE 5000
CMD ["pipenv", "run", "flask", "run"]
