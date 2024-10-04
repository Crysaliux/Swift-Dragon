from peewee import *
from playhouse.cockroachdb import CockroachDatabase
import random
import discord
import asyncio
from PIL import Image, ImageDraw, ImageFont
import requests
import os
from Runners.Executors.console import Swdconsole_logs, returns
from Runners.Executors.securitymanager import Swdai_security
from Runners.Executors.bingwrapper import ImageGen
from Runners.Executors.configmanager import Config
from datetime import datetime, date, timedelta

conf = Config()
err_logs = Swdconsole_logs()
ig = ImageGen(auth_cookie=conf.swift_config()["bing_auth_cookie"], auth_cookie_SRCHHPGUSR=conf.swift_config()["auth_cookie_SRCHHPGUSR"])
sa = Swdai_security()

citadel = CockroachDatabase(conf.swift_config()["database"])

class SWDLogs(Model):
    guild_id = BigIntegerField()
    channel_id = BigIntegerField()

    class Meta:
        database = citadel

class SWDGchat(Model):
    guild_id = BigIntegerField()
    channel_id = BigIntegerField()

    class Meta:
        database = citadel

class SWDChat(Model):
    guild_id = BigIntegerField()
    channel_id = BigIntegerField()

    class Meta:
        database = citadel

class SWDTod(Model):
    guild_id = BigIntegerField()
    channel_id = BigIntegerField()

    class Meta:
        database = citadel

class SWDGreetings(Model):
    guild_id = BigIntegerField()
    channel_id = BigIntegerField()

    class Meta:
        database = citadel

class SWDArtshare(Model):
    guild_id = BigIntegerField()
    channel_id = BigIntegerField()

    class Meta:
        database = citadel

class SWDAutomod(Model):
    guild_id = BigIntegerField()

    class Meta:
        database = citadel

class SWDUser(Model):
    user_id = BigIntegerField()
    account_type = CharField(max_length=10)
    end_date = DateField()

    class Meta:
        database = citadel

class SWDSettings(Model):
    logs = ForeignKeyField(SWDLogs)
    logs_stats = CharField(max_length=10)

    gchat = ForeignKeyField(SWDGchat)
    gchat_stats = CharField(max_length=10)

    chat = ForeignKeyField(SWDChat)
    chat_stats = CharField(max_length=10)

    tod = ForeignKeyField(SWDTod)
    tod_stats = CharField(max_length=10)

    greetings = ForeignKeyField(SWDGreetings)
    greetings_stats = CharField(max_length=10)
    greetings_message = CharField(max_length=500)

    artshare = ForeignKeyField(SWDArtshare)
    artshare_stats = CharField(max_length=10)


    class Meta:
        database = citadel

class SWDWarns(Model):
    guild_id = BigIntegerField()
    user_id = BigIntegerField()
    warn = CharField(max_length=200)

    class Meta:
        database = citadel

class SWDArts(Model):
    artist_id = BigIntegerField()
    info = CharField(max_length=500)
    rating = BigIntegerField()
    uid = BigIntegerField()
    name = CharField(max_length=20)

    class Meta:
        database = citadel

class SWDCharacters(Model):
    user = ForeignKeyField(SWDUser)
    name = CharField(max_length=20)
    avatar = CharField(max_length=200)
    prefix = CharField(max_length=5)
    prompt = TextField()

    class Meta:
        database = citadel

class SWDMemory(Model):
    user = ForeignKeyField(SWDUser)
    character = ForeignKeyField(SWDCharacters)
    role = CharField(max_length=20)
    content = TextField()

    class Meta:
        database = citadel

class SWDQueue(Model):
    user_id = BigIntegerField()
    channel_id = BigIntegerField()
    prompt = TextField()

    class Meta:
        database = citadel


citadel.connect()
citadel.create_tables([SWDLogs, SWDGchat, SWDChat, SWDTod, SWDGreetings, SWDArtshare, SWDAutomod, SWDUser, SWDSettings, SWDArts, SWDCharacters, SWDMemory, SWDQueue])


