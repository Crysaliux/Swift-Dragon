#This file is used for testing purposes only!

import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import threading
import asyncio


from Runners.Executors.console import Swdconsole_logs, returns
from Runners.Executors.colormanager import Swdcolor_picker


con_logs = Swdconsole_logs()
sp = Swdcolor_picker()


class Testing(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "tester", current)


async def setup(swd):
    await swd.add_cog(Testing(swd))