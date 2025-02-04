import logging
from datetime import datetime
from revChatGPT.V1 import Chatbot


class ChatBotWithExpiration:
    """
    ChatGPTBot with recording last access time
    """
    def __init__(self, config) -> None:
        self.bot = Chatbot(config)
        self.last_access_time = datetime.now().timestamp()
        self.err_msg = "[Chat-Bot] 请求 ChatGPT 失败, 请重试"

    def _update_last_access_time(self):
        self.last_access_time = datetime.now().timestamp()

    def reset(self):
        """
        reset conversation session
        """
        self.bot.reset_chat()
        self._update_last_access_time()
        return "[ChatBot] ChatGPT 会话已重置, 发送消息开始聊天"

    def get_response(self, text):
        """
        request chatgpt and get response
        """
        logging.info("[Chat-Bot] requesting ChatGPT: %s", text)
        try:
            prev_text = ""
            for data in self.bot.ask(text):
                prev_text = prev_text + data["message"][len(prev_text) :]
            response = prev_text
        except Exception as e:
            logging.error("[Chat-Bot] Request ChatGPT failed. %s", e)
            response = self.err_msg
        self._update_last_access_time()
        return response
