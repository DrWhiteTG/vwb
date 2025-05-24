from bot import Bot
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647  #Add Db Channel id Here -10000000000

if __name__ == "__main__":
    Bot().run()