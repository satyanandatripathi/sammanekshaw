from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Stella import StellaCli
from Stella.helper import custom_filter

@StellaCli.on_message(custom_filter.command(commands=('privacy')))
async def urbanDictionary(client, message):
    chat_id = message.chat.id
    if '-' in str(chat_id):
        await message.reply_text("Use this command in my dm!")
        return
    
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Privacy Policy", callback_data = "privacy#policy")
            ],
            [
                InlineKeyboardButton("Cancel", callback_data = "privacy#cancel")
            ]
        ]
    )
    reply_text = "Select one of the below options for more information about how the bot handles your privacy."
    await message.reply_text(
        text = reply_text,
        reply_markup = reply_markup
    )
    return

@StellaCli.on_callback_query(custom_filter.create(lambda _, __, query: 'privacy#' in query.data))
async def ud_callback(client: StellaCli, callback_query: CallbackQuery):
    message_id = callback_query.message.message_id
    chat_id = callback_query.message.chat.id 
    pro = str(callback_query.data.split('#')[1]) 
    if pro == "cancel":
        text_r = "Privacy deletion request cancelled."
        await StellaCli.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=text_r
        )
