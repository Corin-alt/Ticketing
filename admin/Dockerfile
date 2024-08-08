FROM python:3.12.1-alpine

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./admin/admin.py /app/

CMD [ "flask", "--app", "admin", "run","--host", "0.0.0.0"] 