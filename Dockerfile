FROM python:3.7

ENV FLASK_APP=app:create_app

COPY requirements.txt ./
RUN pip install --requirement requirements.txt

COPY . .

CMD gunicorn --bind "0.0.0.0:${PORT:-5000}" 'app:create_app()'

EXPOSE 5000
