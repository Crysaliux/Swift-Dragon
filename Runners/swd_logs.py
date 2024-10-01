import discord
from discord.ext import commands
import asyncio
from datetime import datetime


from Runners.Executors.dataexecutor import Swdmain_settings
from Runners.Executors.console import Swdconsole_logs
from Runners.Executors.colormanager import Swdcolor_picker

ss = Swdmain_settings()
con_logs = Swdconsole_logs()
sp = Swdcolor_picker()


class SWDLogs(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "swd_logs", current)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        logs = ss.swd_pull(member.guild.id, 'logs')
        log_channel = self.swd.get_channel(logs.get("channel_id"))
        log_type = logs.get("status")
        if log_type == "off":
            pass
        else:
            if log_type == "all":
                join_emb = discord.Embed(title='[New user has joined]', colour=sp.get_color("idle"))
                join_emb.add_field(name=f'▶User name: {member.name}', value=f'➾ **-** Uid: {member.id}\n➾ **-** Status: {member.status}\n➾ **-** Joined discord: {member.joined_at.strftime("%b %d, %Y, %T")}', inline=False)
                await log_channel.send(embed=join_emb)
            elif log_type == "users":
                join_emb = discord.Embed(title='[New user has joined]', colour=sp.get_color("idle"))
                join_emb.add_field(name=f'▶User name: {member.name}', value=f'➾ **-** Uid: {member.id}\n➾ **-** Status: {member.status}\n➾ **-** Joined discord: {member.joined_at.strftime("%b %d, %Y, %T")}', inline=False)
                await log_channel.send(embed=join_emb)
            elif log_type == "messages":
                pass
        await asyncio.sleep(2)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        logs = ss.swd_pull(member.guild.id, 'logs')
        log_channel = self.swd.get_channel(logs.get("channel_id"))
        log_type = logs.get("status")
        if log_type == "off":
            pass
        else:
            if log_type == "all":
                join_emb = discord.Embed(title='[User has left]', colour=sp.get_color("idle"))
                join_emb.add_field(name=f'▶User name: {member.name}',
                                   value=f'➾ **-** Uid: {member.id}\n➾ **-** Status: {member.status}\n➾ **-** Joined discord: {member.joined_at.strftime("%b %d, %Y, %T")}',
                                   inline=False)
                await log_channel.send(embed=join_emb)
            elif log_type == "users":
                join_emb = discord.Embed(title='[User has left]', colour=sp.get_color("idle"))
                join_emb.add_field(name=f'▶User name: {member.name}',
                                   value=f'➾ **-** Uid: {member.id}\n➾ **-** Status: {member.status}\n➾ **-** Joined discord: {member.joined_at.strftime("%b %d, %Y, %T")}',
                                   inline=False)
                await log_channel.send(embed=join_emb)
            elif log_type == "messages":
                pass
        await asyncio.sleep(2)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot:
            pass
        else:
            logs = ss.swd_pull(after.guild.id, 'logs')
            log_channel = self.swd.get_channel(logs.get("channel_id"))
            log_type = logs.get("status")
            if log_type == "off":
                pass
            else:
                if log_type == "all":
                    join_emb = discord.Embed(title='[Message has been edited]', colour=sp.get_color("idle"))
                    join_emb.add_field(
                        name=f'▶Message: https://discord.com/channels/{after.guild.id}/{after.channel.id}/{after.id}',
                        value=f'➾ **-** Id: {after.id}\n➾ **-** Before: ```{before.content}```\n➾ **-** After: ```{after.content}```',
                        inline=False)
                    await log_channel.send(embed=join_emb)
                elif log_type == "users":
                    pass
                elif log_type == "messages":
                    join_emb = discord.Embed(title='[Message has been edited]', colour=sp.get_color("idle"))
                    join_emb.add_field(
                        name=f'▶Message: https://discord.com/channels/{after.guild.id}/{after.channel.id}/{after.id}',
                        value=f'➾ **-** Id: {after.id}\n➾ **-** Before: ```{before.content}```\n➾ **-** After: ```{after.content}```',
                        inline=False)
                    await log_channel.send(embed=join_emb)
        await asyncio.sleep(2)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            pass
        else:
            logs = ss.swd_pull(message.guild.id, 'logs')
            log_channel = self.swd.get_channel(logs.get("channel_id"))
            log_type = logs.get("status")
            if log_type == "off":
                pass
            else:
                if log_type == "all":
                    log_emb = discord.Embed(title='[Message has been deleted]', colour=sp.get_color("idle"))
                    log_emb.add_field(
                        name=f'▶Message: -deleted-',
                        value=f'➾ **-** Id: {message.id}\n➾ **-** Content: ```{message.content}```',
                        inline=False)
                    await log_channel.send(embed=log_emb)
                elif log_type == "users":
                    pass
                elif log_type == "messages":
                    log_emb = discord.Embed(title='[Message has been deleted]', colour=sp.get_color("idle"))
                    log_emb.add_field(
                        name=f'▶Message: -deleted-',
                        value=f'➾ **-** Id: {message.id}\n➾ **-** Content: ```{message.content}```',
                        inline=False)
                    await log_channel.send(embed=log_emb)
        await asyncio.sleep(2)


async def setup(swd):
    await swd.add_cog(SWDLogs(swd))