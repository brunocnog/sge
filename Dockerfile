FROM python:3.11-slim

WORKDIR /sge

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apt update && apt -y install cron && apt -y install nano
RUN apt update && apt -y install cron && apt -y install nano && apt -y install procps

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./cron /etc/cron.d/cron
RUN chmod 0644 /etc/cron.d/cron
RUN touch /var/log/cron.log && chmod 0666 /var/log/cron.log

# RUN crontab /etc/cron.d/cron

# RUN python manage.py migrate

EXPOSE 8000

# CMD cron ; python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD service cron start && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
CMD cron -f & python manage.py migrate && python manage.py runserver 0.0.0.0:8000
