import random
import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import json
from datetime import datetime


from Runners.Executors.dataexecutor import Swdmain_settings
from Runners.Executors.console import Swdconsole_logs
from Runners.Executors.colormanager import Swdcolor_picker

ss = Swdmain_settings()
con_logs = Swdconsole_logs()
sp = Swdcolor_picker()


class SecondStage(discord.ui.View):
    def __init__(self, swd: commands.Bot):
        super().__init__(timeout=None)
        self.swd = swd

    @discord.ui.select(
        row = 0,
        cls=discord.ui.ChannelSelect,
        placeholder = "Select a channel to receive logs",
        min_values = 1,
        max_values = 1,
        channel_types=[discord.ChannelType.text],
        custom_id='select-logs'
    )
    async def select_logs(self, interaction, select):
        ss.swd_setup('logs', interaction.guild.id, select.values[0].id, 'all')
        settings_emb = discord.Embed(title=f'[{ss.running_bar(8, 2)}]', colour=sp.get_color("idle"))
        settings_emb.add_field(name='▶Setup:',
                               value='➾ **-** You can now set a channel to play ToD in\n➾ **-** Use /settings to view current active modules\n➾ **-** /tod will help you configuring this module later',
                               inline=False)
        settings_emb.add_field(name='▶Playing Truth or Dare',
                               value="➾ **-** Run /play in selected channel (check /settings if you don't remember! :3)\n➾ **-** Click [Truth] or [Dare] buttons to get new tasks or press [Random] to get either Truth or Dare task\n➾ **-** Have fun! :p",
                               inline=False)
        await interaction.response.edit_message(embed=settings_emb, view=ThirdStage(swd=self.swd))

    @discord.ui.button(label="Skip to ToD settings", row=1, style=discord.ButtonStyle.blurple, custom_id='skip-button')
    async def skip_button(self, interaction, button):
        ss.swd_setup('logs', interaction.guild.id, 0, 'all')
        settings_emb = discord.Embed(title=f'[{ss.running_bar(8, 2)}]', colour=sp.get_color("idle"))
        settings_emb.add_field(name='▶Setup:',
                               value='➾ **-** You can now set a channel to play ToD in\n➾ **-** Use /settings to view current active modules\n➾ **-** /tod will help you configuring this module later',
                               inline=False)
        settings_emb.add_field(name='▶Playing Truth or Dare',
                               value="➾ **-** Run /play in selected channel (check /settings if you don't remember! :3)\n➾ **-** Click [Truth] or [Dare] buttons to get new tasks or press [Random] to get either Truth or Dare task\n➾ **-** Have fun! :p",
                               inline=False)
        await interaction.response.edit_message(embed=settings_emb, view=ThirdStage(swd=self.swd))

class ThirdStage(discord.ui.View):
    def __init__(self, swd: commands.Bot):
        super().__init__(timeout=None)
        self.swd = swd

    @discord.ui.select(
        row = 0,
        cls=discord.ui.ChannelSelect,
        placeholder = "Select a channel to play Truth or Dare",
        min_values = 1,
        max_values = 1,
        channel_types=[discord.ChannelType.text],
        custom_id='select-tod'
    )
    async def select_tod(self, interaction, select):
        ss.swd_setup('tod', interaction.guild.id, select.values[0].id, 'on')
        settings_emb = discord.Embed(title=f'[{ss.running_bar(8, 3)}]', colour=sp.get_color("idle"))
        settings_emb.add_field(name='▶Setup:',
                               value='➾ **-** Selecting General Chat channel\n➾ **-** Use /settings to view current active modules\n➾ **-** /gchat will help you configuring this module later',
                               inline=False)
        settings_emb.add_field(name='▶How does General Chat work?',
                               value="➾ **-** This module connects several discord servers, creating interserver chat in selected channel\n➾ **-** Bot GNrules (General rules) apply to this module\n➾ **-** Remember that this module in still in development, unexpected bugs/errors may occur!",
                               inline=False)
        await interaction.response.edit_message(embed=settings_emb, view=FourthStage(swd=self.swd))

    @discord.ui.button(label="Skip to Gchat [beta!]", row=1, style=discord.ButtonStyle.blurple, custom_id='skip-button')
    async def skip_button(self, interaction, button):
        ss.swd_setup('tod', interaction.guild.id, 0, 'off')
        settings_emb = discord.Embed(title=f'[{ss.running_bar(8, 3)}]', colour=sp.get_color("idle"))
        settings_emb.add_field(name='▶Setup:',
                               value='➾ **-** You can now set a channel to play ToD in\n➾ **-** Use /settings to view current active modules\n➾ **-** /tod will help you configuring this module later',
                               inline=False)
        settings_emb.add_field(name='▶Playing Truth or Dare',
                               value="➾ **-** Run /play in selected channel (check /settings if you don't remember! :3)\n➾ **-** Click [Truth] or [Dare] buttons to get new tasks or press [Random] to get either Truth or Dare task\n➾ **-** Have fun! :p",
                               inline=False)
        await interaction.response.edit_message(embed=settings_emb, view=FourthStage(swd=self.swd))


