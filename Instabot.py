from instabot import Bot
#username = "nevtelentesztelo21"
#password = "zD}GR3X~@U"

bot = Bot()
bot.login(username='nevtelentesztelo21', password='zD}GR3X~@U')
#fiókadatok megszerzése
user_info = bot.get_user_info(username='target_username')
print(user_info)
#felhasználó követáse
bot.follow('target_username')
#5 post likeoldása
bot.like_user_posts('target_username', amount=5)
