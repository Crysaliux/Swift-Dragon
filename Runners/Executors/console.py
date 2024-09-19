import discord
import asyncio

class colors:
    ERROR = '\033[91m'
    WARNING = '\033[33m'
    LINE = '\033[45m'

    emb_error = 0x992d22
    emb_warning = 0xf1c40f

class returns:
    exists = 'inex'
    not_found = 'nfo'
    over_limit = 'ovlim'

class indexes:
    idle = '[IDLE]: '
    warning = '[WARNING]: '
    error = '[ERROR]: '

class warnings:
    not_enough_perms = "Not enough permissions provided, warning code: 010"
    cooldown = "Command is on cooldown, warning code: 020"
    system_command = "System commands can only be executed by Swifty Team, warning code: 030"
    unexpected_prefix = "Wrong prefix, warning code: 040"

class errors:
    unexpected_error = "Unexpected error occurred, error code: 100"
    user_not_found = "User can't be found, error code: 200"
    role_not_found = "Role can't be found, warning code: 300"
    internal_error = "Internal error has occurred, error code: 400"
    timeout_error = "Timeout error has occurred, error code: 500"
    redirect_error = "Redirect error has occurred, error code: 600"
    blocked_prompt_error = "Blocked prompt error has occurred, error code: 700"
    prompt_being_reviewed_error = "Prompt being reviewed error has occurred, error code: 800"
    no_results_error = "No results error has occurred, error code: 900"
    unsupported_lang_error = "Unsupported language error has occurred, error code : 1000"
    bad_images_error = "Bad images error has occurred, error code : 1100"
    no_images_error = "No images error has occurred, error code : 1200"
    server_not_found = "Server has not been found, error code :1300"
    token_not_found = "Token file has not been found, error code: 1400"
    char_not_found = "Character not found, error code: 1300"