class FourthStage(discord.ui.View):
    def __init__(self, swd: commands.Bot):
        super().__init__(timeout=None)
        self.swd = swd

    @discord.ui.select(
        row = 0,
        cls=discord.ui.ChannelSelect,
        placeholder = "Select a channel to participate in global chat",
        min_values = 1,
        max_values = 1,
        channel_types=[discord.ChannelType.text],
        custom_id='select-gchat'
    )
    async def select_gchat(self, interaction, select):
        ss.swd_setup('gchat', interaction.guild.id, select.values[0].id, 'on')
        settings_emb = discord.Embed(title=f'[{ss.running_bar(8, 4)}]', colour=sp.get_color("idle"))
        settings_emb.add_field(name='▶Setup:',
                               value='➾ **-** Selecting Swifty AI Chat channel\n➾ **-** Use /settings to view current active modules\n➾ **-** /chat will help you configuring this module later',
                               inline=False)
        settings_emb.add_field(name='▶How to chat with Swifty',
                               value="➾ **-** Create your own characters and chat with them in selected channel!\n➾ **-** Use /character_create [name] [prefix] [avatar url] to create your own character\n➾ **-** All server members are able to create their character models\n➾ **-** More information in /help, SArules (Swifty AI rules) apply here",
                               inline=False)
        await interaction.response.edit_message(embed=settings_emb, view=FifthStage(swd=self.swd))


    @discord.ui.button(label="Skip to Swifty AI", row=1, style=discord.ButtonStyle.blurple, custom_id='skip-button')
    async def skip_button(self, interaction, button):
        ss.swd_setup('gchat', interaction.guild.id, 0, 'off')
        settings_emb = discord.Embed(title=f'[{ss.running_bar(8, 4)}]', colour=sp.get_color("idle"))
        settings_emb.add_field(name='▶Setup:',
                               value='➾ **-** Selecting Swifty AI Chat channel\n➾ **-** Use /settings to view current active modules\n➾ **-** /chat will help you configuring this module later',
                               inline=False)
        settings_emb.add_field(name='▶How to chat with Swifty',
                               value="➾ **-** Create your own characters and chat with them in selected channel!\n➾ **-** Use /character_create [name] [prefix] [avatar url] to create your own character\n➾ **-** All server members are able to create their character models\n➾ **-** More information in /help, SArules (Swifty AI rules) apply here",
                               inline=False)
        await interaction.response.edit_message(embed=settings_emb, view=FifthStage(swd=self.swd))


class FifthStage(discord.ui.View):
    def __init__(self, swd: commands.Bot):
        super().__init__(timeout=None)
        self.swd = swd

    @discord.ui.select(
        row = 0,
        cls=discord.ui.ChannelSelect,
        placeholder = "Select a channel to use Swifty AI",
        min_values = 1,
        max_values = 1,
        channel_types=[discord.ChannelType.text],
        custom_id='select-chat'
    )
    async def select_chat(self, interaction, select):
        ss.swd_setup('chat', interaction.guild.id, select.values[0].id, 'on')
        settings_emb = discord.Embed(title=f'[{ss.running_bar(8, 5)}]', colour=sp.get_color("idle"))
        settings_emb.add_field(name='▶Setup:',
                               value='➾ **-** Artshare channel selection\n➾ **-** Use /settings to view current active modules\n➾ **-** /artshare will help you configuring this module later',
                               inline=False)
        settings_emb.add_field(name='▶What is Artshare?',
                               value="➾ **-** Artshare enables artists to share their art across discord communities\n➾ **-** Just send your art in selected channel and it'll be instantly spread! We, of course, make sure that art isn't stolen. A watermark will be added to your art as soon as it reaches another community\n➾ **-** Use /register to create a new artist profile or /accout_delete to remove an existing one\n GArules (General Art rules) apply",
                               inline=False)
        await interaction.response.edit_message(embed=settings_emb, view=SixthStage(swd=self.swd))


    @discord.ui.button(label="Skip to Artshare", row=1, style=discord.ButtonStyle.blurple, custom_id='skip-button')
    async def skip_button(self, interaction, button):
        ss.swd_setup('chat', interaction.guild.id, 0, 'off')
        settings_emb = discord.Embed(title=f'[{ss.running_bar(8, 5)}]', colour=sp.get_color("idle"))
        settings_emb.add_field(name='▶Setup:',
                               value='➾ **-** Artshare channel selection\n➾ **-** Use /settings to view current active modules\n➾ **-** /artshare will help you configuring this module later',
                               inline=False)
        settings_emb.add_field(name='▶What is Artshare?',
                               value="➾ **-** Artshare enables artists to share their art across discord communities\n➾ **-** Just send your art in selected channel and it'll be instantly spread! We, of course, make sure that art isn't stolen. A watermark will be added to your art as soon as it reaches another community\n➾ **-** Use /register to create a new artist profile or /accout_delete to remove an existing one\n GArules (General Art rules) apply",
                               inline=False)
        await interaction.response.edit_message(embed=settings_emb, view=SixthStage(swd=self.swd))


