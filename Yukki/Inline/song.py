from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def song_markup(videoid, duration, user_id, query, query_type):
    buttons = [
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"song_right B|{query_type}|{query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝",
                callback_data=f"qwertyuiopasdfghjkl {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"song_right F|{query_type}|{query}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐂𝐥𝐨𝐬𝐞",
                callback_data=f"forceclose {query}|{user_id}",
            )
        ],
    ]
    return buttons


def song_download_markup(videoid, user_id):
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
                text="𝐂𝐥𝐨𝐬𝐞",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons
