FROM python:slim AS builder
RUN apt update && apt install gcc curl -y
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y && apt install --reinstall libc6-dev -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN pip install --no-cache tiktoken

FROM python:alpine
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
WORKDIR /wx-chatbot
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]
