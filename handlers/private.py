from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Salam dəyərli istifadəçi.
Mən [𝐊𝐇𝐀𝐍](https://t.me/tag1y3v) tərəfindən yaradılmış 𝐊𝐇𝐀𝐍  𝐌𝐔𝐒𝐈𝐂  𝐁𝐎𝐓 musiqi botuyam ♥️
Məni qrupunuza əlavə edərək adminlik verin və playerim olan @KhanMusicAssistant -ı qrupa əlavə edərək musiqilərdən zövq alın**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 İrad, təklif və reklamla bağlı 🛠", url="https://t.me/tag1y3v")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/KhanChat"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/KhanVlog"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Məni qrupunuza əlavə edin ➕", url="https://t.me/Khan_MusicBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Khan Music Bot aktivdir ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/KhanVlog")
                ]
            ]
        )
   )


