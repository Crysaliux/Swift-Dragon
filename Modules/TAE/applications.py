import discord
import json
from discord.ext import commands
from discord import app_commands
from datetime import datetime


from Runners.Executors.configmanager import Config
from Runners.Executors.console import Swdconsole_logs
from Runners.Executors.colormanager import Swdcolor_picker


con_logs = Swdconsole_logs()
sp = Swdcolor_picker()
conf = Config()


class Applications(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        self.app_forum = swd.get_channel(1220044279154479225)
        self.client = conf.groq_config()["client"]
        self.model = conf.groq_config()["model"]
        self.prompt = json.load(open("Modules/TAE/modconf.json"))["prompt"]

        self.artist_role = 1220044514085834853
        self.writer_role = 1220044595233034250
        self.gamedev_role = 1220044558927138878
        self.roleplayer_role= 1283364034716106753


        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "TAE/applications", current)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id == 1172162501979406408:
            if message.channel in self.app_forum.threads:
                messages = [
                    {"role": "system", "content": self.prompt},
                    {"role": "user", "content": message.content}
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
                if reply == 'artist':
                    role = discord.utils.get(message.guild.roles, id=self.artist_role)
                    await message.author.add_roles(role)
                    await message.reply("**Your application has been accepted, yippie! :3\nYou got verified artist role!**\n_Rangers, with love :3_")
                elif reply == 'writer':
                    role = discord.utils.get(message.guild.roles, id=self.writer_role)
                    await message.author.add_roles(role)
                    await message.reply("**Your application has been accepted, yippie! :3\nYou got verified artist role!**\n_Rangers, with love :3_")
                elif reply == 'gamedev':
                    role = discord.utils.get(message.guild.roles, id=self.gamedev_role)
                    await message.author.add_roles(role)
                    await message.reply("**Your application has been accepted, yippie! :3\nYou got verified artist role!**\n_Rangers, with love :3_")
                elif reply == 'roleplayer':
                    role = discord.utils.get(message.guild.roles, id=self.roleplayer_role)
                    await message.author.add_roles(role)
                    await message.reply("**Your application has been accepted, yippie! :3\nYou got verified artist role!**\n_Rangers, with love :3_")
                elif reply == 'denied':
                    await message.reply("**Your application has been denied! :c\nCheck if you provide enough examples!\nIf you think this is an error contact us via ModMail :0**\n_Rangers, with love :3_")


async def setup(swd):
    await swd.add_cog(Applications(swd))