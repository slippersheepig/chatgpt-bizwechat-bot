FROM python:alpine
RUN apk add --no-cache build-base curl‑dev libffi-dev
WORKDIR /wx-chatbot
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apk del build-base
CMD [ "python", "main.py" ]
