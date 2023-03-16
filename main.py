import instaloader

username = "nevtelentesztelo21"
password = "zD}GR3X~@U"


bot = instaloader.Instaloader()
bot.login(user=username, passwd=password)
#Profile allocation
profile = instaloader.Profile.from_username(bot.context, 'kishammel')

#Profile data
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers Count: ", profile.followers)
print("Following Count: ", profile.followees)
print("Bio: ", profile.biography)
print("External URL: ", profile.external_url)


"""
#followers
followers = [follower.username for follower in profile.get_followers()]
followers_df = pd.DataFrame(followers)
followers_df.to_csv('followers.csv', index=True)
"""

"""
#following
#followings = [followee.username for followee in profile.get_followees()]
#followings_df = pd.DataFrame(followings)
#followings_df.to_csv('followings.csv', index=False)
"""

"""
#Downloading any public accounts posts
posts = profile.get_posts()
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")
"""

