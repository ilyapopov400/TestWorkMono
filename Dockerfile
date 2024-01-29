FROM python:3.10
# установили среду

SHELL ["/bin/bash", "-c"]

# set environment variabels
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apt update
# обновили зависимости

RUN mkdir /app
# создали в контейнере папку app

COPY .. /app/
# скопировали с компьютере все из текущей папк в папку app в контейнере

WORKDIR /app
# установили рабочий каталог приложения в контейнере

RUN pip install -r requirements.txt
# установили зависимости из файла

EXPOSE 8080
# установили порт

CMD ["python3", "Mono/manage.py", "runserver", "0.0.0.0:8080"]