class Swdmain_settings:
    def __init__(self):
        if citadel.is_closed():
            citadel.connect()

    def check_connection(self):
        if citadel.is_closed():
            citadel.connect()

    def swd_setup(self, type: str, guild_id=None, channel_id=None, status: str=None, message: str=None):
        try:
            if type == "logs":
                logs = SWDLogs.get_or_none(guild_id=guild_id)
                if logs is None:
                    logs = SWDLogs.create(guild_id=guild_id, channel_id=channel_id)
                else:
                    logs.channel_id = channel_id
                    logs.save()

                settings = SWDSettings.get_or_none(logs=logs)
                if settings is None:
                    gchat = SWDGchat.create(guild_id=guild_id, channel_id='0')
                    chat = SWDChat.create(guild_id=guild_id, channel_id='0')
                    tod = SWDTod.create(guild_id=guild_id, channel_id='0')
                    greetings = SWDGreetings.create(guild_id=guild_id, channel_id='0')
                    artshare = SWDArtshare.create(guild_id=guild_id, channel_id='0')
                    SWDSettings.create(logs=logs, logs_stats=status, gchat=gchat, gchat_stats='off', chat=chat,
                                       chat_stats='off', tod=tod, tod_stats='off', greetings=greetings,
                                       greetings_stats='off', greetings_message='none', artshare=artshare,
                                       artshare_stats='off')
                else:
                    settings.logs_stats = status
                    settings.save()

            elif type == "gchat":
                gchat = SWDGchat.get_or_none(guild_id=guild_id)
                if gchat is None:
                    gchat = SWDGchat.create(guild_id=guild_id, channel_id=channel_id)
                else:
                    gchat.channel_id = channel_id
                    gchat.save()

                settings = SWDSettings.get_or_none(gchat=gchat)
                if settings is None:
                    logs = SWDLogs.create(guild_id=guild_id, channel_id='0')
                    chat = SWDChat.create(guild_id=guild_id, channel_id='0')
                    tod = SWDTod.create(guild_id=guild_id, channel_id='0')
                    greetings = SWDGreetings.create(guild_id=guild_id, channel_id='0')
                    artshare = SWDArtshare.create(guild_id=guild_id, channel_id='0')
                    SWDSettings.create(logs=logs, logs_stats='off', gchat=gchat, gchat_stats=status, chat=chat,
                                       chat_stats='off', tod=tod, tod_stats='off', greetings=greetings,
                                       greetings_stats='off', greetings_message='none', artshare=artshare,
                                       artshare_stats='off')
                else:
                    settings.gchat_stats = status
                    settings.save()

            elif type == "chat":
                chat = SWDChat.get_or_none(guild_id=guild_id)
                if chat is None:
                    chat = SWDChat.create(guild_id=guild_id, channel_id=channel_id)
                else:
                    chat.channel_id = channel_id
                    chat.save()

                settings = SWDSettings.get_or_none(chat=chat)
                if settings is None:
                    logs = SWDLogs.create(guild_id=guild_id, channel_id='0')
                    gchat = SWDGchat.create(guild_id=guild_id, channel_id='0')
                    tod = SWDTod.create(guild_id=guild_id, channel_id='0')
                    greetings = SWDGreetings.create(guild_id=guild_id, channel_id='0')
                    artshare = SWDArtshare.create(guild_id=guild_id, channel_id='0')
                    SWDSettings.create(logs=logs, logs_stats='off', gchat=gchat, gchat_stats='off', chat=chat,
                                       chat_stats=status, tod=tod, tod_stats='off', greetings=greetings,
                                       greetings_stats='off', greetings_message='none', artshare=artshare,
                                       artshare_stats='off')
                else:
                    settings.chat_stats = status
                    settings.save()

            elif type == "tod":
                tod = SWDTod.get_or_none(guild_id=guild_id)
                if tod is None:
                    tod = SWDTod.create(guild_id=guild_id, channel_id=channel_id)
                else:
                    tod.channel_id = channel_id
                    tod.save()

                settings = SWDSettings.get_or_none(tod=tod)
                if settings is None:
                    logs = SWDLogs.create(guild_id=guild_id, channel_id='0')
                    gchat = SWDGchat.create(guild_id=guild_id, channel_id='0')
                    chat = SWDChat.create(guild_id=guild_id, channel_id='0')
                    greetings = SWDGreetings.create(guild_id=guild_id, channel_id='0')
                    artshare = SWDArtshare.create(guild_id=guild_id, channel_id='0')
                    SWDSettings.create(logs=logs, logs_stats='off', gchat=gchat, gchat_stats='off', chat=chat,
                                       chat_stats='off', tod=tod, tod_stats=status, greetings=greetings,
                                       greetings_stats='off', greetings_message='none', artshare=artshare,
                                       artshare_stats='off')
                else:
                    settings.tod_stats = status
                    settings.save()

            elif type == "greetings":
                greetings = SWDGreetings.get_or_none(guild_id=guild_id)
                if greetings is None:
                    greetings = SWDGreetings.create(guild_id=guild_id, channel_id=channel_id)
                else:
                    greetings.channel_id = channel_id
                    greetings.save()

                settings = SWDSettings.get_or_none(greetings=greetings)
                if settings is None:
                    logs = SWDLogs.create(guild_id=guild_id, channel_id='0')
                    gchat = SWDGchat.create(guild_id=guild_id, channel_id='0')
                    chat = SWDChat.create(guild_id=guild_id, channel_id='0')
                    tod = SWDTod.create(guild_id=guild_id, channel_id='0')
                    artshare = SWDArtshare.create(guild_id=guild_id, channel_id='0')
                    SWDSettings.create(logs=logs, logs_stats='off', gchat=gchat, gchat_stats='off', chat=chat,
                                       chat_stats='off', tod=tod, tod_stats='off', greetings=greetings,
                                       greetings_stats=status, greetings_message=message, artshare=artshare,
                                       artshare_stats='off')
                else:
                    settings.greetings_stats = status
                    settings.greetings_message = message
                    settings.save()

            elif type == "artshare":
                artshare = SWDArtshare.get_or_none(guild_id=guild_id)
                if artshare is None:
                    artshare = SWDArtshare.create(guild_id=guild_id, channel_id=channel_id)
                else:
                    artshare.channel_id = channel_id
                    artshare.save()

                settings = SWDSettings.get_or_none(artshare=artshare)
                if settings is None:
                    logs = SWDLogs.create(guild_id=guild_id, channel_id='0')
                    gchat = SWDGchat.create(guild_id=guild_id, channel_id='0')
                    chat = SWDChat.create(guild_id=guild_id, channel_id='0')
                    tod = SWDTod.create(guild_id=guild_id, channel_id='0')
                    greetings = SWDGreetings.create(guild_id=guild_id, channel_id='0')
                    SWDSettings.create(logs=logs, logs_stats='off', gchat=gchat, gchat_stats='off', chat=chat,
                                       chat_stats='off', tod=tod, tod_stats='off', greetings=greetings,
                                       greetings_stats='off', greetings_message='none', artshare=artshare,
                                       artshare_stats=status)
                else:
                    settings.artshare_stats = status
                    settings.save()
        except:
            err_logs.error('400')
            return 'error'

    def swd_pull(self, guild_id, type: str):
        try:
            result = {}
            if type == 'logs':
                logs = SWDLogs.get_or_none(guild_id=guild_id)
                if logs is None:
                    result['channel_id'] = "none"
                    result['status'] = "off"
                else:
                    settings = SWDSettings.get(logs=logs)
                    result['channel_id'] = logs.channel_id
                    result['status'] = settings.logs_stats

            elif type == 'gchat':
                gchat = SWDGchat.get_or_none(guild_id=guild_id)
                if gchat is None:
                    result['channel_id'] = "none"
                    result['status'] = "off"
                else:
                    settings = SWDSettings.get(gchat=gchat)
                    result['channel_id'] = gchat.channel_id
                    result['status'] = settings.gchat_stats

            elif type == 'chat':
                chat = SWDChat.get_or_none(guild_id=guild_id)
                if chat is None:
                    result['channel_id'] = "none"
                    result['status'] = "off"
                else:
                    settings = SWDSettings.get(chat=chat)
                    result['channel_id'] = chat.channel_id
                    result['status'] = settings.chat_stats

            elif type == 'tod':
                tod = SWDTod.get_or_none(guild_id=guild_id)
                if tod is None:
                    result['channel_id'] = "none"
                    result['status'] = "off"
                else:
                    settings = SWDSettings.get(tod=tod)
                    result['channel_id'] = tod.channel_id
                    result['status'] = settings.tod_stats

            elif type == 'greetings':
                greetings = SWDGreetings.get_or_none(guild_id=guild_id)
                if greetings is None:
                    result['channel_id'] = "none"
                    result['status'] = "off"
                    result['message'] = "none"
                else:
                    settings = SWDSettings.get(greetings=greetings)
                    result['channel_id'] = greetings.channel_id
                    result['status'] = settings.greetings_stats
                    result['message'] = settings.greetings_message

            elif type == 'artshare':
                artshare = SWDArtshare.get_or_none(guild_id=guild_id)
                if artshare is None:
                    result['channel_id'] = "none"
                    result['status'] = "off"
                else:
                    settings = SWDSettings.get(artshare=artshare)
                    result['channel_id'] = artshare.channel_id
                    result['status'] = settings.artshare_stats

            return result
        except:
            err_logs.error('400')
            return 'error'

    def swd_channel_modify(self, type, guild_id):
        try:
            if type != 0:
                result = "https://discord.com/channels/" + f"{guild_id}/" + f"{type}"
            else:
                result = "**Not selected**"
            return result
        except:
            err_logs.error('400')
            return 'error'

    def running_bar(self, total: int, progress: int):
        try:
            bar = "<:bar:1279376595911573504>"
            empty_bar = "<:emptybar:1279378261746651169>"
            progress_bar = []
            for i in range(total):
                progress_bar.append(empty_bar)
            for i in range(progress):
                progress_bar[i] = bar
            result = ''.join(progress_bar)
            return result
        except:
            err_logs.error('400')
            return 'error'

    def payment(self, type: str, user_id):
        try:
            expiration_date = None
            if type == 'monthly':
                user = SWDUser.get_or_none(user_id=user_id)
                if user is None:
                    user = SWDUser.create(user_id=user_id, account_type=type, end_date=date.today())
                    user.end_date = user.end_date + timedelta(days=30)
                    user.save()
                else:
                    user.account_type = type
                    user.end_date = user.end_date + timedelta(days=30)
                    user.save()
                expiration_date = user.end_date

            elif type == 'yearly':
                user = SWDUser.get_or_none(user_id=user_id)
                if user is None:
                    user = SWDUser.create(user_id=user_id, account_type=type, end_date=date.today())
                    user.end_date = user.end_date + timedelta(days=365)
                    user.save()
                else:
                    user.account_type = type
                    user.end_date = user.end_date + timedelta(days=365)
                    user.save()
                expiration_date = user.end_date

            elif type == 'remove':
                user = SWDUser.get_or_none(user_id=user_id)
                if user is None:
                    pass
                else:
                    user.delete_instance()

            return expiration_date
        except:
            err_logs.error('400')
            return 'error'

    def give_warn(self, guild_id, user_id, warn):
        try:
            warns = SWDWarns.get_or_none(guild_id=guild_id, user_id=user_id)
            if warns is None:
                SWDWarns.create(guild_id=guild_id, user_id=user_id, warn=warn)
            else:
                SWDWarns.create(guild_id=guild_id, user_id=user_id, warn=warn)
                number = SWDWarns.select().where(SWDWarns.guild_id == guild_id, SWDWarns.user_id == user_id).count()
                if number > 2:
                    return returns.over_limit
        except:
            err_logs.error('400')
            return 'error'

    def pardon(self, guild_id, user_id):
        try:
            warns = SWDWarns.get_or_none(guild_id=guild_id, user_id=user_id)
            if warns is None:
                return returns.not_found
            else:
                warns.delete_instance()
        except:
            err_logs.error('400')
            return 'error'

    def register_art(self, user_id, info, name):
        try:
            artist = SWDArts.get_or_none(artist_id=user_id)
            if artist is None:
                while True:
                    random_id = random.randint(1, 3000)
                    check_uid = SWDArts.get_or_none(uid=random_id)
                    if check_uid is None:
                        SWDArts.create(artist_id=user_id, info=info, rating='0', uid=random_id, name=name)
                        break
            else:
                return returns.exists
        except:
            err_logs.error('400')
            return 'error'

    def delete(self, user_id):
        try:
            artist = SWDArts.get_or_none(artist_id=user_id)
            if artist is None:
                return returns.not_found
            else:
                artist.delete_instance()
        except:
            err_logs.error('400')
            return 'error'

    def get_artist(self, uid=None, artist_id=None):
        try:
            if uid:
                artist = SWDArts.get_or_none(uid=uid)
                if artist is None:
                    return returns.not_found
                else:
                    result = {'name': artist.name, 'artist_id': artist.artist_id, 'rating': artist.rating, 'info': artist.info}
                    return result
            elif artist_id:
                artist = SWDArts.get_or_none(artist_id=artist_id)
                if artist is None:
                    return returns.not_found
                else:
                    result = {'name': artist.name, 'uid': artist.uid, 'rating': artist.rating, 'info': artist.info}
                    return result
        except:
            err_logs.error('400')
            return 'error'

    async def art_spread(self, image_url, user_id, guild_id, channel_id, name: str, swd):
        try:
            artchannel = SWDArtshare.get_or_none(guild_id=guild_id)
            if artchannel is None:
                pass
            else:
                if artchannel.channel_id == channel_id:
                    artist = SWDArts.get_or_none(artist_id=user_id)
                    if artist is None:
                        pass
                    else:
                        original = Image.open(requests.get(image_url, stream=True).raw)
                        draw = ImageDraw.Draw(original)
                        text = name
                        font = ImageFont.truetype('arial.ttf', 82)

                        textwidth, textheight = draw.textsize(text, font)
                        width, height = original.size
                        x = width / 2 - textwidth / 2
                        y = height - textheight - 300

                        draw.text((x, y), text, font=font)
                        original.save('Runners/Executors/ud/wm.png', "PNG")

                        file = discord.File("Runners/Executors/ud/wm.png")
                        message = f'**Artist ID:** {artist.uid}\n**Artist name:** {artist.name}\n**Rating:** {artist.rating}\n**Personal information:**\n{artist.info}'
                        for swift in SWDArts.select():
                            if swift.channel_id == channel_id:
                                pass
                            else:
                                channel = swd.get_channel(swift.channel_id)
                                await channel.send(message, files=file)
                else:
                    pass
        except:
            err_logs.error('400')
            return 'error'

    async def gchat_purge(self, guild_id, swd, name, avatar, message):
        try:
            for swift in SWDGchat.select():
                if guild_id == swift.guild_id:
                    pass
                else:
                    settings = SWDSettings.get(gchat=SWDGchat.get(guild_id=swift.guild_id))
                    if settings.gchat_stats == "off":
                        pass
                    else:
                        if sa.check_content(message.content) == 'yes':
                            await message.delete()
                        else:
                            rc = swd.get_channel(swift.channel_id)
                            sender = await rc.create_webhook(name=name, avatar=avatar)
                            await sender.send(content=message.content)
                            await sender.delete()
        except:
            err_logs.error('400')
            return 'error'


