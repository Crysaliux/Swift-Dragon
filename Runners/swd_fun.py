import discord
from discord.ext import commands
from datetime import datetime
import sys
sys.path.append("Runners/Executors")
from console import Swdconsole_logs
from gifmanager import Swdgif_selector
from colormanager import Swdcolor_picker

con_logs = Swdconsole_logs()
gs = Swdgif_selector()
sp = Swdcolor_picker()


class SWDFun(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "swd_fun", current)

    @commands.slash_command(name='kiss', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def kiss(self, ctx, user: discord.Member):
        fun_emb = discord.Embed(title='[Kissing time!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{ctx.author.name} kisses {user.name}!', value=f'➾ {user.mention}', inline=False)
        fun_emb.set_image(url=gs.get_gif("kiss"))
        await ctx.respond(embed=fun_emb)

    @commands.slash_command(name='hug', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def hug(self, ctx, user: discord.Member):
        fun_emb = discord.Embed(title='[Hugging time!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{ctx.author.name} hugs {user.name}!', value=f'➾ {user.mention}', inline=False)
        fun_emb.set_image(url=gs.get_gif("hug"))
        await ctx.respond(embed=fun_emb)

    @commands.slash_command(name='nom', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def nom(self, ctx, user: discord.Member):
        fun_emb = discord.Embed(title='[Nomming time!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{ctx.author.name} noms {user.name}!', value=f'➾ {user.mention}', inline=False)
        fun_emb.set_image(url=gs.get_gif("nom"))
        await ctx.respond(embed=fun_emb)

    @commands.slash_command(name='nuzzle', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def nuzzle(self, ctx, user: discord.Member):
        fun_emb = discord.Embed(title='[Nuzzling time!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{ctx.author.name} nuzzles {user.name}!', value=f'➾ {user.mention}', inline=False)
        fun_emb.set_image(url=gs.get_gif("nuzzle"))
        await ctx.respond(embed=fun_emb)

    @commands.slash_command(name='boop', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def boop(self, ctx, user: discord.Member):
        fun_emb = discord.Embed(title='[Booping time!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{ctx.author.name} boops {user.name}!', value=f'➾ {user.mention}', inline=False)
        fun_emb.set_image(url=gs.get_gif("boop"))
        await ctx.respond(embed=fun_emb)

    @commands.slash_command(name='bite', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def bite(self, ctx, user: discord.Member):
        fun_emb = discord.Embed(title='[Biting time!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{ctx.author.name} bites {user.name}!', value=f'➾ {user.mention}', inline=False)
        fun_emb.set_image(url=gs.get_gif("bite"))
        await ctx.respond(embed=fun_emb)

    @commands.slash_command(name='lick', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def lick(self, ctx, user: discord.Member):
        fun_emb = discord.Embed(title='[Licking time!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{ctx.author.name} licks {user.name}!', value=f'➾ {user.mention}', inline=False)
        fun_emb.set_image(url=gs.get_gif("lick"))
        await ctx.respond(embed=fun_emb)

    @commands.slash_command(name='blush', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def blush(self, ctx):
        fun_emb = discord.Embed(title='[Blush!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{ctx.author.name} blushes!', value=f'➾ :p', inline=False)
        fun_emb.set_image(url=gs.get_gif("blush"))
        await ctx.respond(embed=fun_emb)

    @commands.slash_command(name='wiggle', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def wiggle(self, ctx):
        fun_emb = discord.Embed(title="[Wigglin' !]", colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{ctx.author.name} wiggles!', value=f'➾ :p', inline=False)
        fun_emb.set_image(url=gs.get_gif("wiggle"))
        await ctx.respond(embed=fun_emb)

    @commands.slash_command(name='happy', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def wiggle(self, ctx):
        fun_emb = discord.Embed(title='[Happiness!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{ctx.author.name} is happy!', value=f'➾ :p', inline=False)
        fun_emb.set_image(url=gs.get_gif("happy"))
        await ctx.respond(embed=fun_emb)


def setup(swd):
    swd.add_cog(SWDFun(swd))