#    Stella (Development)
#    Copyright (C) 2021 - meanii (Anil Chauhan)
#    Copyright (C) 2021 - SpookyGang (Neel Verma, Anil Chauhan)

#    This program is free software; you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by 
#    the Free Software Foundation; either version 3 of the License, or 
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.plugins.connection.connect import connectRedirect
from Stella.plugins.greeting.captcha.button_captcha import \
    buttonCaptchaRedirect
from Stella.plugins.greeting.captcha.text_captcha import textCaptchaRedirect
from Stella.plugins.notes.private_notes import note_redirect
from Stella.plugins.rules.rules import rulesRedirect
# from Stella.plugins.help.help import redirectHelp

START_TEXT = (
    "Heya {mention}! My name is Emcee - I'm here to help you manage your groups! Hit /help to find out more about how to use me to my full potential.\n\n Join my [News Channel](http://t.me/emcee_updates) to get information on all the latest updates."
)

@StellaCli.on_message(custom_filter.command(commands=('start')))
async def start(client, message):
    if (
        len(message.command) == 1
    ):
        if message.chat.type == 'private':
            buttons = [[
                InlineKeyboardButton(
            text="Add Me To Your Chat", url="t.me/emcee_bot?startgroup=true"), 

                ]]
            await message.reply_text(
                START_TEXT.format(mention=message.from_user.mention),
                reply_markup=InlineKeyboardMarkup(buttons),
                disable_web_page_preview=True,
                quote=True
                )

        elif message.chat.type == 'supergroup':
            await message.reply(
                "Heya :) PM me if you have any questions on how to use me!"
            )
    
    if (
        len(message.command) > 1
    ):
        # # help
        # if startCheckQuery(message, StartQuery='help_'):
        #     await redirectHelp(message)
            
        # Captcha Redirect Implementation 
        if startCheckQuery(message, StartQuery='captcha'):
            await buttonCaptchaRedirect(message)
            await textCaptchaRedirect(message)

        # Private Notes Redirect Implementation 
        elif startCheckQuery(message, StartQuery='note'):
            await note_redirect(message)
        
        # Connection Redirect Implementation
        elif startCheckQuery(message, StartQuery='connect'):
            await connectRedirect(message)
        
        # Rules Redirect Implementation
        elif startCheckQuery(message, StartQuery='rules'):
            await rulesRedirect(message)

    

def startCheckQuery(message, StartQuery=None) -> bool:
    if (
        StartQuery in message.command[1].split('_')[0]
        and message.command[1].split('_')[0] == StartQuery
    ):
        return True
    else: 
        return False 
