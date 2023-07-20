FROM python:slim

WORKDIR /wx-chatbot
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]
