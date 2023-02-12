FROM python:slim

RUN apt update && apt install chromium xvfb xauth -y

WORKDIR /wx-chatbot
ENV PATH="${PATH}:/usr/local/bin:/usr/bin:/bin"

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]
