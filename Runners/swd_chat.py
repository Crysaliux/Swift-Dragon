import discord
from discord.ext import commands
from datetime import datetime
import random
import sys
sys.path.append("Runners/Executors")
from dataexecutor import Swdswift_chat, Swdmain_settings
from console import Swdconsole_logs, returns
from colormanager import Swdcolor_picker
from aimanager import client, swift_ai

sc = Swdswift_chat()
con_logs = Swdconsole_logs()
sp = Swdcolor_picker()
ss = Swdmain_settings()


model = swift_ai.model

class NewChar(discord.ui.Modal):
    def __init__(self, user_id, name, prefix, aurl, *args, **kwargs) -> None:
        self.user_id = user_id
        self.name = name
        self.prefix = prefix
        self.aurl = aurl
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="How would you describe your character?", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        sc.character_create(self.user_id, self.name, self.prefix, self.aurl, self.children[0].value)
        swift_emb = discord.Embed(title='[Character Created!]', colour=sp.get_color("idle"))
        swift_emb.add_field(
            name=f'▶Your character, {self.name} has been successfully created!',
            value=f'➾ **-** Prefix: {self.prefix}\n➾ **-** Description: ```{self.children[0].value}```',
            inline=False)
        await interaction.response.send_message(embed=swift_emb)


class SWDChat(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "swd_chat", current)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            pass
        else:
            guild = message.guild
            if not guild:
                pass
            else:
                chat = ss.swd_pull(message.guild.id, 'chat')
                if chat.get("channel_id") == "none":
                    pass
                else:
                    if chat.get("channel_id") != message.channel.id:
                        pass
                    else:
                        if chat.get("status") == "off":
                            pass
                        else:
                            prefix = message.content.split(' ')[0]
                            check = sc.character_check(message.author.id, prefix)
                            if check == returns.not_found:
                                pass
                            else:
                                await sc.character_reply(message, sc, check.get("prefix"), check.get("prompt"), check.get("name"), check.get("avatar"), message.content[len(prefix):], client, model, 1, 500)

    @commands.slash_command(name='clear_history', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def clear_history(self, ctx, prefix: str):
        await ctx.response.defer()
        if len(prefix) > 4:
            await con_logs.command_warning('040', ctx)
        else:
            sc.delete_history(ctx.author.id, prefix)
            swift_emb = discord.Embed(title='[History Cleared]', colour=sp.get_color("idle"))
            swift_emb.add_field(name=f'▶Chat history has been cleared. Interacting with characters:',
                                value=f'➾ **-** Create a character to chat with them!\n➾ **-** [their prefix] [your message] - to chat in the server!',
                                inline=False)
            await ctx.respond(embed=swift_emb)

    @commands.slash_command(name='delete_character', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def delete_character(self, ctx, prefix: str):
        await ctx.response.defer()
        if len(prefix) > 4:
            await con_logs.command_warning('040', ctx)
        else:
            check = sc.character_check(ctx.author.id, prefix)
            if check != returns.not_found:
                sc.character_delete(ctx.author.id, prefix)
                swift_emb = discord.Embed(title='[Character Deleted]', colour=sp.get_color("idle"))
                swift_emb.add_field(name=f'▶Character {check.get("name")}, has been deleted. Interacting with characters:',
                                    value=f'➾ **-** Create a character to chat with them!\n➾ **-** [their prefix] [your message] - to chat in the server!',
                                    inline=False)
                await ctx.respond(embed=swift_emb)
            else:
                await con_logs.command_warning('1300', ctx)

    @commands.slash_command(name='create_character', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def create_character(self, ctx, name: str, prefix: str, avatar_url):
        if len(name) > 20:
            swift_emb = discord.Embed(title='[Name Length Limit!]', colour=sp.get_color("warning"))
            swift_emb.add_field(name=f'▶Character name must be less that 20 letters long!',
                                value=f'➾ **-** {len(name)} > 20!',
                                inline=False)
            await ctx.respond(embed=swift_emb, ephemeral=True)

        elif len(prefix) > 4:
            swift_emb = discord.Embed(title='[Prefix Length Limit!]', colour=sp.get_color("warning"))
            swift_emb.add_field(name=f'▶Character prefix must not be longer than 4 letters!',
                                value=f'➾ **-** {len(name)} > 5!',
                                inline=False)
            await ctx.respond(embed=swift_emb, ephemeral=True)

        else:
            if "https://" in avatar_url:
                modal = NewChar(title='Character description!', name=name, prefix=prefix, aurl=avatar_url, user_id=ctx.author.id)
                await ctx.send_modal(modal)
            else:
                swift_emb = discord.Embed(title='[Invalid Url!]', colour=sp.get_color("warning"))
                swift_emb.add_field(name=f'▶Your url seems to be invalid, please try again!',
                                    value=f'➾ **-** {avatar_url}!',
                                    inline=False)
                await ctx.respond(embed=swift_emb, ephemeral=True)

    @commands.slash_command(name='characters', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def characters(self, ctx):
        await ctx.response.defer()
        check = sc.get_characters(ctx.author.id)
        if check != returns.not_found:
            swift_emb = discord.Embed(title=f'[Your characters, {ctx.author.name}!]', colour=sp.get_color("idle"))
            for character in check:
                swift_emb.add_field(name=f"▶{character.get('name')}",
                                    value=f"➾ **-** Avatar: [{character.get('name')}'s avatar]({character.get('avatar')}) | prefix: {character.get('prefix')}\nDescription:\n```{character.get('prompt')}```",
                                    inline=False)
            roulette = random.randint(0, 100)
            if roulette < 50:
                swift_emb.set_footer(text='You got a happy dragon! 50% chance of getting one :3', icon_url='')
            elif roulette < 30:
                swift_emb.set_footer(text='You got a blushy dragon! 30% chance of getting one :3', icon_url='')
            elif roulette < 10:
                swift_emb.set_footer(text='Cool dragon! 10% chance of getting one :3', icon_url='')
            await ctx.respond(embed=swift_emb)
        else:
            swift_emb = discord.Embed(title='[No characters found]', colour=sp.get_color("warning"))
            swift_emb.add_field(name=f'▶Please run /character_create in order to create your first character!',
                                value='➾ **-** This command requires existing character models which were not found.',
                                inline=False)
            await ctx.respond(embed=swift_emb, ephemeral=True)


def setup(swd):
    swd.add_cog(SWDChat(swd))