FROM python:alpine
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev
WORKDIR /wx-chatbot
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apk del .build-deps
CMD [ "python", "main.py" ]
