import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime


from Runners.Executors.dataexecutor import Swdmain_settings
from Runners.Executors.console import Swdconsole_logs, returns
from Runners.Executors.colormanager import Swdcolor_picker

ss = Swdmain_settings()
con_logs = Swdconsole_logs()
sp = Swdcolor_picker()


class SWDOwneronly(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "swd_owneronly", current)

    @app_commands.command(name='update_account', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def update_account(self, interaction: discord.Interaction, username: str, type: str):
        if self.swd.is_owner(interaction.user):
            await interaction.response.defer()
            for member in self.swd.get_all_members():
                if member.name == username:
                    user = member
                    break

            if type != "remove":
                result = ss.payment(type, user.id)
                own_emb = discord.Embed(title='[Subscription granted!]', colour=sp.get_color("warning"))
                own_emb.add_field(name=f'▶Info:',
                                  value=f'➾ **-** Username: {username}\n➾ **-** Expiration date: {result}',
                                  inline=False)
            else:
                ss.payment(type, user.id)
                own_emb = discord.Embed(title='[Subscription removed!]', colour=sp.get_color("warning"))
                own_emb.add_field(name=f'▶Info:',
                                  value=f'➾ **-** Username: {username}\n➾ **-** Expiration date: today',
                                  inline=False)
            await interaction.response.send_message(embed=own_emb)


async def setup(swd):
    await swd.add_cog(SWDOwneronly(swd))