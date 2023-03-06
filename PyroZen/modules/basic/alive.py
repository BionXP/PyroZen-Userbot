# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import time
import asyncio
import os
from gc import get_objects
from datetime import datetime

from config import CMD_HANDLER as cmd
from pyrogram import Client, enums, filters
from pyrogram.types import *
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from PyroZen import CMD_HELP, StartTime, app, ids
from pyrogram.raw.functions import Ping
from PyroZen.utils import get_readable_time
from pyrogram import *
from config import *
from PyroZen import *

OWNER_ID = 1897354060

cmds = [".", "*", "!", "?", "s"]

@Client.on_message(filters.command(["zen", "alive"], cmds) & filters.me)
async def alive(client: Client, message: Message):
    users = 0
    group = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            users += 1
        elif dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            group += 1
    if client.me.id == OWNER_ID:
        status = "**Owner**"
    elif client.me.id in SUDO_ID:
        status = "**Admin**"
    else:
        status = "**Premium**"
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    ping = (datetime.now() - start).microseconds / 1000
    uptime = await get_readable_time((time.time() - StartTime))
    await message.reply(
        f"**ZenUbot**\n"
        f"   <b>Status : {status}</b>\n"
        f"     <b>expires_on:<b>\n"
        f"     <b>Dc_id: <code>{client.me.dc_id}</b>\n"
        f"     <b>Ping_DC:</b> <code>{ping} ms</code>\n"
        f"     <b>Peer_Users:</b> <code>{users} users</code>\n"
        f"     <b>Peer_Group:</b> <code>{group} group</code>\n"
        )
