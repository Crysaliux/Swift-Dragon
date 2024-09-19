import discord
from discord.ext import commands
from discord.ext.pages import PaginatorButton, Paginator, Page
from datetime import datetime
import sys
sys.path.append("Runners/Executors")
from console import Swdconsole_logs
from colormanager import Swdcolor_picker

con_logs = Swdconsole_logs()
sp = Swdcolor_picker()


class SWDInfo(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        self.pages = [
            Page(
                embeds=[
                    discord.Embed(title="[General information]", fields=[
                        discord.EmbedField(name="▶About us:", value="➾ **-** Swift Dragon is a project maintained by sevaral people. When using services this app provides, you **must** abide by our guidelines listed below. Please make yourself familiar with them before reading further!", inline=False),
                        discord.EmbedField(name="▶Main Guidelines:", value="➾ **-** General:\n[1] - Any media, links to media used by Swift Dragon **should not** be copied/spread without permission\n[2] - Users using any bugs/loopholes in bot's functionality without reporting them to dev team will be banned from using this app\n[3] - We do not tolerate any communities/members that support ||terrorism||, ||abuse||, ||suicidal topics||. Those will be instantly banned from using our app\n➾ **-** Artshare:\n[7] - Images containing ||gore|| or ||nsfw|| are not allowed\n[8] - Each art gets spoilered automatically, to avoid it being stolen. If this function decreases your art's quality in any way, please let us know here [Our official community](https://discord.gg/f9Q4YRPRwW)\n➾ **-** Global chat:\n[9] - No spamming is allowed (gifs flood, too many stickers, random text)\n[10] - Be kind and respectful to others\n[11] - Keep chat SFW. Global chat is being monitored by our AI security 24/7", inline=False),
                        discord.EmbedField(name="▶AI Guidelines:", value="➾ **-** Swift AI:\n[4] - Using Character models to impersonate, abuse or trick people is stricktly prohibited\n[5] - We have right to remove Character models with inappropriate nicknames, avatars or description\n[6] - Keep your questions sfw!", inline=False)
                    ])
                ]
            )
        ]

        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "swd_info", current)

    @commands.slash_command(name='help', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def help(self, ctx):
        await ctx.response.defer()
        paginator = Paginator(pages=self.pages)
        help_emb = discord.Embed(title='[Information/Commands]', colour=sp.get_color("idle"))
        help_emb.add_field(name=f'▶Bots functionality:',
                           value=f'➾ /setup **-** runs setup function for your server.\n➾ /settings **-** View desired channels for ToD, Globalchat and Logs.\n➾ /play **-** use to trigger ToD game.\n➾ /tod **-** configure tod channel and settings.\n➾ /gchat **-** configure global chat channel and settings',
                           inline=False)
        await paginator.respond(ctx.interaction)


def setup(swd):
    swd.add_cog(SWDInfo(swd))