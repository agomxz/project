# Base
FROM python:3.11

ENV DB_HOST=aws-0-us-west-1.pooler.supabase.com
ENV DB_NAME=postgres
ENV DB_USER=postgres.vzvrmhhqiwyntaftiveh
ENV DB_PASS=Hello02630.by3
ENV DB_PORT=6543

# Set working diretory
WORKDIR /code

# copy requirements.txt and install
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy FastAPI application
COPY ./app /code/app

# Set command to run the application
CMD ["uvicorn", "app.main:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8000"]