#!/usr/bin/env python3

if __name__ == "__main__":
    bot = Bot("@Thorin_Bot", os.getenv("THORIN_API_TOKEN"))
    bot.run()
