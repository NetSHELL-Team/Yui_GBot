import os
import subprocess
import sys

from contextlib import suppress
from time import sleep

import tgbot

from tgbot import dispatcher
from tgbot.modules.helper_funcs.chat_status import dev_plus
from telegram import TelegramError, Update
from telegram.error import Unauthorized
from telegram.ext import CallbackContext, CommandHandler, run_async

@run_async
@dev_plus
def allow_groups(update: Update, context: CallbackContext):
    args = context.args
    if not args:
        update.effective_message.reply_text(f"Current state: {tgbot.ALLOW_CHATS}")
        return
    if args[0].lower() in ["off", "no"]:
        tgbot.ALLOW_CHATS = True
    elif args[0].lower() in ["yes", "on"]:
        tgbot.ALLOW_CHATS = False
    else:
        update.effective_message.reply_text("Format: /lockdown Yes/No or Off/On")
        return
    update.effective_message.reply_text("Done! Lockdown value toggled.")

@run_async
@dev_plus
def leave(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    if args:
        chat_id = str(args[0])
        try:
            bot.leave_chat(int(chat_id))
        except TelegramError:
            update.effective_message.reply_text(
                "Beep boop, I could not leave that group(dunno why tho)."
            )
            return
        with suppress(Unauthorized):
            update.effective_message.reply_text("Beep boop, I left that soup!.")
    else:
        update.effective_message.reply_text("Send a valid chat ID")





LEAVE_HANDLER = CommandHandler("leave", leave)
ALLOWGROUPS_HANDLER = CommandHandler("lockdown", allow_groups)

dispatcher.add_handler(ALLOWGROUPS_HANDLER)
dispatcher.add_handler(LEAVE_HANDLER)



__handlers__ = [LEAVE_HANDLER, ALLOWGROUPS_HANDLER]










# I0BOZXRfU0hFTEwgUHJvamVjdCAjQFlVaV9HQm90IChCWSAtIEBHQm90X05ldHdvcmsp




