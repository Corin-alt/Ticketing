FROM python:3.12.1-alpine

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./shop/shop.py /app/

CMD [ "flask", "--app", "shop", "run","--host", "0.0.0.0"] 