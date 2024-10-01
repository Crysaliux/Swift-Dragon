from Runners.Executors.console import Swdconsole_logs
from Runners.Executors.configmanager import Config

con_logs = Swdconsole_logs()
conf = Config()


class Swdai_security:
    def __init__(self):
        con_logs.call("Securitymanager")
        self.client = conf.groq_config()["client"]
        self.model = conf.groq_config()["model"]

    def check_content(self, content):
        messages = [
            {
                "role": "system", "content": conf.prompts("security")
            },
            {
                "role": "user", "content": content
            }
        ]

        chat_completion = self.client.chat.completions.create(
            messages=messages,
            model=self.model,
            temperature=1,
            max_tokens=10,
            top_p=1,
            stop=None,
            stream=False
        )

        reply = chat_completion.choices[0].message.content.lower()
        if reply == "yes":
            return reply