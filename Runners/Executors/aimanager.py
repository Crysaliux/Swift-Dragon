from groq import Groq
from console import Swdconsole_logs
import os

con_logs = Swdconsole_logs()


groq_api_key = open("Runners/Executors/ts_data/groc.txt", "r").readline()
client = Groq(api_key=groq_api_key)


class swift_ai:
    model = 'llama3-8b-8192'

class swift_protect:
    model = 'llama3-8b-8192'
    prompt = open("Runners/Executors/prompts/security.txt", "r").readline()


class Swdai_access:
    def __init__(self):
        con_logs.call("Aimanager")

    def check_content(self, content):
        messages = [
            {
                "role": "system", "content": swift_protect.prompt
            },
            {
                "role": "user", "content": content
            }
        ]

        chat_completion = client.chat.completions.create(
            messages=messages,
            model=swift_protect.model,
            temperature=1,
            max_tokens=10,
            top_p=1,
            stop=None,
            stream=False
        )

        reply = chat_completion.choices[0].message.content.lower()
        if reply == "yes":
            return reply