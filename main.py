import instaloader

username = "nevtelentesztelo21"
password = "zD}GR3X~@U"


bot = instaloader.Instaloader()
#bot.login(user=username, passwd=password)

#Profile allocation
profile = instaloader.Profile.from_username(bot.context, 'kishammel')
#print(profile.get_posts())
"""""
# returns if a proile is private
private = profile.is_private

print(private)

# returns if a profile is business
business = profile.is_business

print(business)
"""""
""""
#Profile data
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers Count: ", profile.followers)
print("Following Count: ", profile.followees)
print("Bio: ", profile.biography)
print("External URL: ", profile.external_url)
"""

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
    print(post)
    bot.download_post(post, target=f"{profile.username}_{index}")

"""

"""""
posts = profile.get_posts()
comments_arr = []

for post in posts:
   print(post.likes)
"""



post = instaloader.Post.from_shortcode(bot.context, 'CBAQLopB6d3')

comments_from_loop_including_answers = []

for comment in post.get_comments():
    comments_from_loop_including_answers.append(comment)
    for answer in comment.answers:
        comments_from_loop_including_answers.append(answer)

print(len(comments_from_loop_including_answers))
print(post.comments)


