FROM python:3.11.5
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]

# docker build -t rest-flask-python .
# docker run -p 5005:5000 -w /app -v $PWD/:/app rest-api-flask-python