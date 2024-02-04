FROM python:3.11-buster
## Don't really need virtual envs but keeping in as it matches what I dev'd

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1

RUN pip install poetry==1.7.1

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY elt_script ./elt_script

CMD ["poetry", "run", "-vvv", "python", "./elt_script/main.py"]