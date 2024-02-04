FROM python:3.11-bookworm
## Don't really need virtual envs but keeping in as it matches what I dev'd

RUN apt update && \
    apt install -y curl && \
    rm -rf /var/lib/apt/lists/*

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1

RUN pip install poetry==1.7.1

WORKDIR /app

### Install usql
RUN curl -LJO https://github.com/xo/usql/releases/download/v0.17.5/usql-0.17.5-linux-amd64.tar.bz2 && \
    tar -C /usr/local/bin/ -xjf usql-0.17.5-linux-amd64.tar.bz2 && \
    rm usql-0.17.5-linux-amd64.tar.bz2
###

COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY elt_script ./elt_script

CMD ["poetry", "run", "-vvv", "python", "./elt_script/main.py"]