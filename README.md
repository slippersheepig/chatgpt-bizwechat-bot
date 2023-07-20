# ChatGPT BizWechat Bot
A BizWechat Bot that integrates with OpenAI's [ChatGPT](https://openai.com/blog/chatgpt/) to provide answers. Ready to use with minimal configuration required. Based on [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) 

基于 [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT) 开发的企业微信聊天机器人

## Attension
服务器的IP不能被BAN，我没有IP测试项目是否可用，请自行尝试

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
- Access Token（ 有效期约半个月，登录ChatGPT官方网页版后再打开https://chat.openai.com/api/auth/session ）

## Getting started

### Install with Docker Compose
```bash
services:
  chatgpt:
    image: sheepgreen/chatgpt-wework
#   environment:
#     - CHATGPT_BASE_URL=ChatGPT代理地址，不填默认使用作者的地址，可能存在请求频率等限制
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
