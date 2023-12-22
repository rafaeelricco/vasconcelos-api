FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN /bin/sh -c pip install -r requirements.txt
RUN pip install -r requirements.txt
COPY . /code/