import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from YuiGBot import telethn
from YuiGBot.events import register as Yui
from telethon import TelegramClient




@Yui(pattern="^/vctag ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "ꜱᴀᴠɪ ᴠᴄ ᴊᴏɪɴ ᴋʀᴏ !!"
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 99999):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


@Yui(pattern="^/tagadmin ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = " Admins Kha Ho !!! "
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

__mod_name__ = "VC-Tag"
__help__ = """
- /vctag : Tag everyone in a chat
- /tagadmin tag the group admin
"""



# https://stackoverflow.com/questions/63781592/what-should-i-do-if-i-want-tag-all-members-of-a-group-in-telegram-python-bot

# I0BOZXRfU0hFTEwgUHJvamVjdCAjQFlVaV9HQm90IChCWSAtIEBHQm90X05ldHdvcmsp
