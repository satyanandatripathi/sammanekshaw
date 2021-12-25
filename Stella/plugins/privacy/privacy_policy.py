from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Stella import StellaCli, client, app
from Stella.helper import custom_filter
from pyrogram import filters


main_text = """
**Our contact details**
**Name:** Sam Manekshaw
**Telegram:** https://t.me/menotdeveloper

The bot has been made to **protect** and **preserve** privacy as best as possible.
The proper functioning of the bot is defined as the data required for all the commands in the /help to work as expected.

Our privacy policy may change from time to time. If we make any material changes to our policies, we will place a prominent notice on https://t.me/dotenv.
"""

collect_text = """
**The type of personal information we collect**

We currently collect and process the following information:
    • Telegram UserID, firstname, lastname, username (Note: These are your public telegram details. We do not know your "real" details.)
    • Chat memberships (The list of all chats you have been seen interacting in)
    • Settings or configurations as set through any commands (For example, welcome settings, notes, filters, etc)
"""

why_text = """
**How we get the personal information and why we have it**

Most of the personal information we process is provided to us directly by you for one of the following reasons:
    • You've messaged the bot directly. This can be to read the complete a CAPTCHA, read the documentation, etc.
    • You've opted to save your messages through the bot.

We also receive personal information indirectly, from the following sources in the following scenarios:
    • You're part of a group, or channel, which uses this bot.
"""

wedo_text = """
**What we do with the personal information**

We use the information that you have given us in order to support various bot features. This can include:
    • User ID/username pairing, which allows the bot to resolve usernames to valid user ids.
    • Chat memberships, which allows for federations to know where to ban from, and determine which bans are of importance to you.
    • Storing certain messages that have been explicitly saved. (eg through notes, filters, welcomes, etc)
"""

wedonot_text = """
**What we DO NOT do with the personal information**

We **DO NOT:**
    • store any messages, unless explicitly saved (eg through notes, filters, welcomes etc).
    • use technologies like beacons or unique device identifiers to identify you or your device.
    • knowingly contact or collect personal information from children under 13. If you believe we have inadvertently collected such information, please contact us so we can promptly obtain parental consent or remove the information.
    • share any sensitive information with any other organisations or individuals.
"""

right_text = """
**Rights to process**

Under the General Data Protection Regulation (GDPR), the lawful bases we rely on for processing this information are:
    • Your consent. You are able to remove your consent at any time. You can do this by using the tools provided to delete your data, which will delete any data that isnt critical to bot functionality.
    • We need it to perform a public task. Namely, allowing group or channel admins to protect their chats.
    • We have a legitimate interest: The data collected and retained is essential to the functioning of the bot. Admins add this bot to protect their chats, and certain data is required to guarantee this.
"""

main_button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("What information we collect", callback_data = "collecttext_privacy")
        ],
        [
            InlineKeyboardButton("Why we collect it", callback_data = "whytext_privacy")
        ],
        [
            InlineKeyboardButton("What we do", callback_data = "wedotext_privacy")
        ],
        [
            InlineKeyboardButton("What we DO NOT do", callback_data = "wedonottext_privacy")
        ],
        [
            InlineKeyboardButton("Right to process", callback_data = "righttext_privacy")
        ]
    ]
)

collect_button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("• What information we collect •", callback_data = "collecttext_privacy")
        ],
        [
            InlineKeyboardButton("Why we collect it", callback_data = "whytext_privacy")
        ],
        [
            InlineKeyboardButton("What we do", callback_data = "wedotext_privacy")
        ],
        [
            InlineKeyboardButton("What we DO NOT do", callback_data = "wedonottext_privacy")
        ],
        [
            InlineKeyboardButton("Right to process", callback_data = "righttext_privacy")
        ],
        [
            InlineKeyboardButton("Back", callback_data = "back_privacy")
        ]
    ]
)

why_button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("What information we collect", callback_data = "collecttext_privacy")
        ],
        [
            InlineKeyboardButton("• Why we collect it •", callback_data = "whytext_privacy")
        ],
        [
            InlineKeyboardButton("What we do", callback_data = "wedotext_privacy")
        ],
        [
            InlineKeyboardButton("What we DO NOT do", callback_data = "wedonottext_privacy")
        ],
        [
            InlineKeyboardButton("Right to process", callback_data = "righttext_privacy")
        ],
        [
            InlineKeyboardButton("Back", callback_data = "back_privacy")
        ]
    ]
)

wedo_button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("What information we collect", callback_data = "collecttext_privacy")
        ],
        [
            InlineKeyboardButton("Why we collect it", callback_data = "whytext_privacy")
        ],
        [
            InlineKeyboardButton("• What we do •", callback_data = "wedotext_privacy")
        ],
        [
            InlineKeyboardButton("What we DO NOT do", callback_data = "wedonottext_privacy")
        ],
        [
            InlineKeyboardButton("Right to process", callback_data = "righttext_privacy")
        ],
        [
            InlineKeyboardButton("Back", callback_data = "back_privacy")
        ]
    ]
)

wedonot_button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("What information we collect", callback_data = "collecttext_privacy")
        ],
        [
            InlineKeyboardButton("Why we collect it", callback_data = "whytext_privacy")
        ],
        [
            InlineKeyboardButton("What we do", callback_data = "wedotext_privacy")
        ],
        [
            InlineKeyboardButton("• What we DO NOT do •", callback_data = "wedonottext_privacy")
        ],
        [
            InlineKeyboardButton("Right to process", callback_data = "righttext_privacy")
        ],
        [
            InlineKeyboardButton("Back", callback_data = "back_privacy")
        ]
    ]
)

right_button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("What information we collect", callback_data = "collecttext_privacy")
        ],
        [
            InlineKeyboardButton("Why we collect it", callback_data = "whytext_privacy")
        ],
        [
            InlineKeyboardButton("What we do", callback_data = "wedotext_privacy")
        ],
        [
            InlineKeyboardButton("What we DO NOT do", callback_data = "wedonottext_privacy")
        ],
        [
            InlineKeyboardButton("• Right to process •", callback_data = "righttext_privacy")
        ],
        [
            InlineKeyboardButton("Back", callback_data = "back_privacy")
        ]
    ]
)

@StellaCli.on_callback_query()
async def ud_callback(client: StellaCli, query: CallbackQuery):
    data = query.data
    if data == "privacy#policy":
        await query.message.edit_text(
            text = main_text,
            disable_web_page_preview = True
            reply_markup = main_button
        )
    elif data == "collecttext_privacy":
        await query.message.edit_text(
            text = collect_text,
            reply_markup = collect_button,
        )
    elif data == "whytext_privacy":
        await query.message.edit_text(
            text = why_text,
            reply_markup = why_button
        )
    elif data == "wedotext_privacy":
        await query.message.edit_text(
            text = wedo_text,
            reply_markup = wedo_button
        )
    elif data == "wedonottext_privacy":
        await query.message.edit_text(
            text = wedonot_text,
            reply_markup = wedonot_button
        )
    elif data == "righttext_privacy":
        await query.message.edit_text(
            text = right_text,
            reply_markup = right_button
        )
    elif data == "back_privacy":
        await query.message.edit_text(
            text = main_text,
            reply_markup = main_button
        )
