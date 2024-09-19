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


class SWDArtshare(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "swd_artshare", current)

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.attachments:
            pass
        else:
            await ss.art_spread(message.attachments[0].url, message.author.id, message.guild.id, message.channel.id, message.author.name, self.swd)

    @commands.slash_command(name='register', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def register(self, ctx, info: str):
        await ctx.response.defer()
        check = ss.register_art(ctx.author.id, info, ctx.author.name)
        if check == 'success':
            art_emb = discord.Embed(title='[Your art account has been created!]', colour=sp.get_color("idle"))
            art_emb.add_field(name=f'▶Rules:',
                              value=f'➾ **-** No NSFW is allowed.\n➾ **-** Do not spam art.\n➾ **-** Please keep gore to minimum, all images are moderated.',
                              inline=False)
        else:
            art_emb = discord.Embed(title='[Account already exists!]', colour=sp.get_color("warning"))
            art_emb.add_field(name=f'▶Try:',
                              value=f'➾ **-** Contact staff if you think this is an error.\n➾ **-** Using command again',
                              inline=False)
        await ctx.respond(embed=art_emb)

    @commands.slash_command(name='find_artist', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def find_artist(self, ctx, given_id: int):
        await ctx.response.defer()
        artist = ss.get_artist(uid=given_id)
        if artist != returns.not_found:
            art_emb = discord.Embed(title='[Artist found!]', colour=sp.get_color("idle"))
            art_emb.add_field(name=f'▶Information:',
                              value=f"➾ ID **-** {given_id}\n➾ Name **-** {artist.get('name')}\n➾ Rating **-** {artist.get('rating')}\n➾ Personal Information **-** {artist.get('info')}",
                              inline=False)
        else:
            art_emb = discord.Embed(title='[Artist with given ID does not exist!]', colour=sp.get_color("error"))
            art_emb.add_field(name=f'▶Try:',
                              value=f'➾ **-** Contact staff if you think this is an error.\n➾ **-** Using command again',
                              inline=False)
        await ctx.respond(embed=art_emb)

    @commands.slash_command(name='account_delete', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def account_delete(self, ctx):
        await ctx.response.defer()
        artist = ss.get_artist(artist_id=ctx.author.id)
        check = ss.delete(ctx.author.id)
        if check != returns.not_found:
            art_emb = discord.Embed(title='[Your art account has been deleted!]', colour=sp.get_color("idle"))
            art_emb.add_field(name=f'▶Information:',
                              value=f"➾ **-** Your last name:\n```{artist.get('name')}```\n➾ **-** Your last artist id:\n```{artist.get('uid')}```\n➾ **-** Your last Personal Information:\n```{artist.get('info')}```",
                              inline=False)
        else:
            art_emb = discord.Embed(title='[There is no artist account linked to you!]', colour=sp.get_color("error"))
            art_emb.add_field(name=f'▶Try:',
                              value=f'➾ **-** Contact staff if you think this is an error.\n➾ **-** Using command again',
                              inline=False)
        await ctx.respond(embed=art_emb)


def setup(swd):
    swd.add_cog(SWDArtshare(swd))