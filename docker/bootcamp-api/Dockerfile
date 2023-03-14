FROM python:3.8

WORKDIR /var/api

ENV WORKDIR /var/api

COPY . .

RUN apt-get -y update
RUN python -m pip install --upgrade pip
RUN python -m pip install uvicorn

RUN pip install -r ./requirements.txt

CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]
