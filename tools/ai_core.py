import time

import requests

from tools.config_util import ConfigUtil


class AICore:
    def __init__(self):
        self.endpoint = ConfigUtil.get_ai_endpoint()
        self.api_key = ConfigUtil.get_ai_api_key()

    def ask_ai(self, messages):
        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key
        }
        payload = {
            "messages": messages,
            "temperature": 0.5,
            "top_p": 0.95,
            "max_tokens": 800
        }

        try:
            response = requests.post(self.endpoint, headers=headers, json=payload)
            response.raise_for_status()
        except requests.RequestException as e:
            raise SystemExit(f"Failed to make the request. Error: {e}")
        return response.json()['choices'][0]['message']['content']
