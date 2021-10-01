import json
import os
from Bot import Bot
import jishaku
from bot_utils.Keep_alive import keep_alive

with open("./bot_utils/config.json") as f:
    config = json.load(f)

if __name__ == "__main__":

    keep_alive()
    bot = Bot()  # subclassing commands.Bot
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename} cog loaded")
    bot.load_extension(
        "jishaku"
    )  # jishaku is tool that allow bot developers to do a lot of stuff
    print("All cogs have been successfully loaded")

    bot.run(os.getenv("Token"), reconnect=True)
