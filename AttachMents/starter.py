from HelpFile.helper import start_text, help_text
from config import bot
from telethon import events

class start():

    @bot.on(events.NewMessage(pattern=r"^/start$|^/start@Anime_Gallery_Robot"))
    async def event_handler_start(_, e: events):
        TheVenomXD = -1001791685690
        user = e.from_user.id
        try:
            await client.get_chat_member(TheVenomXD, user)
        except UserNotParticipant:
            return await message.reply_text("You need to join @channel username to use me.", disable_web_page_preview=True)
            await bot.send_message(
                events.chat_id,
                start_text,
                file='https://tenor.com/view/chika-fujiwara-kaguya-sama-love-is-war-anime-wink-smile-gif-18043249'
            )

    @bot.on(events.NewMessage(pattern=r"^/help$|^"))
    async def event_handler_help(event):
        await bot.send_message(
            event.chat_id,
            help_text
            )












