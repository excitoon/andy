FROM library/python:3.10.13-bullseye

RUN curl -sSL https://install.python-poetry.org | python3 - --version 2.1.1
ENV PATH=/root/.local/bin:$PATH

WORKDIR /app

COPY pyproject.toml poetry.lock* .

RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

ENTRYPOINT ["python3", "test.py"]
