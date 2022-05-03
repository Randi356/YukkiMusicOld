from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

stats1 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝐒𝐲𝐬𝐭𝐞𝐦 𝐬𝐭𝐚𝐭𝐬", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="𝐒𝐭𝐨𝐫𝐚𝐠𝐞 𝐬𝐭𝐚𝐭𝐬", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐬", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="𝐌𝐨𝐧𝐠𝐨𝐃𝐁 𝐒𝐭𝐚𝐭𝐬", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐀𝐬𝐢𝐬𝐬𝐭𝐚𝐧𝐭 𝐒𝐭𝐚𝐭𝐬", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝐆𝐞𝐧𝐞𝐫𝐚𝐥 𝐒𝐭𝐚𝐭𝐬", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="𝐒𝐭𝐨𝐫𝐚𝐠𝐞 𝐒𝐭𝐚𝐭𝐬", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐬", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="𝐌𝐨𝐧𝐠𝐨𝐃𝐁 𝐒𝐭𝐚𝐭𝐬", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐀𝐬𝐢𝐬𝐬𝐭𝐚𝐧𝐭 𝐒𝐭𝐚𝐭𝐬", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats3 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝐒𝐲𝐬𝐭𝐞𝐦 𝐒𝐭𝐚𝐭𝐬", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="𝐆𝐞𝐧𝐞𝐫𝐚𝐥 𝐒𝐭𝐚𝐭𝐬", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐬", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="𝐌𝐨𝐧𝐠𝐨𝐃𝐁 𝐒𝐭𝐚𝐭𝐬", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐀𝐬𝐢𝐬𝐬𝐭𝐚𝐧𝐭 𝐒𝐭𝐚𝐭𝐬", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats4 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝐒𝐲𝐬𝐭𝐞𝐦 𝐒𝐭𝐚𝐭𝐬", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="𝐒𝐭𝐨𝐫𝐚𝐠𝐞 𝐒𝐭𝐚𝐭𝐬", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐆𝐞𝐧𝐞𝐫𝐚𝐥 𝐒𝐭𝐚𝐭𝐬", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="𝐌𝐨𝐧𝐠𝐨𝐃𝐁 𝐒𝐭𝐚𝐭𝐬", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐀𝐬𝐢𝐬𝐬𝐭𝐚𝐧𝐭 𝐒𝐭𝐚𝐭𝐬", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats5 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝐒𝐲𝐬𝐭𝐞𝐦 𝐒𝐭𝐚𝐭𝐬", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="𝐒𝐭𝐨𝐫𝐚𝐠𝐞 𝐒𝐭𝐚𝐭𝐬", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐬", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="𝐆𝐞𝐧𝐞𝐫𝐚𝐥 𝐒𝐭𝐚𝐭𝐬", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐀𝐬𝐢𝐬𝐬𝐭𝐚𝐧𝐭 𝐒𝐭𝐚𝐭𝐬", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats6 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝐒𝐲𝐬𝐭𝐞𝐦 𝐒𝐭𝐚𝐭𝐬", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="𝐒𝐭𝐨𝐫𝐚𝐠𝐞 𝐒𝐭𝐚𝐭𝐬", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐬", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="𝐌𝐨𝐧𝐠𝐨𝐃𝐁 𝐒𝐭𝐚𝐭𝐬", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐆𝐞𝐧𝐞𝐫𝐚𝐥 𝐒𝐭𝐚𝐭𝐬", callback_data=f"gen_stats"
            )
        ],
    ]
)


stats7 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Getting Assistant Stats....",
                callback_data=f"wait_stats",
            )
        ]
    ]
)
