import discord
from discord.ext import commands
import asyncio
from peewee import *
from threading import Timer
from Runners.Executors.dataexecutor import Swdmain_settings, Swdaddons_local
from Runners.Executors.console import Swdconsole_logs

sl = Swdaddons_local()
err_logs = Swdconsole_logs


class Voting(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.select(
        placeholder = "Vote here",
        custom_id= 'voting',
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="✅",
                description="-"
            ),
            discord.SelectOption(
                label="❌",
                description="-"
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == '✅':
            check = sl.save_vote(int(interaction.user.id), int(interaction.message.id), 'for')
            if check == 'error':
                warning_emb = discord.Embed(title='[Have Already Voted!]', colour=0xe91e63)
                warning_emb.add_field(name='▶It seems you have already voted, Senator',
                                      value=f'➾ Voting goes for **-** 24 hours',
                                      inline=False)
                await interaction.response.send_message(embed=warning_emb, ephemeral=True)
            else:
                await interaction.response.defer()

        elif select.values[0] == '❌':
            check = sl.save_vote(int(interaction.user.id), int(interaction.message.id), 'against')
            if check == 'error':
                warning_emb = discord.Embed(title='[Have Already Voted!]', colour=0xe91e63)
                warning_emb.add_field(name='▶It seems you have already voted, Senator',
                                      value=f'➾ Voting goes for **-** 24 hours',
                                      inline=False)
                await interaction.response.send_message(embed=warning_emb, ephemeral=True)
            else:
                await interaction.response.defer()

class Senator_choice(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Call a Vote", custom_id='vote-button', row=0, style=discord.ButtonStyle.green)
    async def first_button_callback(self, button, interaction):
        tae_emb = discord.Embed(title='What will be your next choice, Senator', colour=0xe91e63)
        await interaction.response.edit_message(embed=tae_emb, view=Select())

class SWDTAE_local(commands.Cog):
    def __init__(self, swd):
        self.swd = swd

    @commands.slash_command(name='console_tab', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def console_tab(self, ctx):
        if ctx.guild.id != 1172162501979406408:
            await err_logs.command_warning('030', ctx)
        else:
            role = ctx.guild.get_role(1184031650963804212)
            if role not in ctx.author.roles:
                await err_logs.command_warning('030', ctx)
            else:
                rolelist = [r.mention for r in ctx.author.roles if r != ctx.guild.default_role]
                user_roles = ", ".join(rolelist)

                role = discord.utils.find(lambda r: r.name == 'support', ctx.guild.roles)
                if role in ctx.author.roles:
                    duties = 'Support'
                    description = 'Supporters are those who are involved in TAE life and are always ready to help!'
                else:
                    role = discord.utils.find(lambda r: r.name == 'administrator', ctx.guild.roles)
                    if role in ctx.author.roles:
                        duties = 'Administrator'
                        description = 'Administrators are the ones to keep this nice server a thing and coordinate work of others!'
                    else:
                        duties = 'Moderator'
                        description = 'Moderators are our security and protection, restless fighters against scammers and keepers of the inner safety!'

                tae_emb = discord.Embed(title=f'Welcome aboard, Senator. What will be your decision?', colour=0xe91e63)
                tae_emb.add_field(name='Your Identification:',
                                  value=f'➾ **-** {ctx.author.name}\n➾ **-**  Discord ID: {ctx.author.id}',
                                  inline=False)
                tae_emb.add_field(name='Your Permissions, Senator:', value=f'➾ **-** {user_roles}', inline=False)
                tae_emb.add_field(name='Your Duties:', value=f'➾ **-** {duties}\n➾ **-** {description}', inline=False)
                await ctx.respond(embed=tae_emb)

    @commands.slash_command(name='vote', description='-')
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def vote(self, ctx, member: discord.Member, time_in_seconds: int):
        if ctx.guild.id != 1172162501979406408:
            await err_logs.command_warning('030', ctx)
        else:
            role = ctx.guild.get_role(1184031650963804212)
            if role not in ctx.author.roles:
                await err_logs.command_warning('030', ctx)
            else:
                sl.clear_data(member)
                channel = self.swd.get_channel(1198265993944911872)
                staff_role = ctx.guild.get_role(1198266478424772728)

                tae_emb = discord.Embed(
                    title=f'{ctx.author.name} believe {member.name} should be accepted as a new Senator',
                    colour=0xe91e63)
                tae_emb.add_field(name='Vote for or against:', value=f'➾ **-** ✅\n➾ **-** ❌\n{staff_role.mention}', inline=False)
                message = await channel.send(embed=tae_emb, view=Voting())
                sl.save_elected(member.id, message.id)

                tae_emb = discord.Embed(title=f'The vote has started, Senator!', colour=0xe91e63)
                tae_emb.add_field(name='Vote here:',
                                  value='➾ **-** https://discord.com/channels/1172162501979406408/1198265993944911872',
                                  inline=False)
                await ctx.response.defer()
                await sl.run_function(ctx, member, time_in_seconds)

    @commands.Cog.listener()
    async def on_ready(self):
        self.swd.add_view(Senator_choice())
        self.swd.add_view(Voting())


def setup(swd):
    swd.add_cog(SWDTAE_local(swd))