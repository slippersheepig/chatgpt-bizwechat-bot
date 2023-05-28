FROM python:alpine
RUN apk add --no-cache --virtual .build-deps libffi-dev
WORKDIR /wx-chatbot
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]
