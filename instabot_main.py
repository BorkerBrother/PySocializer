import time

from user import insta_username, insta_password
import instabot

bot = instabot.Bot()
time.sleep(2)
bot.login(username="insta_username", password="insta_password")
time.sleep(2)

