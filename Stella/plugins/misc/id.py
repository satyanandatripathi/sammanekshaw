from asyncio import Lock

from pyrogram import filters
from Stella import app, eor


@app.on_message(filters.command("id"))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.message_id
    reply = message.reply_to_message

    text = f"**[Message ID:]({message.link})** `{message_id}`\n"
    text += f"**[Your ID:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[User ID:](tg://user?id={user_id})** `{user_id}`\n"
        except Exception:
            return await eor(message, text="This user doesn't exist.")

    text += f"**[Chat ID:](https://t.me/{chat.username})** `{chat.id}`\n\n"
    if not getattr(reply, "empty", True):
        text += (
            f"**[Replied Message ID:]({reply.link})** `{reply.message_id}`\n"
        )
        text += f"**[Replied User ID:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`"

    await eor(
        message,
        text=text,
        disable_web_page_preview=True,
        parse_mode="md",
    )
