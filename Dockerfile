FROM python:latest

RUN apt-get update -qq \
    && apt-get install -y build-essential python3-dev \
    python3-pip python3-setuptools python3-wheel python3-cffi \
    libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# set env valriables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .
RUN python -m pip install -r requirements.txt
RUN python -m pip install psycopg[binary]

COPY . .