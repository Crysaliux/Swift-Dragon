from Runners.Executors.colormanager import Swdcolor_picker
import discord

sp = Swdcolor_picker()


class help_pages:
    first_page = discord.Embed(title="[General information]", colour=sp.get_color("idle"))
    first_page.add_field(name="▶About us:",
                         value="➾ **-** Swift Dragon is a project maintained by sevaral people. When using services this app provides, you **must** abide by our guidelines listed below. Please make yourself familiar with them before reading further!",
                         inline=False)
    first_page.add_field(name="▶Main Guidelines:",
                         value="➾ **-** General:\n[1] - Any media, links to media used by Swift Dragon **should not** be copied/spread without permission\n[2] - Users using any bugs/loopholes in bot's functionality without reporting them to dev team will be banned from using this app\n[3] - We do not tolerate any communities/members that support ||terrorism||, ||abuse||, ||suicidal topics||. Those will be instantly banned from using our app\n➾ **-** Artshare:\n[7] - Images containing ||gore|| or ||nsfw|| are not allowed\n[8] - Each art gets spoilered automatically, to avoid it being stolen. If this function decreases your art's quality in any way, please let us know here [Our official community](https://discord.gg/f9Q4YRPRwW)\n➾ **-** Global chat:\n[9] - No spamming is allowed (gifs flood, too many stickers, random text)\n[10] - Be kind and respectful to others\n[11] - Keep chat SFW. Global chat is being monitored by our AI security 24/7",
                         inline=False)
    first_page.add_field(name="▶AI Guidelines:",
                         value="➾ **-** Swift AI:\n[4] - Using Character models to impersonate, abuse or trick people is strictly prohibited\n[5] - We have right to remove Character models with inappropriate nicknames, avatars or description\n[6] - Keep your questions sfw!",
                         inline=False)

    second_page = discord.Embed(title="[Characters]", colour=sp.get_color("idle"))
    second_page.add_field(name="▶About Characters:",
                          value="➾ **-** Characters are controlled by swd_chat module. Feel free to create your own characters with custom avatars, names and behaviour!",
                          inline=False)
    second_page.add_field(name="▶Configuration:",
                          value="➾ **-** Creation of your character:\nFirst of all you'll need to execute **/create_character [name] [prefix] [avatar url]**\nLet's now figure out what each part of that command means.\n**[name]** - Your character's name. Make sure it's sfw and readable.\n**[prefix]** - a word or a short phrase that will trigger your character. Remember that character will only work in Swift AI channel, check /settings to see the current selected channel.\n**[avatar url]** - link to your bot's avatar. Can be either image or gif.",
                          inline=False)
    second_page.add_field(name="▶Usage:",
                          value="➾ **-** Here's and example of how a message to a character should look like:\n```sw Hello Swifty! How are you?```\nIn this case, **sw** is a prefix that triggers character. Message should follow the prefix, separated from it at the same time.",
                          inline=False)
