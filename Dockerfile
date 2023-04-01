FROM python:3.10 as builder
RUN mkdir /app 
COPY pyproject.toml /app 
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root
RUN yes | pip3 uninstall poetry
COPY . /app
EXPOSE 8080
ENTRYPOINT ["/app/docker-entrypoint.sh"]
