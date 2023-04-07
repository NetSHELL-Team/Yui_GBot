import html
import random
import yue_tgbot.modules.verified_ok as verified_ok
from yue_tgbot import dispatcher

from telegram import ParseMode, Update, Bot

from yue_tgbot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def verify(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(verified_ok.VERIFY))

@run_async
def draj(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(verified_ok.DRAJ))

VERIFY_HANDLER = DisableAbleCommandHandler("verify", verify)
DRAJ_HANDLER = DisableAbleCommandHandler("draj", draj)

dispatcher.add_handler(VERIFY_HANDLER)
dispatcher.add_handler(DRAJ_HANDLER)
