from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="𝐀𝐮𝐝𝐢𝐨 𝐐𝐮𝐚𝐥𝐢𝐭𝐲", callback_data="AQ"),
            InlineKeyboardButton(text="𝐀𝐮𝐝𝐢𝐨 𝐕𝐨𝐥𝐮𝐦𝐞", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="𝐀𝐮𝐭𝐡𝐨𝐭𝐢𝐳𝐞𝐝 𝐔𝐬𝐞𝐫", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="𝐃𝐚𝐬𝐡𝐛𝐨𝐚𝐫𝐝", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="𝐂𝐥𝐨𝐬𝐞", callback_data="close"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐌𝐞𝐧𝐮", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐌𝐞𝐧𝐮", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐌𝐞𝐧𝐮", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐌𝐞𝐧𝐮", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐌𝐞𝐧𝐮", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐌𝐞𝐧𝐮", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐌𝐞𝐧𝐮", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐌𝐞𝐧𝐮", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="𝐀𝐮𝐝𝐢𝐨 𝐐𝐮𝐚𝐥𝐢𝐭𝐲", callback_data="AQ"),
            InlineKeyboardButton(text="𝐀𝐮𝐝𝐢𝐨 𝐕𝐨𝐥𝐮𝐦𝐞", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐔𝐬𝐞𝐫", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="𝐃𝐚𝐬𝐡𝐛𝐨𝐚𝐫𝐝", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="𝐂𝐥𝐨𝐬𝐞", callback_data="close"),
            InlineKeyboardButton(text="𝐁𝐚𝐜𝐤", callback_data="okaybhai"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐑𝐞𝐬𝐞𝐭 𝐀𝐮𝐝𝐢𝐨 𝐕𝐨𝐥𝐮𝐦𝐞", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="𝐋𝐨𝐰 𝐕𝐨𝐥", callback_data="LV"),
            InlineKeyboardButton(text="𝐌𝐞𝐝𝐢𝐮𝐦 𝐕𝐨𝐥", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="𝐇𝐢𝐠𝐡 𝐕𝐨𝐥", callback_data="HV"),
            InlineKeyboardButton(text="𝐀𝐦𝐩𝐥𝐢𝐟𝐢𝐞𝐝 𝐕𝐨𝐥", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="𝐂𝐮𝐬𝐭𝐨𝐦 𝐕𝐨𝐥𝐮𝐦𝐞", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="𝐁𝐚𝐜𝐤", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="𝐂𝐮𝐬𝐭𝐨𝐦 𝐕𝐨𝐥𝐮𝐦𝐞", callback_data="AV")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="𝐄𝐯𝐞𝐫𝐲𝐨𝐧𝐞", callback_data="EVE"),
            InlineKeyboardButton(text="𝐀𝐝𝐦𝐢𝐧𝐬", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="𝐀𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐔𝐬𝐞𝐫 𝐋𝐢𝐬𝐭𝐬", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="𝐁𝐚𝐜𝐤", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="𝐔𝐩𝐭𝐚𝐦𝐞", callback_data="UPT"),
            InlineKeyboardButton(text="𝐑𝐚𝐦", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="𝐂𝐩𝐮", callback_data="CPT"),
            InlineKeyboardButton(text="𝐃𝐢𝐬𝐤", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="𝐁𝐚𝐜𝐤", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons
