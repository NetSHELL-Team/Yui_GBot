import time
from typing import List

import requests
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

from YuiGBot import StartTime, dispatcher
from YuiGBot.modules.helper_funcs.chat_status import sudo_plus
from YuiGBot.modules.disable import DisableAbleCommandHandler

sites_list = {
    "Telegram": "https://api.telegram.org",
    "APi Core": "https://api.plyton.in",
    "PlyTon": "https://www.plyton.in/",
    "Jikan": "https://api.jikan.moe/v3",
}


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


def ping_func(to_ping: List[str]) -> List[str]:
    ping_result = []

    for each_ping in to_ping:

        start_time = time.time()
        site_to_ping = sites_list[each_ping]
        r = requests.get(site_to_ping)
        end_time = time.time()
        ping_time = str(round((end_time - start_time), 2)) + "s"

        pinged_site = f"<b>{each_ping}</b>"

        if each_ping == "APi Core" or each_ping == "PlyTon":
            pinged_site = f'<a href="{sites_list[each_ping]}">{each_ping}</a>'
            ping_time = f"<code>{ping_time} (Status: {r.status_code})</code>"

        ping_text = f"{pinged_site}: <code>{ping_time}</code>"
        ping_result.append(ping_text)

    return ping_result


@run_async
@sudo_plus
def ping(update: Update, context: CallbackContext):
    msg = update.effective_message

    start_time = time.time()
    message = msg.reply_text("Pinging...")
    end_time = time.time()
    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
    uptime = get_readable_time((time.time() - StartTime))

    message.edit_text(
        "STATUS!!\n"
        "<b>PiNG:</b> <code>{}</code>\n"
        "<b>SERVER ONLiNE:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode=ParseMode.HTML,
    )


@run_async
@sudo_plus
def sys(update: Update, context: CallbackContext):
    to_ping = ["APi Core", "PlyTon", "Telegram", "Jikan"]
    pinged_list = ping_func(to_ping)
    pinged_list.insert(2, "")
    uptime = get_readable_time((time.time() - StartTime))

    reply_msg = "Server Status\n"
    reply_msg += "\n".join(pinged_list)
    reply_msg += "\n<b>SERVER ONLiNE:</b> <code>{}</code>".format(uptime)

    update.effective_message.reply_text(
        reply_msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
    )


PING_HANDLER = DisableAbleCommandHandler("ping", ping)
SYS_HANDLER = DisableAbleCommandHandler("sys", sys)

dispatcher.add_handler(PING_HANDLER)
dispatcher.add_handler(SYS_HANDLER)

__command_list__ = ["ping", "sys"]
__handlers__ = [PING_HANDLER, SYS_HANDLER]



# I0BOZXRfU0hFTEwgUHJvamVjdCAjQFlVaV9HQm90IChCWSAtIEBHQm90X05ldHdvcmsp
