FROM rust:slim AS builder
RUN apt update && apt install pip -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN pip install --no-cache --break-system-packages tiktoken

FROM python:alpine
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
WORKDIR /wx-chatbot
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]
