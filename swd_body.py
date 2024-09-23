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