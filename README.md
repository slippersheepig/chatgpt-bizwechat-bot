# ChatGPT BizWechat Bot
A BizWechat Bot that integrates with OpenAI's [ChatGPT](https://openai.com/blog/chatgpt/) to provide answers. Ready to use with minimal configuration required. Based on [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) 

基于 [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) 开发的企业微信聊天机器人

## Screeeshots
<img src="https://user-images.githubusercontent.com/4464307/206640973-a9790f2f-2452-4edc-b82f-e37bfface7dd.png" width="250"/>

如希望体验该机器人，需加入“3DS电影”企业，请发送邮件到admin@sheepig.top申请（该邮箱不处理其他事务）

## Features
- [x] Reply to specific messages / 回复用户信息
- [x] Can reset conversation thread with the `/reset` command / 发送 `/reset` 来重置对话
- [x] Multi-chat support. Every user has their own chat session / 每个用户有自己独立的对话

## ToDo Features
- [ ] Destroy chatbot after setting expire time to save resources / 会话过期机制, 节省资源

## Prerequisites
- Python 3
- A BizWechat Coporation Account / 企业微信企业账号
- Knowledge of how to deploy a self host bot in bizwechat / 了解如何搭建企业微信机器人 (如何获取 `Token`, `EncodingAESKey`, `CorpID`, `SECRET`, `agent_id` 等参数)
- An [OpenAI](https://openai.com) account / [OpenAI](https://openai.com) 账号
- (optional but recommended) A ChatGPT proxy address, you can use [acheong08/ChatGPT-Proxy](https://github.com/acheong08/ChatGPT-Proxy) to host a bypass server yourself

## Getting started

### Install with Docker Compose
```bash
version: '3'
services:
  chatgpt:
    image: sheepgreen/chatgpt-wework
#   environment:
#     - CHATGPT_BASE_URL=上面说的ChatGPT代理地址，不填默认使用作者的地址，可能存在请求频率等限制
    volumes:
      - ./config.yaml:/wx-chatbot/config.yaml
    ports:
      - "8868:8868"
    restart: always
```

the bot url is `http(s)://host:port/chat`

### Install from source
1. Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/slippersheepig/chatgpt-bizwechat-bot.git
cd chatgpt-bizwechat-bot
```

2. Install dependencies
```
cd src && pip install -r requirements.txt
```

3. Configuration File
create `config.yaml` under `src` folder, it has two section, one for BizWechatBot, one for ChatGPT
```yaml
wx-bot:
  Token: 
  EncodingAESKey: 
  CorpID: 
  SECRET: 
  agent_id: 
chatgpt: 
  email: 直接填邮箱，无需引号包含
  password: 直接填密码，无需引号包含
```

4. Launch Application
```python
python main.py
```

5. Enjoy

the bot url is `http(s)://host:port/chat`

## Credits
- [ChatGPT](https://chat.openai.com/chat) from [OpenAI](https://openai.com)
- [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) for reverse engineering ChatGPT APIs

## Disclaimer
This is a personal project and is not affiliated with OpenAI in any way.

## Changlog
- 2023-02-12: Change back to use [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) 
- 2022-12-14: Change to use [pyChatGPT](https://github.com/terry3041/pyChatGPT)