class SixthStage(discord.ui.View):
    def __init__(self, swd: commands.Bot):
        super().__init__(timeout=None)
        self.swd = swd

    @discord.ui.select(
        row = 0,
        cls=discord.ui.ChannelSelect,
        placeholder = "Select a channel for Artshare",
        min_values = 1,
        max_values = 1,
        channel_types=[discord.ChannelType.text],
        custom_id='select-artshare'
    )
    async def select_artshare(self, interaction, select):
        ss.swd_setup('artshare', interaction.guild.id, select.values[0].id, 'on')
        settings_emb = discord.Embed(title=f'[{ss.running_bar(8, 6)}]', colour=sp.get_color("idle"))
        settings_emb.add_field(name='▶Setup:',
                               value='➾ **-** Selecting channel for Greetings\n➾ **-** Use /settings to view current active modules\n➾ **-** /greeting will help you configuring this module later',
                               inline=False)
        settings_emb.add_field(name='▶Configuring Greetings',
                               value="➾ **-** Greetings module allows youto welcome your members in a warm and happy way!\n➾ **-**  You can use <member> to mention the new member and add urls/role mentions/emojis to your massage which makes this module higly configurable\n➾ **-** Give em a warm dragon hug! :3",
                               inline=False)
        await interaction.response.edit_message(embed=settings_emb, view=SeventhStage(swd=self.swd))


    @discord.ui.button(label="Skip to Greetings", row=1, style=discord.ButtonStyle.blurple, custom_id='skip-button')
    async def skip_button(self, interaction, button):
        ss.swd_setup('artshare', interaction.guild.id, 0, 'off')
        settings_emb = discord.Embed(title=f'[{ss.running_bar(8, 6)}]', colour=sp.get_color("idle"))
        settings_emb.add_field(name='▶Setup:',
                               value='➾ **-** Selecting channel for Greetings\n➾ **-** Use /settings to view current active modules\n➾ **-** /greeting will help you configuring this module later',
                               inline=False)
        settings_emb.add_field(name='▶Configuring Greetings',
                               value="➾ **-** Greetings module allows you to welcome your members in a warm and happy way!\n➾ **-**  You can use <member> to mention the new member and add urls/role mentions/emojis to your massage which makes this module higly configurable\n➾ **-** Give em a warm dragon hug! :3",
                               inline=False)
        await interaction.response.edit_message(embed=settings_emb, view=SeventhStage(swd=self.swd))

