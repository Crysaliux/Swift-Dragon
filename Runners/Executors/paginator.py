import discord
from discord.ext import commands


class Pagination(discord.ui.View):
    def __init__(self, interaction: discord.Interaction, *args):
        super().__init__(timeout=None)
        self.page = 0
        self.total = 0
        self.embeds = []
        self.interaction = interaction
        for emb in args:
            self.total += 1
            self.embeds.append(emb.to_dict())

    async def paginator_start(self):
        self.previous.disabled = True
        self.next.disabled = False
        self.middle.label = f"1//{self.total}"
        self.middle.disabled = True
        page_emb = discord.Embed.from_dict(self.embeds[0])
        await self.interaction.response.send_message(embed=page_emb, view=self)

    async def paginator_call(self, interaction: discord.Interaction):
        page_emb = discord.Embed.from_dict(self.embeds[self.page])
        self.middle.label = f"{self.page + 1}//{self.total}"
        if self.page == 0:
            self.previous.disabled = True
            self.next.disabled = False
        if self.page + 1 == self.total:
            self.previous.disabled = False
            self.next.disabled = True
        if self.page > 0 and self.page + 1 != self.total:
            self.previous.disabled = False
            self.next.disabled = False
        await interaction.response.edit_message(embed=page_emb, view=self)

    @discord.ui.button(label="◀", style=discord.ButtonStyle.green, custom_id='1')
    async def previous(self, interaction: discord.Interaction, button):
        self.page -= 1
        await self.paginator_call(interaction)

    @discord.ui.button(label="//", style=discord.ButtonStyle.gray, custom_id='2')
    async def middle(self, interaction: discord.Interaction, button):
        pass

    @discord.ui.button(label="▶", style=discord.ButtonStyle.green, custom_id='3')
    async def next(self, interaction: discord.Interaction, button):
        self.page += 1
        await self.paginator_call(interaction)
