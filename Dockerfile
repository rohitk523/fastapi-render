FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# Get the PORT environment variable
ENV PORT=8080

# Use the $PORT variable in the CMD
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]