class Swdswift_chat:
    def __init__(self):
        if citadel.is_closed():
            citadel.connect()

    def character_check(self, user_id, prefix: str):
        try:
            user = SWDUser.get_or_none(user_id=user_id)
            if user is None:
                SWDUser.create(user_id=user_id, account_type='default', end_date=date.today())
                return returns.not_found
            else:
                character = SWDCharacters.get_or_none(user=user, prefix=prefix)
                if character is None:
                    return returns.not_found
                else:
                    return {"name": character.name, "prefix": character.prefix, "avatar": character.avatar,
                            "prompt": character.prompt}
        except:
            err_logs.error('400')
            return 'error'

    def get_characters(self, user_id):
        user = SWDUser.get_or_none(user_id=user_id)
        if user is None:
            SWDUser.create(user_id=user_id, account_type='default', end_date=date.today())
            return returns.not_found
        else:
            character = SWDCharacters.get_or_none(user=user)
            if character is None:
                return returns.not_found
            else:
                chars = []
                for swift in SWDCharacters.select().where(SWDCharacters.user == user):
                    chars.append({"name": swift.name, "prefix": swift.prefix, "avatar": swift.avatar, "prompt": swift.prompt})
                return chars

    def character_create(self, user_id, name: str, prefix, avatar, prompt: str):
        try:
            user = SWDUser.get_or_none(user_id=user_id)
            if user is None:
                user = SWDUser.create(user_id=user_id, account_type='default', end_date=date.today())
                SWDCharacters.create(user=user, name=name, avatar=avatar, prefix=prefix, prompt=prompt)
            else:
                character = SWDCharacters.get_or_none(user=user, prefix=prefix)
                if character is None:
                    SWDCharacters.create(user=user, name=name, avatar=avatar, prefix=prefix, prompt=prompt)
                else:
                    character.name = name
                    character.avatar = avatar
                    character.prefix = prefix
                    character.prompt = prompt
                    character.save()
        except:
            err_logs.error('400')
            return 'error'

    def character_delete(self, user_id, prefix: str):
        try:
            user = SWDUser.get_or_none(user_id=user_id)
            character = SWDCharacters.get_or_none(user=user, prefix=prefix)
            for memory in SWDMemory.select().where(SWDMemory.user == user, SWDMemory.character == character):
                memory.delete_instance()
            character.delete_instance()
        except:
            err_logs.error('400')
            return 'error'

    async def character_reply(self, message, source, prefix: str, sys_prompt, name: str, avatar, accon, gcclient, model, temp: str, max_tok: str):
        async with message.channel.typing():
            messages = source.retrieve(message.author.id, prefix)
            if messages == 'none':
                messages = [
                    {
                        "role": "system",
                        "content": sys_prompt
                    },
                    {
                        "role": "user",
                        "content": accon
                    }
                ]
            else:
                new_question = {
                    "role": "user",
                    "content": accon
                }
                messages.append(new_question)
            chat_completion = gcclient.chat.completions.create(
                messages=messages,
                model=model,
                temperature=temp,
                max_tokens=max_tok,
                top_p=1,
                stop=None,
                stream=False
            )
            source.new_message(accon, chat_completion.choices[0].message.content, message.author.id, prefix)

        webhooks = await message.channel.webhooks()
        if webhooks is None:
            hook = await message.channel.create_webhook(name="Swift dragon charfc")
            await hook.send(chat_completion.choices[0].message.content, username=name, avatar_url=avatar)
        else:
            sent = False
            for webhook in webhooks:
                if webhook.name == "Swift dragon charfc":
                    await webhook.send(chat_completion.choices[0].message.content, username=name, avatar_url=avatar)
                    sent = True
                    break

            if sent == False:
                hook = await message.channel.create_webhook(name="Swift dragon charfc")
                await hook.send(chat_completion.choices[0].message.content, username=name, avatar_url=avatar)

    def new_message(self, message, reply, user_id, prefix):
        try:
            user = SWDUser.get_or_none(user_id=user_id)
            character = SWDCharacters.get_or_none(user=user, prefix=prefix)
            memory = SWDMemory.get_or_none(user=user, character=character)

            if character is None:
                return returns.not_found

            else:
                default = {
                    "role": "system",
                    "content": character.prompt
                }

                if memory is None:
                    new_data = []

                    question_data = {}
                    question_data["role"] = "user"
                    question_data["content"] = message

                    reply_data = {}
                    reply_data["role"] = "assistant"
                    reply_data["content"] = reply

                    new_data.append(default)
                    new_data.append(question_data)
                    new_data.append(reply_data)
                else:
                    new_data = []

                    question_data = {}
                    question_data["role"] = "user"
                    question_data["content"] = message

                    reply_data = {}
                    reply_data["role"] = "assistant"
                    reply_data["content"] = reply

                    new_data.append(question_data)
                    new_data.append(reply_data)

                for lines in new_data:
                    SWDMemory.create(user=user, character=character, role=lines["role"], content=lines["content"])
        except:
            err_logs.error('400')
            return 'error'

    def retrieve(self, user_id, prefix):
        try:
            retrieve_data = []
            user = SWDUser.get_or_none(user_id=user_id)
            character = SWDCharacters.get_or_none(user=user, prefix=prefix)
            memory = SWDMemory.get_or_none(user=user, character=character)
            if user is None:
                return 'none'
            elif character is None:
                return 'none'
            elif memory is None:
                return 'none'
            else:
                for memory in SWDMemory.select().where(SWDMemory.user == user, SWDMemory.character == character):
                    data_memory = {}
                    data_memory["role"] = memory.role
                    data_memory["content"] = memory.content
                    retrieve_data.append(data_memory)
                return retrieve_data
        except:
            err_logs.error('400')
            return 'error'

    def delete_history(self, user_id, prefix: str):
        try:
            user = SWDUser.get_or_none(user_id=user_id)
            character = SWDCharacters.get_or_none(user=user, prefix=prefix)
            for memory in SWDMemory.select().where(SWDMemory.user == user, SWDMemory.character == character):
                memory.delete_instance()
        except:
            err_logs.error('400')
            return 'error'


