<<<<<<< HEAD
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
=======
import discord
from discord.ext import commands
from datetime import datetime
import sys
sys.path.append("Runners/Executors")
from addonexecutor import AddonWalker
from console import Swdconsole_logs
from colormanager import Swdcolor_picker
from dataexecutor import Swdmain_settings

con_logs = Swdconsole_logs()
sp = Swdcolor_picker()
ss = Swdmain_settings()


current = datetime.today().strftime('%Y-%m-%d')
con_logs.logs('001', "swd_body", current)

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
swd = discord.Bot(command_prefix='sw.', intents=intents, owner_id=830486806478848040)

cogs_list = [
        'Runners.swd_setup',
        'Runners.swd_logs',
        'Runners.swd_gchat',
        'Runners.swd_tod',
        'Runners.swd_info',
        'Runners.swd_greeting',
        'Runners.swd_artshare',
        'Runners.swd_chat',
        'Runners.swd_imagine',
        'Runners.swd_fun',
        "Runners.swd_owneronly"
    ]
new_cogs_list = AddonWalker(cogs_list)
for cog in new_cogs_list:
    swd.load_extension(f'{cog}')

def member_count_update():
    try:
        member_count = 0
        for guild in swd.guilds:
            member_count = member_count + len(guild.members)
        return member_count
    except:
        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.error('1300', current)

@swd.event
async def on_ready():
    await swd.change_presence(status=discord.Status.idle,
                              activity=discord.Game(name=f'Looking at {member_count_update()} dragons!'))

@swd.event
async def on_member_join(member):
    await swd.change_presence(status=discord.Status.idle,
                              activity=discord.Game(name=f'Looking at {member_count_update()} dragons!'))

@swd.event
async def on_member_remove(member):
    await swd.change_presence(status=discord.Status.idle,
                              activity=discord.Game(name=f'Looking at {member_count_update()} dragons!'))

@swd.before_invoke
async def command_executed(message):
    ss.check_connection()

@swd.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        warning_emb = discord.Embed(title='[No that fast! :0]', colour=sp.get_color("warning"))
        warning_emb.add_field(name=f"▶You running commands too often! Retry in {error.retry_after:.2f} seconds",
                            value=f'➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Command is on cooldown, warning code: 020```',
                            inline=False)
        await ctx.respond(embed=warning_emb, ephemeral=True)

    elif isinstance(error, commands.MissingPermissions):
        warning_emb = discord.Embed(title='[Missing Permissions!]', colour=sp.get_color("warning"))
        warning_emb.add_field(name="▶It seems you're missing some permissions, ask staff if you think this is an error",
                              value=f'➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Not enough permissions provided, warning code: 010```',
                              inline=False)
        await ctx.respond(embed=warning_emb, ephemeral=True)

    elif isinstance(error, commands.BotMissingPermissions):
        warning_emb = discord.Embed(title='[Bot Missing Permissions!]', colour=sp.get_color("warning"))
        warning_emb.add_field(name="▶It seems Swifty is missing some permissions, she can't work work with roles higher than her own :c",
                              value=f'➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Not enough permissions provided, warning code: 010```',
                              inline=False)
        await ctx.respond(embed=warning_emb, ephemeral=True)
    else:
        raise error


try:
    swd.run(open("Runners/Executors/ts_data/swift.txt", "r").readline())
except:
    current = datetime.today().strftime('%Y-%m-%d')
    con_logs.error('1400', current)
>>>>>>> 6697f8dd6ee0aab8dec0c1c083990599333ca1ea
