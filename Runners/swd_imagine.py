import discord
from discord.ext import commands, tasks
from discord import app_commands
from datetime import datetime
import threading
import asyncio
from queue import Queue


from Runners.Executors.dataexecutor import Swdswift_imagine
from Runners.Executors.console import Swdconsole_logs, returns
from Runners.Executors.colormanager import Swdcolor_picker


q = Queue()
si = Swdswift_imagine()
con_logs = Swdconsole_logs()
sp = Swdcolor_picker()


class Choose(discord.ui.View):
    def __init__(self, links, count):
        super().__init__(timeout=None)
        self.links = links
        self.count = count

    @discord.ui.button(label="First image", custom_id='1-image', row=0, style=discord.ButtonStyle.green)
    async def first_button_callback(self, interaction, button):
        await interaction.response.send_message(self.links[0])

    @discord.ui.button(label="Second image", custom_id='2-image', row=0, style=discord.ButtonStyle.green)
    async def second_button_callback(self, interaction, button):
        if self.count >= 2:
            await interaction.response.send_message(self.links[1])
        else:
            button.disabled = True
            button.label = "No image!"

    @discord.ui.button(label="Third image", custom_id='3-image', row=1, style=discord.ButtonStyle.green)
    async def third_button_callback(self, interaction, button):
        if self.count >= 3:
            await interaction.response.send_message(self.links[2])
        else:
            button.disabled = True
            button.label = "No image!"

    @discord.ui.button(label="Fourth image", custom_id='4-image', row=1, style=discord.ButtonStyle.green)
    async def fourth_button_callback(self, interaction, button):
        if self.count > 3:
            await interaction.response.send_message(self.links[3])
        else:
            button.disabled = True
            button.label = "No image!"


class SWDImagine(commands.Cog):
    def __init__(self, swd):
        self.swd = swd
        current = datetime.today().strftime('%Y-%m-%d')
        con_logs.logs('001', "swd_imagine", current)
        loop = asyncio.new_event_loop()
        self.parse.start(loop)
        self.channel = None
        self.call_back = None

        self.pull = si.bulk_pull()
        if self.pull != returns.not_found:
            for data in self.pull:
                q.put(data)

    @app_commands.command(name='imagine', description='-')
    @app_commands.checks.cooldown(1, 2)
    async def imagine(self, interaction: discord.Interaction, prompt: str):
        check = si.queue_save(interaction.user.id, interaction.channel.id, prompt)
        if check == returns.exists:
            process_emb = discord.Embed(title='[Still In Queue!]', colour=sp.get_color("warning"))
            process_emb.add_field(
                name=f"▶It seems your request is still in queue, you can't have several requests at once!",
                value=f"➾ **-** Swifty will remind you when generation is ready, remember that prompts must be SFW!\n➾ **-** Join our community to get Swifty updates: https://discord.gg/FpYas3s2Fp",
                inline=False)
        else:
            q.put([interaction.user.id, interaction.channel.id])
            process_emb = discord.Embed(title='[Waiting In Queue...]', colour=sp.get_color("idle"))
            process_emb.add_field(
                name=f"▶Approximate waiting time: [{20} seconds]",
                value=f"➾ **-** Swifty will remind you when generation is ready, remember that prompts must be SFW!\n➾ **-** Join our community to get Swifty updates: https://discord.gg/FpYas3s2Fp",
                inline=False)
        await interaction.response.send_message(embed=process_emb)


    @tasks.loop(seconds=20)
    async def parse(self, loop):
        try:
            def run_loop():
                waiter = q.get()
                get_data = loop.run_until_complete(si.generate_image(self.swd, waiter[0], loop))
                self.channel = self.swd.get_channel(waiter[1])
                self.call_back = get_data

            thread = threading.Thread(target=run_loop)
            thread.start()

            gen_emb = discord.Embed(title='[All Done!]', colour=0xe91e63)
            gen_emb.add_field(
                name=f"▶Images generated: [{self.call_back['count']}]",
                value=f"➾ **-** To select the best one use corresponding button below\n➾ **-** Join our community to get Swifty updates: https://discord.gg/FpYas3s2Fp",
                inline=False)
            gen_emb.set_image(url=self.call_back["image"])

           
            await self.channel.send(file=self.call_back["file"], embed=gen_emb, view=Choose(links=self.call_back["links"], count=self.call_back["count"]))
        except:
            pass


async def setup(swd):
    await swd.add_cog(SWDImagine(swd))