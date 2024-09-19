import discord

class Choose(discord.ui.View):
    def __init__(self, links, count):
        super().__init__(timeout=None)
        self.links = links
        self.count = count

    @discord.ui.button(label="First image", custom_id='1-image', row=0, style=discord.ButtonStyle.green)
    async def first_button_callback(self, button, interaction):
        await interaction.response.send_message(self.links[0])

    @discord.ui.button(label="Second image", custom_id='2-image', row=0, style=discord.ButtonStyle.green)
    async def second_button_callback(self, button, interaction):
        if self.count >= 2:
            await interaction.response.send_message(self.links[1])
        else:
            button.disabled = True
            button.label = "No image!"

    @discord.ui.button(label="Third image", custom_id='3-image', row=1, style=discord.ButtonStyle.green)
    async def third_button_callback(self, button, interaction):
        if self.count >= 3:
            await interaction.response.send_message(self.links[2])
        else:
            button.disabled = True
            button.label = "No image!"

    @discord.ui.button(label="Fourth image", custom_id='4-image', row=1, style=discord.ButtonStyle.green)
    async def fourth_button_callback(self, button, interaction):
        if self.count > 3:
            await interaction.response.send_message(self.links[3])
        else:
            button.disabled = True
            button.label = "No image!"