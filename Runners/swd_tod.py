import random
import discord
from discord.ext import commands
from peewee import *
import sys
sys.path.append("Runners/Executors")
from dataexecutor import Swdmain_settings
from colormanager import Swdcolor_picker

ss = Swdmain_settings()
sp = Swdcolor_picker()


class Select(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Truth", custom_id='truth-button', row=0, style=discord.ButtonStyle.green)
    async def first_button_callback(self, button, interaction):
        question = random.choice(open('Data/truth_or_dare/truth.txt').read().splitlines())
        tod_emb = discord.Embed(title=f'[Truth] [Requested by {interaction.user.name}]', colour=sp.get_color("idle"))
        tod_emb.add_field(name='~~~', value=f'➾ **-** {question}', inline=False)
        await interaction.response.send_message(embed=tod_emb, view=Select())

    @discord.ui.button(label="Dare", custom_id='dare-button', row=0, style=discord.ButtonStyle.green)
    async def second_button_callback(self, button, interaction):
        question = random.choice(open('Data/truth_or_dare/dare.txt').read().splitlines())
        tod_emb = discord.Embed(title=f'[Dare] [Requested by {interaction.user.name}]', colour=sp.get_color("idle"))
        tod_emb.add_field(name='~~~', value=f'➾ **-** {question}', inline=False)
        await interaction.response.send_message(embed=tod_emb, view=Select())

    @discord.ui.button(label="Random", custom_id='random-button', row=0, style=discord.ButtonStyle.red)
    async def third_button_callback(self, button, interaction):
        if random.randint(0, 1) == 1:
            question = random.choice(open('Data/truth_or_dare/dare.txt').read().splitlines())
            tod_emb = discord.Embed(title=f'[Dare] [Requested by {interaction.user.name}]', colour=sp.get_color("idle"))
            tod_emb.add_field(name='~~~', value=f'➾ **-** {question}', inline=False)
        else:
            question = random.choice(open('Data/truth_or_dare/truth.txt').read().splitlines())
            tod_emb = discord.Embed(title=f'[Truth] [Requested by {interaction.user.name}]', colour=sp.get_color("idle"))
            tod_emb.add_field(name='~~~', value=f'➾ **-** {question}', inline=False)
        await interaction.response.send_message(embed=tod_emb, view=Select())

class SWDTod(commands.Cog):
    def __init__(self, swd):
        self.swd = swd

    @commands.slash_command(name='play', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def play(self, ctx):
        await ctx.response.defer()
        tod = ss.swd_pull(ctx.guild.id, 'tod')
        error_emb = discord.Embed(title='[This channel is not for ToD]', colour=sp.get_color("warning"))
        error_emb.add_field(name=f'▶Please head to https://discord.com/channels/{ctx.guild.id}/{tod.get("channel_id")}',
                            value='➾ **-** Contact server staff if you think this is a mistake.',
                            inline=False)
        tod_emb = discord.Embed(title='[ToD started!]', colour=sp.get_color("idle"))
        tod_emb.add_field(name='Press one of the buttons below', value=f'➾ **-** Truth\n➾ **-** Dare',
                          inline=False)
        if ctx.channel.id != tod.get("channel_id"):
            await ctx.respond(embed=error_emb)
        else:
            await ctx.respond(embed=tod_emb, view=Select())

    @commands.Cog.listener()
    async def on_ready(self):
        self.swd.add_view(Select())


def setup(swd):
    swd.add_cog(SWDTod(swd))