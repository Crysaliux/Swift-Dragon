import discord
from discord.ext import commands
from datetime import datetime


from Runners.Executors.dataexecutor import Swdmain_settings
from Runners.Executors.console import Swdconsole_logs
from Runners.Executors.colormanager import Swdcolor_picker

ss = Swdmain_settings()
con_logs = Swdconsole_logs()
sp = Swdcolor_picker()


class SWDGreeting(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "swd_greeting", current)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        greetings = ss.swd_pull(member.guild.id, 'greetings')
        check = greetings.get("channel_id")
        if check == "none":
            pass
        else:
            if greetings.get("status") == "off":
                pass
            else:
                channel = self.swd.get_channel(check)
                await channel.send(greetings.get("message").replace('<member>', f'{member.mention}'))


async def setup(swd):
    await swd.add_cog(SWDGreeting(swd))