class Swdconsole_logs:
    def __init__(self):
        print(indexes.idle + colors.LINE + 'Console executor has been called')

    def call(self, executor: str):
        print(indexes.idle + colors.LINE + f'{executor} executor has been called')

    def warning(self, code: str):
        if code == '010':
            print(indexes.warning + colors.WARNING + warnings.not_enough_perms)
        elif code == '020':
            print(indexes.warning + colors.WARNING + warnings.cooldown)
        elif code == '040':
            print(indexes.warning + colors.WARNING + warnings.unexpected_prefix)
        else:
            print(indexes.error + colors.ERROR + errors.internal_error)

    def error(self, code: str, time=None):
        if code == '100':
            print(indexes.error + colors.ERROR + errors.unexpected_error)
        elif code == '200':
            print(indexes.error + colors.ERROR + errors.user_not_found)
        elif code == '300':
            print(indexes.error + colors.ERROR + errors.role_not_found)
        elif code == '400':
            print(indexes.error + colors.ERROR + errors.internal_error)
        elif code == '500':
            print(indexes.error + colors.ERROR + errors.timeout_error)
        elif code == '600':
            print(indexes.error + colors.ERROR + errors.redirect_error)
        elif code == '700':
            print(indexes.error + colors.ERROR + errors.blocked_prompt_error)
        elif code == '800':
            print(indexes.error + colors.ERROR + errors.prompt_being_reviewed_error)
        elif code == '900':
            print(indexes.error + colors.ERROR + errors.no_results_error)
        elif code == '1000':
            print(indexes.error + colors.ERROR + errors.unsupported_lang_error)
        elif code == '1100':
            print(indexes.error + colors.ERROR + errors.bad_images_error)
        elif code == '1200':
            print(indexes.error + colors.ERROR + errors.no_images_error)
        elif code == '1300':
            print(indexes.error + colors.ERROR + errors.server_not_found + f"At: {time}")
        elif code == '1400':
            print(indexes.error + colors.ERROR + errors.token_not_found + f"At: {time}")
        else:
            print(indexes.error + colors.ERROR + errors.internal_error)

    def logs(self, code: str, module=None, time=None):
        if code == '001':
            print(indexes.idle + colors.LINE + f"Module {module} has been successfully loaded at {time}")

    async def command_error(self, code: str, ctx, user=None, role=None):
        if code == '100':
            error_emb = discord.Embed(title='[Unexpected Error!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems an unexpected error has occurred :c",
                value=f"➾ **-** Contact us in our community to report the bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Unexpected error occurred, error code: 100```",
                inline=False)
            await ctx.respond(embed=error_emb, ephemeral=True)
        elif code == '200':
            error_emb = discord.Embed(title='[User Not Found!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems user {user.name} can't be found, ask staff if you think this is an error",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```User can't be found, error code: 200```",
                inline=False)
            await ctx.respond(embed=error_emb, ephemeral=True)
        elif code == '300':
            error_emb = discord.Embed(title='[Role Not Found!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems {role} role can't be found, ask staff if you think this is an error",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Role can't be found, error code: 300```",
                inline=False)
            await ctx.respond(embed=error_emb, ephemeral=True)
        elif code == '500':
            error_emb = discord.Embed(title='[Timeout Error!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems timeout error has occurred :c",
                value=f"➾ **-** Contact us in our community to report the bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Timeout error occurred, error code: 500```",
                inline=False)
            await ctx.respond(embed=error_emb, ephemeral=True)
        elif code == '600':
            error_emb = discord.Embed(title='[Redirect Error!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems redirect error has occurred :c",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Redirect error occurred, error code: 600```",
                inline=False)
            await ctx.respond(embed=error_emb, ephemeral=True)
        elif code == '700':
            error_emb = discord.Embed(title='[Blocked Prompt!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems blocked prompt error has occurred, try removing or replacing any sensitive words",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Blocked prompt error occurred, error code: 700```",
                inline=False)
            await ctx.respond(embed=error_emb, ephemeral=True)
        elif code == '800':
            error_emb = discord.Embed(title='[Prompt Being Reviewed!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems prompt being reviewed error has occurred, try removing or replacing any sensitive words",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Prompt being reviewed error occurred, error code: 800```",
                inline=False)
            await ctx.respond(embed=error_emb, ephemeral=True)
        elif code == '900':
            error_emb = discord.Embed(title='[No Results!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems no results error has occurred :c",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```No results error occurred, error code: 900```",
                inline=False)
            await ctx.respond(embed=error_emb, ephemeral=True)
        elif code == '1000':
            error_emb = discord.Embed(title='[Unsupported Language!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems unsupported language error has occurred, AI does not support that language!",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Unsupported language error occurred, error code: 1000```",
                inline=False)
            await ctx.respond(embed=error_emb, ephemeral=True)
        elif code == '1100':
            error_emb = discord.Embed(title='[Bad Images!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems bad images error has occurred :c",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Bad images error occurred, error code: 1100```",
                inline=False)
            await ctx.respond(embed=error_emb, ephemeral=True)
        elif code == '1200':
            error_emb = discord.Embed(title='[No Images!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems no images error has occurred",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```No images error occurred, error code: 1200```",
                inline=False)
            await ctx.respond(embed=error_emb, ephemeral=True)
        elif code == '1300':
            error_emb = discord.Embed(title='[Character Not Found!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems that character with specified prefix can't be found",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Character not found, error code: 1300```",
                inline=False)
            await ctx.respond(embed=error_emb, ephemeral=True)
        else:
            print(indexes.error + colors.ERROR + errors.internal_error)

    async def channel_error(self, code: str, channel, user=None, role=None):
        if code == '100':
            error_emb = discord.Embed(title='[Unexpected Error!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems an unexpected error has occurred :c",
                value=f"➾ **-** Contact us in our community to report the bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Unexpected error occurred, error code: 100```",
                inline=False)
            message = await channel.send(embed=error_emb)
            await message.reply(f"||{user.mention}||")
        elif code == '200':
            error_emb = discord.Embed(title='[User Not Found!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems user {user.name} can't be found, ask staff if you think this is an error",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```User can't be found, error code: 200```",
                inline=False)
            message = await channel.send(embed=error_emb)
            await message.reply(f"||{user.mention}||")
        elif code == '300':
            error_emb = discord.Embed(title='[Role Not Found!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems {role} role can't be found, ask staff if you think this is an error",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Role can't be found, error code: 300```",
                inline=False)
            message = await channel.send(embed=error_emb)
            await message.reply(f"||{user.mention}||")
        elif code == '500':
            error_emb = discord.Embed(title='[Timeout Error!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems timeout error has occurred :c",
                value=f"➾ **-** Contact us in our community to report the bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Timeout error occurred, error code: 500```",
                inline=False)
            message = await channel.send(embed=error_emb)
            await message.reply(f"||{user.mention}||")
        elif code == '600':
            error_emb = discord.Embed(title='[Redirect Error!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems redirect error has occurred :c",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Redirect error occurred, error code: 600```",
                inline=False)
            message = await channel.send(embed=error_emb)
            await message.reply(f"||{user.mention}||")
        elif code == '700':
            error_emb = discord.Embed(title='[Blocked Prompt!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems blocked prompt error has occurred, try removing or replacing any sensitive words",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Blocked prompt error occurred, error code: 700```",
                inline=False)
            message = await channel.send(embed=error_emb)
            await message.reply(f"||{user.mention}||")
        elif code == '800':
            error_emb = discord.Embed(title='[Prompt Being Reviewed!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems prompt being reviewed error has occurred, try removing or replacing any sensitive words",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Prompt being reviewed error occurred, error code: 800```",
                inline=False)
            message = await channel.send(embed=error_emb)
            await message.reply(f"||{user.mention}||")
        elif code == '900':
            error_emb = discord.Embed(title='[No Results!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems no results error has occurred :c",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```No results error occurred, error code: 900```",
                inline=False)
            message = await channel.send(embed=error_emb)
            await message.reply(f"||{user.mention}||")
        elif code == '1000':
            error_emb = discord.Embed(title='[Unsupported Language!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems unsupported language error has occurred, AI does not support that language!",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Unsupported language error occurred, error code: 1000```",
                inline=False)
            message = await channel.send(embed=error_emb)
            await message.reply(f"||{user.mention}||")
        elif code == '1100':
            error_emb = discord.Embed(title='[Bad Images!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems bad images error has occurred :c",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Bad images error occurred, error code: 1100```",
                inline=False)
            message = await channel.send(embed=error_emb)
            await message.reply(f"||{user.mention}||")
        elif code == '1200':
            error_emb = discord.Embed(title='[No Images!]', colour=colors.emb_error)
            error_emb.add_field(
                name=f"▶It seems no images error has occurred",
                value=f"➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```No images error occurred, error code: 1200```",
                inline=False)
            message = await channel.send(embed=error_emb)
            await message.reply(f"||{user.mention}||")
        else:
            print(indexes.error + colors.ERROR + errors.internal_error)

    async def command_warning(self, code: str, ctx, user=None, role=None):
        if code == '010':
            warning_emb = discord.Embed(title='[Missing Permissions!]', colour=colors.emb_warning)
            warning_emb.add_field(
                name="▶It seems you're missing some permissions, ask staff if you think this is an error",
                value=f'➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Not enough permissions provided, warning code: 010```',
                inline=False)
            await ctx.respond(embed=warning_emb, ephemeral=True)
        elif code == '030':
            warning_emb = discord.Embed(title='[System Command!]', colour=colors.emb_warning)
            warning_emb.add_field(
                name="▶It seems you're trying to execute bot's system command, ask staff if you think this is an error",
                value=f'➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```System commands can only be executed by Swifty Team, warning code: 030```',
                inline=False)
            await ctx.respond(embed=warning_emb, ephemeral=True)
        elif code == '040':
            warning_emb = discord.Embed(title='[Unexpected prefix!]', colour=colors.emb_warning)
            warning_emb.add_field(
                name="▶It seems that prefix is too big and can't be accepted! Prefixes can't have more than 4 characters, ask staff if you think this is an error",
                value=f'➾ **-** You can contact us in our support community if you think there is a bug: https://discord.gg/FpYas3s2Fp**\n➾ **-** ```Wrong prefix, warning code: 040```',
                inline=False)
            await ctx.respond(embed=warning_emb, ephemeral=True)
        else:
            print(indexes.error + colors.ERROR + errors.internal_error)