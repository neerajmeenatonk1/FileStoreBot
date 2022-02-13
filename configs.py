# (c) @senuinfinity

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
ɪ'ᴍ ᴀ ᴘᴇʀᴍᴀɴɴᴇɴᴛ ғɪʟᴇʙᴏʀᴇs sᴛᴏʀᴇ!
ᴀʟʟ ɪ ᴡᴀɴᴛ ᴛᴏ ғɪʟᴇ ᴍᴇ, ɪ'ʟʟ ᴘᴜᴛ ᴛʜᴇᴍ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ. ᴀʟsᴏ ᴡᴏʀᴋs ғᴏʀ ᴄʜᴀɴɴᴇʟ. ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ, ɪ ᴡɪʟʟ ᴀᴅᴅ sᴀᴠᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ғɪʟᴇ ɪɴ ᴄʜᴀɴɴᴇʟ & ᴀᴅᴅ sʜᴀʀᴀʙʟᴇ ʙᴜᴛᴛᴏɴ ʟɪɴᴋ.

🤖 ᴍʏ ɴᴀᴍᴇ: [ғɪʟᴇs sᴛᴏʀᴇ ʙᴏᴛ] (ʜᴛᴛᴘs://ᴛ.ᴍᴇ/ {ʙᴏᴛ_ᴜsᴇʀɴᴀᴍᴇ})

📝 ɪ ᴡᴀs ᴍᴀᴅᴇ: [ᴘʏᴛʜᴏɴ𝟹] (ʜᴛᴛᴘs://ᴡᴡᴡ.ᴘʏᴛʜᴏɴ.ᴏʀɢ)

📚 ʟɪʙʀᴀʀʏ: [ᴘʏʀᴏɢʀᴀᴍ] (ʜᴛᴛᴘs://ᴅᴏᴄs.ᴘʏʀᴏɢʀᴀᴍ.ᴏʀɢ)

ɪ ʟɪᴠᴇ ɪɴ ᴛʜᴇ ʜᴇʀᴋᴜ sᴇʀᴠᴇʀ: [ʜᴇʀᴋᴜ] (ʜᴛᴛᴛ://ʜᴇʀᴏᴋᴜ.ᴄᴏᴍ)

👥 ʜᴇʟᴘ ɴᴇᴇᴅs ʜᴇʟᴘ ᴡɪᴛʜ: [ᴛʜᴀɴɪᴍᴀɪ sᴜᴘᴘᴏʀᴛ] (ʜᴛᴛᴘs://ᴛ.ᴍᴇ/ᴛʜᴀɴɪᴍᴀɪsᴜᴘᴘᴏʀᴛ)

📢 ᴍʏ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ: [ᴛʜᴀɴɪᴍᴀɪʙᴏᴛs] (ʜᴛᴛᴘs://ᴛ.ᴍᴇ/ᴛʜᴀɴɪᴍᴀɪʙᴏᴛs)
"""
 ABOUT_DEV_TEXT = ғ """
🧑🏻💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: @sᴀʀʙᴜᴅᴇᴇɴ𝟽𝟾𝟼

ɪ'ᴍ ɢᴏɪɴɢ ᴛᴏ sᴄʜᴏᴏʟ sᴛɪʟʟ. ɪғ ʏᴏᴜ ᴄᴀɴ, ᴅᴏ ᴛʜɪs ᴛᴏ ᴅᴏ ᴛʜɪs.

ʏᴏᴜ sᴀɪᴅ ᴛʜᴀᴛ ɪғ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ᴡᴀs ʙᴀᴅ, ɪᴍᴏᴠᴇ ᴡɪʟʟ ɪᴍᴍᴇᴅɪᴀᴛᴇʟʏ

[ᴅᴏɴᴀᴛᴇ ɴᴏᴡ] (ᴄᴏᴏᴍɪɴɢ sᴏᴏɴ) (ᴘᴀʏᴘᴀʟ)
"""
HOME_TEXT = """
ʜɪ, [ᴛɢ: // ᴜsᴇʀ? ɪᴅ = {}) \ ɴᴛʜɪs {}) \}) \}) \}) \

sᴇɴᴅ ᴍᴇ ғɪʟᴇ ɪ ᴡɪʟʟ ɢɪᴠᴇ sʜᴀʀᴀʙʟᴇ ʟɪɴᴋ. ɪ sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ᴀʟsᴏ! ᴄʜᴇᴄᴋ ᴀʙᴏᴜᴛ ʙᴏᴛ ʙᴜᴛᴛᴏɴ.
"""
