from discord.ext import commands
from datetime import datetime
import sys
sys.path.append("Runners/Executors")
from dataexecutor import Swdmain_settings
from console import Swdconsole_logs
from urllib.request import Request, urlopen

ss = Swdmain_settings()
con_logs = Swdconsole_logs()

class SWDGchat(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "swd_gchat", current)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            pass
        else:
            gchat = ss.swd_pull(message.guild.id, 'gchat')
            guild = message.guild
            if not guild:
                pass
            else:
                channel_id = gchat.get("channel_id")
                if channel_id == "none":
                    pass
                elif gchat.get("status") == "off":
                    pass
                else:
                    if message.channel.id != channel_id:
                        pass
                    else:
                        req = Request(
                            url=message.author.avatar.url,
                            headers={'User-Agent': 'Mozilla/5.0'}
                        )
                        with urlopen(req) as url:
                            result = url.read()
                        await ss.gchat_purge(message.guild.id, self.swd, message.author.name, result, message)


def setup(swd):
    swd.add_cog(SWDGchat(swd))