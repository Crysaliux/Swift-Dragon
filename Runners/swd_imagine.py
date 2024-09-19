import discord
from discord.ext import commands
from datetime import datetime
import sys
sys.path.append("Runners/Executors")
from dataexecutor import Swdswift_imagine
from console import Swdconsole_logs, returns
from colormanager import Swdcolor_picker

si = Swdswift_imagine()
con_logs = Swdconsole_logs()
sp = Swdcolor_picker()


class SWDImagine(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "swd_imagine", current)

    @commands.slash_command(name='imagine', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def imagine(self, ctx, prompt: str):
        await ctx.response.defer()
        check = si.queue_save(ctx.author.id, ctx.channel.id, prompt)
        if check == returns.exists:
            process_emb = discord.Embed(title='[Still In Queue!]', colour=sp.get_color("warning"))
            process_emb.add_field(
                name=f"▶It seems your request is still in queue, you can't have several requests at once!",
                value=f"➾ **-** Swifty will remind you when generation is ready, remember that prompts must be SFW!\n➾ **-** Join our community to get Swifty updates: https://discord.gg/FpYas3s2Fp",
                inline=False)
        else:
            process_emb = discord.Embed(title='[Waiting In Queue...]', colour=sp.get_color("idle"))
            process_emb.add_field(
                name=f"▶Place in global queue: [{check}]",
                value=f"➾ **-** Swifty will remind you when generation is ready, remember that prompts must be SFW!\n➾ **-** Join our community to get Swifty updates: https://discord.gg/FpYas3s2Fp",
                inline=False)
        await ctx.respond(embed=process_emb)

        await si.queue_remove(self.swd)


def setup(swd):
    swd.add_cog(SWDImagine(swd))