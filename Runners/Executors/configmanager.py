import discord
import json
from groq import Groq
import os

from Runners.Executors.console import Swdconsole_logs

con_logs = Swdconsole_logs()


class Config:
    def __init__(self):
        con_logs.call("Colormanager")

    def swift_config(self):
        try:
            intents = discord.Intents.default()
            conf = open("Runners/Executors/ts_data/swift_config.json")
            data = json.load(conf)
            if data["intents_messages"] == "True":
                intents.messages = True
            if data["intents_members"] == "True":
                intents.members = True
            if data["intents_message_content"] == "True":
                intents.message_content = True

            return {"token": data["token"], "cogs": data["cogs"], "owner_id": data["owner_id"],
                    "database": data["database"], "bing_auth_cookie": data["bing_auth_cookie"],
                    "auth_cookie_SRCHHPGUSR": data["auth_cookie_SRCHHPGUSR"], "intents": intents}
        except:
            con_logs.error('400')
            return 'error'

    def groq_config(self):
        try:
            conf = open('Runners/Executors/ts_data/groq_config.json')
            data = json.load(conf)
            client = Groq(api_key=data["token"])

            return {"client": client, "model": data["model"], "temperature": data["temperature"], "max_tokens": data["max_tokens"]}
        except:
            con_logs.error('400')
            return 'error'

    def prompts(self, type: str):
        try:
            conf = open('Runners/Executors/prompts/sys_prms.json')
            data = json.load(conf)
            if type == "security":
                return data["security"]
            else:
                con_logs.error('400')
                return 'error'
        except:
            con_logs.error('400')
            return 'error'