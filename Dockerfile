FROM python:3.7-slim

WORKDIR /app

# both files are explicitly required!
COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
  apt-get update && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
  pipenv install --deploy --system && \
  apt-get remove -y gcc python3-dev libssl-dev && \
  apt-get autoremove -y && \
  pip uninstall pipenv -y

COPY . ./
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
