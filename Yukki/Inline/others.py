from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import db_mem


def others_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 1
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐋𝐲𝐫𝐢𝐜𝐬",
                callback_data=f"lyrics {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐘𝐨𝐮 𝐏𝐥𝐚𝐲𝐋𝐢𝐬𝐭",
                callback_data=f"your_playlist {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="𝐆𝐫𝐨𝐮𝐩 𝐏𝐥𝐚𝐲𝐋𝐢𝐬𝐭",
                callback_data=f"group_playlist {videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐀𝐮𝐝𝐢𝐨/𝐕𝐢𝐝𝐞𝐨",
                callback_data=f"audio_video_download {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐁𝐚𝐜𝐤",
                callback_data=f"pr_go_back_timer {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="𝐂𝐥𝐨𝐬𝐞",
                callback_data=f"close",
            ),
        ],
    ]
    return buttons


def download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐆𝐞𝐭 𝐀𝐮𝐝𝐢𝐨",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="𝐆𝐞𝐭 𝐕𝐢𝐝𝐞𝐨",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐁𝐚𝐜𝐤", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="𝐂𝐥𝐨𝐬𝐞", callback_data=f"close"),
        ],
    ]
    return buttons
