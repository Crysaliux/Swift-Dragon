import discord
from discord.ext import commands
from discord import app_commands, interactions
from datetime import datetime


from Runners.Executors.dataexecutor import Swdmain_settings
from Runners.Executors.console import Swdconsole_logs, returns
from Runners.Executors.colormanager import Swdcolor_picker

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

    @app_commands.command(name='register', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def register(self, interaction: discord.Interaction, info: str):
        check = ss.register_art(interaction.user.id, info, interaction.user.name)
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
        await interaction.response.send_message(embed=art_emb)

    @app_commands.command(name='find_artist', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def find_artist(self, interaction: discord.Interaction, given_id: int):
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
        await interaction.response.send_message(embed=art_emb)

    @app_commands.command(name='account_delete', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def account_delete(self, interaction: discord.Interaction):
        artist = ss.get_artist(artist_id=interaction.user.id)
        check = ss.delete(interaction.user.id)
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
        await interaction.response.send_message(embed=art_emb)


async def setup(swd):
    await swd.add_cog(SWDArtshare(swd))