import discord
from discord.ext import commands
from datetime import datetime
import sys
sys.path.append("Runners/Executors")
from dataexecutor import Swdmain_settings
from console import Swdconsole_logs, returns
from colormanager import Swdcolor_picker

ss = Swdmain_settings()
con_logs = Swdconsole_logs()
sp = Swdcolor_picker()


class SWDOwneronly(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "swd_owneronly", current)

    @commands.slash_command(name='update_account', description='-')
    @commands.is_owner()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def update_account(self, ctx, username: str, type: str):
        await ctx.response.defer()
        for guild in self.swd.guilds:
            user = discord.utils.get(guild.members, name=username)
            if user is None:
                pass
            else:
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
        await ctx.respond(embed=own_emb)


def setup(swd):
    swd.add_cog(SWDOwneronly(swd))