class Swdswift_imagine:
    def __init__(self):
        if citadel.is_closed():
            citadel.connect()

    def queue_save(self, user_id, channel_id, prompt):
        try:
            getexisting = SWDQueue.get_or_none(user_id=user_id)
            if getexisting is None:
                SWDQueue.create(user_id=user_id, channel_id=channel_id, prompt=prompt)
                for swift in SWDQueue.select().where(SWDQueue.user_id == user_id):
                    number = str(swift)
                return number
            else:
                return returns.exists
        except:
            err_logs.error('400')
            return 'error'
        
    def bulk_pull(self):
        try:
            getexisting = SWDQueue.get_or_none()
            if getexisting is None:
                return returns.not_found
            else:
                data = []
                for swift in SWDQueue.select():
                    user_data = [swift.user_id, swift.channel_id]
                    data.append(user_data)
            return data
        except:
            err_logs.error('400')
            return 'error'

    async def generate_image(self, swd, user_id, loop):
        try:
            getexisting = SWDQueue.get_or_none(user_id=user_id)
            if getexisting is None:
                return returns.not_found
            else:
                channel = swd.get_channel(getexisting.channel_id)
                user = swd.get_user(user_id)
                p = getexisting.prompt

                links = ig.get_images(p, channel, user)
                getexisting.delete_instance()

                result = Image.new('RGB', (2048, 2048), (250, 250, 250))
                count = 0
                ordered_links = []
                for link in links:
                    if "https://r.bing.com" in link:
                        pass
                    else:
                        ordered_links.append(link)
                        count = count + 1
                        image = Image.open(requests.get(link, stream=True).raw)
                        if count == 1:
                            result.paste(image, (0, 0))
                        elif count == 2:
                            result.paste(image, (image.size[0], 0))
                        elif count == 3:
                            result.paste(image, (0, image.size[1]))
                        elif count == 4:
                            result.paste(image, (image.size[0], image.size[1]))

                result.save(f"Runners/Executors/ud/{user_id}.png", "PNG")
                file = discord.File(f"Runners/Executors/ud/{user_id}.png")

                return {"count": count, "image": "attachment://result.png", "links": ordered_links, "file": file}
        except:
            err_logs.error('400')
            return 'error'