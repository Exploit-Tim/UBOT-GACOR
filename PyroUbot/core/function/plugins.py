import importlib
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from PyroUbot import bot, ubot
from PyroUbot.core.helpers import PY
from PyroUbot.modules import loadModule
from PyroUbot.core.database import *
from PyroUbot.config import LOGS_MAKER_UBOT
from platform import python_version
from pyrogram import __version__
HELP_COMMANDS = {}


async def loadPlugins():
    modules = loadModule()
    for mod in modules:
        imported_module = importlib.import_module(f"PyroUbot.modules.{mod}")
        module_name = getattr(imported_module, "__MODULE__", "").replace(" ", "_").lower()
        if module_name:
            HELP_COMMANDS[module_name] = imported_module
    print(f"[🤖 ᴜsᴇʀʙᴏᴛ 🤖] [💠 TELAH BERHASIL DIAKTIFKAN! 💠]")
    await bot.send_message(
        LOGS_MAKER_UBOT, 
       f"""                    
<blockquote>» <b><u>[ᴜʟᴛʀᴀ ᴜsᴇʀʙᴏᴛ](https://t.me/ultraroidubot)</u></b> ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :
     <b>ɪᴅ : 5870285414</b>
     <b> ɴᴀᴍᴇ : ᴜʟᴛʀᴀ ᴜsᴇʀʙᴏᴛ
     <b>ᴛᴏᴛᴀʟ ᴍᴏᴅᴜʟᴇs : {len(HELP_COMMANDS)}</b>
     <b>ᴛᴏᴛᴀʟ ᴘᴇɴɢɢᴜɴᴀ : {len(ubot._ubot)}</b>
     <b>ᴜsᴇʀɴᴀᴍᴇ : @ultraroidubot</b></blockquote>
""",
   reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝐔𝐒𝐄𝐑𝐁𝐎𝐓", url="t.me/ultraroidubot"),
                    InlineKeyboardButton("𝐂𝐇𝐀𝐍𝐄𝐋", url="https://t.me/lokontolya"),
                ],
            ]
        ),
    )
    
@PY.CALLBACK("0_cls")
async def _(client, callback_query):
    await callback_query.message.delete()
