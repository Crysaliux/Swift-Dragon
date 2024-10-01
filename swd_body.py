import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import app_commands
from datetime import datetime
import tracemalloc

from Runners.Executors.console import Swdconsole_logs
from Runners.Executors.colormanager import Swdcolor_picker
from Runners.Executors.configmanager import Config
from Runners.Executors.dataexecutor import Swdmain_settings


intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

tracemalloc.start()
conf = Config()


class SwiftDragon(Bot, Swdconsole_logs, Swdcolor_picker, Config, Swdmain_settings):
    def __init__(self, intents=conf.swift_config()["intents"], owner_id=conf.swift_config()["owner_id"], prefix='sw.', swd_cogs=conf.swift_config()["cogs"], token=conf.swift_config()["token"]) -> None:
        current = datetime.today().strftime('%Y-%m-%d')
        Swdconsole_logs.logs(self, '001', "swd_body", current)

        self.swd_intents = intents
        self.owner_id = owner_id
        self.prefix = prefix
        self.swd_cogs = swd_cogs
        self.token = token
        super(SwiftDragon, self).__init__(command_prefix=prefix, tree_cls=CommandErrorHandler, intents=intents, owner_id=owner_id)

    def swd_run(self):
        super().run(self.token)

    def member_count_update(self):
        try:
            member_count = 0
            for member in super().get_all_members():
                member_count += 1
            return member_count
        except:
            current = datetime.today().strftime('%Y-%m-%d')
            super().error('1300', current)

    async def on_ready(self):
        for cog in self.swd_cogs:
            await super().load_extension(f'{cog}')

        await super().change_presence(status=discord.Status.idle, activity=discord.Game(name=f'Looking at {self.member_count_update()} dragons!'))

    async def on_member_join(self, member):
        await super().change_presence(status=discord.Status.idle, activity=discord.Game(name=f'Looking at {self.member_count_update()} dragons!'))

    async def on_member_remove(self, member):
        await super().change_presence(status=discord.Status.idle, activity=discord.Game(name=f'Looking at {self.member_count_update()} dragons!'))

    async def command_executed(self, message):
        super().check_connection()


class CommandErrorHandler(app_commands.CommandTree, Swdcolor_picker):
    async def on_error(self, interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
        if isinstance(error, discord.app_commands.CommandOnCooldown):
            warning_emb = discord.Embed(title='[No that fast! :0]', colour=Swdcolor_picker.get_color(self, "warning"))
            warning_emb.add_field(name=f"▶You running commands too often! Retry in {error.retry_after:.2f} seconds",
                                  value=f'➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Command is on cooldown, warning code: 020```',
                                  inline=False)
            await interaction.response.send_message(embed=warning_emb, ephemeral=True)

        elif isinstance(error, discord.app_commands.MissingPermissions):
            warning_emb = discord.Embed(title='[Missing Permissions!]',
                                        colour=Swdcolor_picker.get_color(self, "warning"))
            warning_emb.add_field(
                name="▶It seems you're missing some permissions, ask staff if you think this is an error",
                value=f'➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Not enough permissions provided, warning code: 010```',
                inline=False)
            await interaction.response.send_message(embed=warning_emb, ephemeral=True)

        elif isinstance(error, discord.app_commands.BotMissingPermissions):
            warning_emb = discord.Embed(title='[Bot Missing Permissions!]',
                                        colour=Swdcolor_picker.get_color(self, "warning"))
            warning_emb.add_field(
                name="▶It seems Swifty is missing some permissions, she can't work work with roles higher than her own :c",
                value=f'➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Not enough permissions provided, warning code: 010```',
                inline=False)
            await interaction.response.send_message(embed=warning_emb, ephemeral=True)
        else:
            raise error


sd = SwiftDragon()
sd.swd_run()