class SeventhStage(discord.ui.View):
    def __init__(self, swd: commands.Bot):
        super().__init__(timeout=None)
        self.swd = swd

    @discord.ui.select(
        row=0,
        cls=discord.ui.ChannelSelect,
        placeholder="Select a channel for Greetings",
        min_values=1,
        max_values=1,
        channel_types=[discord.ChannelType.text],
        custom_id='select-greetings'
    )
    async def select_greetings(self, interaction, select):
        self.swd.add_view(EighthStage(swd=self.swd, channel_id=select.values[0].id))
        settings_emb = discord.Embed(title=f'[{ss.running_bar(8, 7)}]', colour=sp.get_color("idle"))
        settings_emb.add_field(name='▶Setup:',
                                value='➾ **-** Setting welcome message for Greetings module\n➾ **-** Use /settings to view current active modules\n➾ **-** /greeting will help you configuring this module later',
                                inline=False)
        settings_emb.add_field(name='▶Configuring Greetings',
                                value="➾ **-** Greetings module allows you to welcome your members in a warm and happy way!\n➾ **-**  You can use <member> to mention the new member and add urls/role mentions/emojis to your massage which makes this module higly configurable\n➾ **-** Give em a warm dragon hug! :3",
                                inline=False)
        await interaction.response.edit_message(embed=settings_emb, view=EighthStage(swd=self.swd, channel_id=select.values[0].id))

    @discord.ui.button(label="Skip to Complete", row=1, style=discord.ButtonStyle.blurple, custom_id='skip-button')
    async def skip_button(self, interaction, button):
        ss.swd_setup('greetings', interaction.guild.id, 0, 'off', '**Welcome, <member>!** _(Default message)_')
        logs = ss.swd_pull(interaction.guild.id, 'logs')
        gchat = ss.swd_pull(interaction.guild.id, 'gchat')
        tod = ss.swd_pull(interaction.guild.id, 'tod')
        chat = ss.swd_pull(interaction.guild.id, 'chat')
        greetings = ss.swd_pull(interaction.guild.id, 'greetings')
        artshare = ss.swd_pull(interaction.guild.id, 'artshare')
        settings_emb = discord.Embed(title=f'[{ss.running_bar(8, 8)}]', colour=sp.get_color("idle"))
        settings_emb.add_field(name='▶Setup complete!',
                                value='➾ **-** Selecting channel for Greetings\n➾ **-** Use /settings to view current active modules',
                                inline=False)
        settings_emb.add_field(name='▶Server logs',
                            value=f"➾ **-** Channel: {ss.swd_channel_modify(logs.get('channel_id'), interaction.guild.id)} | status: {logs.get('status')}",
                            inline=False)
        settings_emb.add_field(name='▶Global chat',
                            value=f"➾ **-** Channel: {ss.swd_channel_modify(gchat.get('channel_id'), interaction.guild.id)} | status: {gchat.get('status')}",
                            inline=False)
        settings_emb.add_field(name='▶Truth or Dare',
                            value=f"➾ **-** Channel: {ss.swd_channel_modify(tod.get('channel_id'), interaction.guild.id)} | status: {tod.get('status')}",
                            inline=False)
        settings_emb.add_field(name='▶Swifty AI chat',
                            value=f"➾ **-** Channel: {ss.swd_channel_modify(chat.get('channel_id'), interaction.guild.id)} | status: {chat.get('status')}",
                            inline=False)
        settings_emb.add_field(name='▶Greeting',
                            value=f"➾ **-** Channel: {ss.swd_channel_modify(greetings.get('channel_id'), interaction.guild.id)} | status: {greetings.get('status')}\nMessage:\n```{greetings.get('message')}```",
                            inline=False)
        settings_emb.add_field(name='▶Artshare',
                            value=f"➾ **-** Channel: {ss.swd_channel_modify(artshare.get('channel_id'), interaction.guild.id)} | status: {artshare.get('status')}",
                            inline=False)
        roulette = random.randint(0, 100)
        if roulette < 50:
            settings_emb.set_footer(text='You got a happy dragon! 50% chance of getting one :3', icon_url='')
        elif roulette < 30:
            settings_emb.set_footer(text='You got a blushy dragon! 30% chance of getting one :3', icon_url='')
        elif roulette < 10:
            settings_emb.set_footer(text='Cool dragon! 10% chance of getting one :3', icon_url='')
        await interaction.response.edit_message(embed=settings_emb, view=None)

class EighthStage(discord.ui.View):
    def __init__(self, swd: commands.Bot, channel_id):
        super().__init__(timeout=None)
        self.swd = swd
        self.channel_id = channel_id

    @discord.ui.button(label="Set welcome message", custom_id='setup', row=0, style=discord.ButtonStyle.green)
    async def greeting_button(self, interaction, button):
        modal = ESModal(swd=self.swd, channel_id=self.channel_id, title='Welcome message!')
        await interaction.response.send_modal(modal)

