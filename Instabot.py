from instabot import Bot
#username = ""
#password = ""

bot = Bot()
bot.login(username='', password='')
#fiókadatok megszerzése
user_info = bot.get_user_info(username='target_username')
print(user_info)
#felhasználó követáse
bot.follow('target_username')
#5 post likeoldása
bot.like_user_posts('target_username', amount=5)
