FROM python:3.10
ENV UV_COMPILE_BYTECODE=1

ENV PROJECT_NAME=HOLA
ENV POSTGRES_SERVER=123
ENV POSTGRES_USER=123
ENV FIRST_SUPERUSER=123
ENV FIRST_SUPERUSER_PASSWORD=1232
ENV UV_LINK_MODE=copy

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