class ESModal(discord.ui.Modal):
    def __init__(self, swd, channel_id, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.swd = swd
        self.channel_id = channel_id

    w_message = discord.ui.TextInput(
        label='Your welcome message goes here:',
        placeholder='Welcome message',
        style=discord.TextStyle.long,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        ss.swd_setup('greetings', interaction.guild.id, self.channel_id, 'on', self.w_message.value)
        logs = ss.swd_pull(interaction.guild.id, 'logs')
        gchat = ss.swd_pull(interaction.guild.id, 'gchat')
        tod = ss.swd_pull(interaction.guild.id, 'tod')
        chat = ss.swd_pull(interaction.guild.id, 'chat')
        greetings = ss.swd_pull(interaction.guild.id, 'greetings')
        artshare = ss.swd_pull(interaction.guild.id, 'artshare')
        settings_emb = discord.Embed(title=f'[{ss.running_bar(8, 8)}]', colour=sp.get_color("idle"))
        settings_emb.add_field(name='▶Setup complete!',
                               value='➾ **-** Selecting channel for Greetings\n➾ **-** Use /settings to view current active modules',
                               inline=False)
        settings_emb.add_field(name='▶Server logs',
                               value=f"➾ **-** Channel: {ss.swd_channel_modify(logs.get('channel_id'), interaction.guild.id)} | status: {logs.get('status')}",
                               inline=False)
        settings_emb.add_field(name='▶Global chat',
                               value=f"➾ **-** Channel: {ss.swd_channel_modify(gchat.get('channel_id'), interaction.guild.id)} | status: {gchat.get('status')}",
                               inline=False)
        settings_emb.add_field(name='▶Truth or Dare',
                               value=f"➾ **-** Channel: {ss.swd_channel_modify(tod.get('channel_id'), interaction.guild.id)} | status: {tod.get('status')}",
                               inline=False)
        settings_emb.add_field(name='▶Swifty AI chat',
                               value=f"➾ **-** Channel: {ss.swd_channel_modify(chat.get('channel_id'), interaction.guild.id)} | status: {chat.get('status')}",
                               inline=False)
        settings_emb.add_field(name='▶Greeting',
                               value=f"➾ **-** Channel: {ss.swd_channel_modify(greetings.get('channel_id'), interaction.guild.id)} | status: {greetings.get('status')}\nMessage:\n```{greetings.get('message')}```",
                               inline=False)
        settings_emb.add_field(name='▶Artshare',
                               value=f"➾ **-** Channel: {ss.swd_channel_modify(artshare.get('channel_id'), interaction.guild.id)} | status: {artshare.get('status')}",
                               inline=False)
        roulette = random.randint(0, 100)
        if roulette < 50:
            settings_emb.set_footer(text='You got a happy dragon! 50% chance of getting one :3', icon_url='')
        elif roulette < 30:
            settings_emb.set_footer(text='You got a blushy dragon! 30% chance of getting one :3', icon_url='')
        elif roulette < 10:
            settings_emb.set_footer(text='Cool dragon! 10% chance of getting one :3', icon_url='')
        await interaction.response.edit_message(embed=settings_emb, view=None)


class GreetingSetup(discord.ui.Modal):
    def __init__(self, swd: commands.Bot, channel_id, status, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.swd = swd
        self.channel_id = channel_id
        self.status = status

    w_message = discord.ui.TextInput(
        label='Your welcome message goes here:',
        placeholder='Welcome message',
        style=discord.TextStyle.long,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        ss.swd_setup('greetings', interaction.guild.id, self.channel_id, self.status, self.w_message.value)
        setup_emb = discord.Embed(title='[Settings saved]', colour=sp.get_color("idle"))
        setup_emb.add_field(
            name=f'▶Channel https://discord.com/channels/{interaction.guild.id}/{self.channel_id} will now be used for welcoming new members in {interaction.guild.name}!',
            value=f'➾ **-** More information in /settings',
            inline=False)
        await interaction.response.edit_message(embed=setup_emb, view=None)

class GreetingSetupButton(discord.ui.View):
    def __init__(self, swd: commands.Bot, channel_id, status):
        super().__init__(timeout=None)
        self.swd = swd
        self.channel_id = channel_id
        self.status = status

    @discord.ui.button(label="Setup", custom_id='setup', row=0, style=discord.ButtonStyle.green)
    async def greeting_button(self, interaction, button):
        modal = GreetingSetup(title='Welcome message!', swd=self.swd, channel_id=self.channel_id, status=self.status)
        await interaction.response.send_modal(modal)


class SWDSetup(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "swd_setup", current)

    @app_commands.command(name='setup', description='-')
    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.checks.cooldown(1, 2)
    async def setup(self, interaction: discord.Interaction):
        settings_emb = discord.Embed(title=f'[{ss.running_bar(8, 1)}]', colour=sp.get_color("idle"))
        settings_emb.add_field(name='▶Setup:',
                               value='➾ **-** Setting channel to receive logs\n➾ **-** Use /settings to view current active modules\n➾ **-** /logs will help you configuring this module later',
                               inline=False)
        settings_emb.add_field(name='▶Managing logs',
                               value="➾ **-** [All] status means that bot notifies you on members leaving/joining your community, messages being deleted/edited\n➾ **-** Use [messages] status to receive messages being deleted/edited logs only\n➾ **-** Use [Users] to know about members joining/leaving your community",
                               inline=False)
        await interaction.response.send_message(embed=settings_emb, view=SecondStage(swd=self.swd))

    @app_commands.command(name='logs', description='-')
    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.checks.cooldown(1, 2)
    @app_commands.choices(status=[
        app_commands.Choice(name='all', value='all'),
        app_commands.Choice(name='users', value='users'),
        app_commands.Choice(name='messages', value='messages'),
    ])
    async def logs(self, interaction: discord.Interaction, channel: discord.TextChannel, status: app_commands.Choice[str]):
        check = ss.swd_pull(interaction.guild.id, 'logs')
        if check.get("channel_id") == "none":
            setup_emb = discord.Embed(title='[Setup has not been run to satisfy logs module]', colour=sp.get_color("warning"))
            setup_emb.add_field(name=f'▶Please run /setup in order to configure settings for {interaction.guild.name}!',
                                value='➾ **-** This command requires existing server settings which were not found.',
                                inline=False)
        else:
            ss.swd_setup('logs', interaction.guild.id, channel.id, status.name)
            setup_emb = discord.Embed(title='[Settings saved]', colour=sp.get_color("idle"))
            setup_emb.add_field(name=f'▶Channel {channel} will now show logs for {interaction.guild.name}!',
                                value=f'➾ **-** Logs type: {type} | logs state: {status.name}\n➾ **-** More information in /settings',
                                inline=False)
            roulette = random.randint(0, 100)
            if roulette < 50:
                setup_emb.set_footer(text='You got a happy dragon! 50% chance of getting one :3', icon_url='')
            elif roulette < 30:
                setup_emb.set_footer(text='You got a blushy dragon! 30% chance of getting one :3', icon_url='')
            elif roulette < 10:
                setup_emb.set_footer(text='Cool dragon! 10% chance of getting one :3', icon_url='')
        await interaction.response.send_message(embed=setup_emb)

    @app_commands.command(name='tod', description='-')
    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.checks.cooldown(1, 2)
    @app_commands.choices(status=[
        app_commands.Choice(name='on', value='on'),
        app_commands.Choice(name='off', value='off'),
    ])
    async def tod(self, interaction: discord.Interaction, channel: discord.TextChannel, status: app_commands.Choice[str]):
        check = ss.swd_pull(interaction.guild.id, 'tod')
        if check.get("channel_id") == "none":
            setup_emb = discord.Embed(title='[Setup has not been run to satisfy truth or dare module]',
                                      colour=sp.get_color("warning"))
            setup_emb.add_field(name=f'▶Please run /setup in order to configure settings for {interaction.guild.name}!',
                                value='➾ **-** This command requires existing server settings which were not found.',
                                inline=False)
        else:
            ss.swd_setup('tod', interaction.guild.id, channel.id, status.name)
            setup_emb = discord.Embed(title='[Settings saved]', colour=sp.get_color("idle"))
            setup_emb.add_field(
                name=f'▶Channel {channel} will now be used for Truth or Dare game in {interaction.guild.name}!',
                value='➾ **-** More information in /settings',
                inline=False)
            roulette = random.randint(0, 100)
            if roulette < 50:
                setup_emb.set_footer(text='You got a happy dragon! 50% chance of getting one :3', icon_url='')
            elif roulette < 30:
                setup_emb.set_footer(text='You got a blushy dragon! 30% chance of getting one :3', icon_url='')
            elif roulette < 10:
                setup_emb.set_footer(text='Cool dragon! 10% chance of getting one :3', icon_url='')
        await interaction.response.send_message(embed=setup_emb)

    @app_commands.command(name='gchat', description='-')
    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.checks.cooldown(1, 2)
    @app_commands.choices(status=[
        app_commands.Choice(name='on', value='on'),
        app_commands.Choice(name='off', value='off'),
    ])
    async def gchat(self, interaction: discord.Interaction, channel: discord.TextChannel, status: app_commands.Choice[str]):
        check = ss.swd_pull(interaction.guild.id, 'gchat')
        if check.get("channel_id") == "none":
            setup_emb = discord.Embed(title='[Setup has not been run to satisfy gchat module]', colour=sp.get_color("warning"))
            setup_emb.add_field(name=f'▶Please run /setup in order to configure settings for {interaction.guild.name}!',
                                value='➾ **-** This command requires existing server settings which were not found.',
                                inline=False)
        else:
            ss.swd_setup('gchat', interaction.guild.id, channel.id, status.name)
            setup_emb = discord.Embed(title='[Settings saved]', colour=sp.get_color("idle"))
            setup_emb.add_field(name=f'▶Channel {channel} will now be used for global chat in {interaction.guild.name}!',
                                value=f'➾ **-** State: {status.name}\n➾ **-** More information in /settings',
                                inline=False)
            await channel.edit(slowmode_delay=5)
            roulette = random.randint(0, 100)
            if roulette < 50:
                setup_emb.set_footer(text='You got a happy dragon! 50% chance of getting one :3', icon_url='')
            elif roulette < 30:
                setup_emb.set_footer(text='You got a blushy dragon! 30% chance of getting one :3', icon_url='')
            elif roulette < 10:
                setup_emb.set_footer(text='Cool dragon! 10% chance of getting one :3', icon_url='')
        await interaction.response.send_message(embed=setup_emb)

    @app_commands.command(name='chat', description='-')
    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.checks.cooldown(1, 2)
    @app_commands.choices(status=[
        app_commands.Choice(name='on', value='on'),
        app_commands.Choice(name='off', value='off'),
    ])
    async def chat(self, interaction: discord.Interaction, channel: discord.TextChannel, status: app_commands.Choice[str]):
        check = ss.swd_pull(interaction.guild.id, 'chat')
        if check.get("channel_id") == "none":
            setup_emb = discord.Embed(title='[Setup has not been run to satisfy chat module]',
                                      colour=sp.get_color("warning"))
            setup_emb.add_field(name=f'▶Please run /setup in order to configure settings for {interaction.guild.name}!',
                                value='➾ **-** This command requires existing server settings which were not found.',
                                inline=False)
        else:
            ss.swd_setup('chat', interaction.guild.id, channel.id, status.name)
            setup_emb = discord.Embed(title='[Settings saved]', colour=sp.get_color("idle"))
            setup_emb.add_field(name=f'▶Channel {channel} will now be used for chat with Swifty AI in {interaction.guild.name}!',
                                value=f'➾ **-** State: {status.name}\n➾ **-** More information in /settings',
                                inline=False)
            await channel.edit(slowmode_delay=5)
            roulette = random.randint(0, 100)
            if roulette < 50:
                setup_emb.set_footer(text='You got a happy dragon! 50% chance of getting one :3', icon_url='')
            elif roulette < 30:
                setup_emb.set_footer(text='You got a blushy dragon! 30% chance of getting one :3', icon_url='')
            elif roulette < 10:
                setup_emb.set_footer(text='Cool dragon! 10% chance of getting one :3', icon_url='')
        await interaction.response.send_message(embed=setup_emb)

    @app_commands.command(name='greeting', description='-')
    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.checks.cooldown(1, 2)
    @app_commands.choices(status=[
        app_commands.Choice(name='on', value='on'),
        app_commands.Choice(name='off', value='off'),
    ])
    async def greeting(self, interaction: discord.Interaction, channel: discord.TextChannel, status: app_commands.Choice[str]):
        check = ss.swd_pull(interaction.guild.id, 'greetings')
        if check.get("channel_id") == "none":
            setup_emb = discord.Embed(title='[Setup has not been run to satisfy greetings module]',
                                      colour=sp.get_color("warning"))
            setup_emb.add_field(name=f'▶Please run /setup in order to configure settings for {interaction.guild.name}!',
                                value='➾ **-** This command requires existing server settings which were not found.',
                                inline=False)
            await interaction.response.send_message(embed=setup_emb)
        else:
            self.swd.add_view(GreetingSetupButton(swd=self.swd, channel_id=channel.id, status=status.name))
            setup_emb = discord.Embed(title='[Set welcome message!]', colour=sp.get_color("idle"))
            setup_emb.add_field(name=f'▶Utilities:',
                                   value=f'➾ <member> **-** metions member.\n➾ **-** you can use **your message**, ~~your message~~, _your message_ or ```your message`` freely!.',
                                   inline=False)
            roulette = random.randint(0, 100)
            if roulette < 50:
                setup_emb.set_footer(text='You got a happy dragon! 50% chance of getting one :3', icon_url='')
            elif roulette < 30:
                setup_emb.set_footer(text='You got a blushy dragon! 30% chance of getting one :3', icon_url='')
            elif roulette < 10:
                setup_emb.set_footer(text='Cool dragon! 10% chance of getting one :3', icon_url='')
            await interaction.response.send_message(embed=setup_emb, view=GreetingSetupButton(swd=self.swd, channel_id=channel.id, status=status))

    @app_commands.command(name='artshare', description='-')
    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.checks.cooldown(1, 2)
    @app_commands.choices(status=[
        app_commands.Choice(name='on', value='on'),
        app_commands.Choice(name='off', value='off'),
    ])
    async def artshare(self, interaction: discord.Interaction, channel: discord.TextChannel, status: app_commands.Choice[str]):
        check = ss.swd_pull(interaction.guild.id, 'artshare')
        if check.get("channel_id") == "none":
            setup_emb = discord.Embed(title='[Setup has not been run to satisfy artshare module]',
                                      colour=sp.get_color("warning"))
            setup_emb.add_field(name=f'▶Please run /setup in order to configure settings for {interaction.guild.name}!',
                                value='➾ **-** This command requires existing server settings which were not found.',
                                inline=False)
        else:
            ss.swd_setup('artshare', interaction.guild.id, channel.id, status.name)
            setup_emb = discord.Embed(title='[Settings saved]', colour=sp.get_color("idle"))
            setup_emb.add_field(
                name=f'▶Channel {channel} will now be used for artshare in {interaction.guild.name}!',
                value=f'➾ **-** State: {status.name}\n➾ **-** More information in /settings',
                inline=False)
            await channel.edit(slowmode_delay=5)
            roulette = random.randint(0, 100)
            if roulette < 50:
                setup_emb.set_footer(text='You got a happy dragon! 50% chance of getting one :3', icon_url='')
            elif roulette < 30:
                setup_emb.set_footer(text='You got a blushy dragon! 30% chance of getting one :3', icon_url='')
            elif roulette < 10:
                setup_emb.set_footer(text='Cool dragon! 10% chance of getting one :3', icon_url='')
        await interaction.response.send_message(embed=setup_emb)

    @app_commands.command(name='settings', description='-')
    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.checks.cooldown(1, 2)
    async def settings(self, interaction: discord.Interaction):
        logs = ss.swd_pull(interaction.guild.id, 'logs')
        gchat = ss.swd_pull(interaction.guild.id, 'gchat')
        tod = ss.swd_pull(interaction.guild.id, 'tod')
        chat = ss.swd_pull(interaction.guild.id, 'chat')
        greetings = ss.swd_pull(interaction.guild.id, 'greetings')
        artshare = ss.swd_pull(interaction.guild.id, 'artshare')
        setup_emb = discord.Embed(title=f'[Settings for {interaction.guild.name}]', colour=sp.get_color("idle"))
        setup_emb.add_field(name='▶Server logs',
                               value=f"➾ **-** Channel: {ss.swd_channel_modify(logs.get('channel_id'), interaction.guild.id)} | status: {logs.get('status')}",
                               inline=False)
        setup_emb.add_field(name='▶Global chat',
                               value=f"➾ **-** Channel: {ss.swd_channel_modify(gchat.get('channel_id'), interaction.guild.id)} | status: {gchat.get('status')}",
                               inline=False)
        setup_emb.add_field(name='▶Truth or Dare',
                               value=f"➾ **-** Channel: {ss.swd_channel_modify(tod.get('channel_id'), interaction.guild.id)} | status: {tod.get('status')}",
                               inline=False)
        setup_emb.add_field(name='▶Swifty AI chat',
                            value=f"➾ **-** Channel: {ss.swd_channel_modify(chat.get('channel_id'), interaction.guild.id)} | status: {chat.get('status')}",
                            inline=False)
        setup_emb.add_field(name='▶Greeting',
                            value=f"➾ **-** Channel: {ss.swd_channel_modify(greetings.get('channel_id'), interaction.guild.id)} | status: {greetings.get('status')}\nMessage:\n```{greetings.get('message')}```",
                            inline=False)
        setup_emb.add_field(name='▶Artshare',
                            value=f"➾ **-** Channel: {ss.swd_channel_modify(artshare.get('channel_id'), interaction.guild.id)} | status: {artshare.get('status')}",
                            inline=False)
        roulette = random.randint(0, 100)
        if roulette < 50:
            setup_emb.set_footer(text='You got a happy dragon! 50% chance of getting one :3', icon_url='')
        elif roulette < 30:
            setup_emb.set_footer(text='You got a blushy dragon! 30% chance of getting one :3', icon_url='')
        elif roulette < 10:
            setup_emb.set_footer(text='Cool dragon! 10% chance of getting one :3', icon_url='')
        await interaction.response.send_message(embed=setup_emb)

    @commands.Cog.listener()
    async def on_ready(self):
        self.swd.add_view(SecondStage(swd=self.swd))
        self.swd.add_view(ThirdStage(swd=self.swd))
        self.swd.add_view(FourthStage(swd=self.swd))
        self.swd.add_view(FifthStage(swd=self.swd))
        self.swd.add_view(SixthStage(swd=self.swd))
        self.swd.add_view(SeventhStage(swd=self.swd))


async def setup(swd):
    await swd.add_cog(SWDSetup(swd))