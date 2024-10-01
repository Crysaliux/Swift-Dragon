import discord
from discord.ext import commands
from discord import app_commands
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

    @app_commands.command(name='kiss', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def kiss(self, interaction: discord.Interaction, user: discord.Member):
        fun_emb = discord.Embed(title='[Kissing time!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{interaction.user.name} kisses {user.name}!', value=f'➾ {user.mention}', inline=False)
        fun_emb.set_image(url=gs.get_gif("kiss"))
        await interaction.response.send_message(embed=fun_emb)

    @app_commands.command(name='hug', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def hug(self, interaction: discord.Interaction, user: discord.Member):
        fun_emb = discord.Embed(title='[Hugging time!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{interaction.user.name} hugs {user.name}!', value=f'➾ {user.mention}', inline=False)
        fun_emb.set_image(url=gs.get_gif("hug"))
        await interaction.response.send_message(embed=fun_emb)

    @app_commands.command(name='nom', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def nom(self, interaction: discord.Interaction, user: discord.Member):
        fun_emb = discord.Embed(title='[Nomming time!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{interaction.user.name} noms {user.name}!', value=f'➾ {user.mention}', inline=False)
        fun_emb.set_image(url=gs.get_gif("nom"))
        await interaction.response.send_message(embed=fun_emb)

    @app_commands.command(name='nuzzle', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def nuzzle(self, interaction: discord.Interaction, user: discord.Member):
        fun_emb = discord.Embed(title='[Nuzzling time!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{interaction.user.name} nuzzles {user.name}!', value=f'➾ {user.mention}', inline=False)
        fun_emb.set_image(url=gs.get_gif("nuzzle"))
        await interaction.response.send_message(embed=fun_emb)

    @app_commands.command(name='boop', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def boop(self, interaction: discord.Interaction, user: discord.Member):
        fun_emb = discord.Embed(title='[Booping time!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{interaction.user.name} boops {user.name}!', value=f'➾ {user.mention}', inline=False)
        fun_emb.set_image(url=gs.get_gif("boop"))
        await interaction.response.send_message(embed=fun_emb)

    @app_commands.command(name='bite', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def bite(self, interaction: discord.Interaction, user: discord.Member):
        fun_emb = discord.Embed(title='[Biting time!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{interaction.user.name} bites {user.name}!', value=f'➾ {user.mention}', inline=False)
        fun_emb.set_image(url=gs.get_gif("bite"))
        await interaction.response.send_message(embed=fun_emb)

    @app_commands.command(name='lick', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def lick(self, interaction: discord.Interaction, user: discord.Member):
        fun_emb = discord.Embed(title='[Licking time!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{interaction.user.name} licks {user.name}!', value=f'➾ {user.mention}', inline=False)
        fun_emb.set_image(url=gs.get_gif("lick"))
        await interaction.response.send_message(embed=fun_emb)

    @app_commands.command(name='blush', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def blush(self, interaction: discord.Interaction):
        fun_emb = discord.Embed(title='[Blush!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{interaction.user.name} blushes!', value=f'➾ :p', inline=False)
        fun_emb.set_image(url=gs.get_gif("blush"))
        await interaction.response.send_message(embed=fun_emb)

    @app_commands.command(name='wiggle', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def wiggle(self, interaction: discord.Interaction):
        fun_emb = discord.Embed(title="[Wigglin' !]", colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{interaction.user.name} wiggles!', value=f'➾ :p', inline=False)
        fun_emb.set_image(url=gs.get_gif("wiggle"))
        await interaction.response.send_message(embed=fun_emb)

    @app_commands.command(name='happy', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def wiggle(self, interaction: discord.Interaction):
        fun_emb = discord.Embed(title='[Happiness!]', colour=sp.get_color("idle"))
        fun_emb.add_field(name=f'▶{interaction.user.name} is happy!', value=f'➾ :p', inline=False)
        fun_emb.set_image(url=gs.get_gif("happy"))
        await interaction.response.send_message(embed=fun_emb)


async def setup(swd):
    await swd.add_cog(SWDFun(swd))