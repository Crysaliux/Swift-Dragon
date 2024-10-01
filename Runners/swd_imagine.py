import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime


from Runners.Executors.dataexecutor import Swdswift_imagine
from Runners.Executors.console import Swdconsole_logs, returns
from Runners.Executors.colormanager import Swdcolor_picker


si = Swdswift_imagine()
con_logs = Swdconsole_logs()
sp = Swdcolor_picker()


class SWDImagine(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "swd_imagine", current)

    @app_commands.command(name='imagine', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def imagine(self, interaction: discord.Interaction, prompt: str):
        await interaction.response.send_message("This command is currently unavailable.")

        #check = si.queue_save(interaction.user.id, interaction.channel.id, prompt)
        #if check == returns.exists:
            #process_emb = discord.Embed(title='[Still In Queue!]', colour=sp.get_color("warning"))
            #process_emb.add_field(
                #name=f"▶It seems your request is still in queue, you can't have several requests at once!",
                #value=f"➾ **-** Swifty will remind you when generation is ready, remember that prompts must be SFW!\n➾ **-** Join our community to get Swifty updates: https://discord.gg/FpYas3s2Fp",
                #inline=False)
        #else:
            #process_emb = discord.Embed(title='[Waiting In Queue...]', colour=sp.get_color("idle"))
            #process_emb.add_field(
                #name=f"▶Place in global queue: [{check}]",
                #value=f"➾ **-** Swifty will remind you when generation is ready, remember that prompts must be SFW!\n➾ **-** Join our community to get Swifty updates: https://discord.gg/FpYas3s2Fp",
                #inline=False)
        #await interaction.response.send_message(embed=process_emb)
        #await si.generate_image(self.swd, interaction.user.id)


async def setup(swd):
    await swd.add_cog(SWDImagine(swd))