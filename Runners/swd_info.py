import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime


from Runners.Executors.console import Swdconsole_logs
from Runners.Executors.colormanager import Swdcolor_picker
from Runners.Executors.paginator import Pagination
from Runners.Executors.extra.info_extra import help_pages

con_logs = Swdconsole_logs()
sp = Swdcolor_picker()


class SWDInfo(commands.Cog):
    def __init__(self, swd):
        self.swd = swd

        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "swd_info", current)

    @app_commands.command(name='help', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def help(self, interaction: discord.Interaction):
        paginator = Pagination(interaction, help_pages.first_page, help_pages.second_page)
        await paginator.paginator_start()


async def setup(swd):
    await swd.add_cog(SWDInfo(swd))