import instaloader

username = ""
password = ""


bot = instaloader.Instaloader()
#bot.login(user=username, passwd=password)

#Profile allocation
publicprofile = instaloader.Profile.from_username(bot.context, 'brigiuhlar')
privateprofile = instaloader.Profile.from_username(bot.context, 'klaaa_xx')
businessprofile = instaloader.Profile.from_username(bot.context, 'kishammel')

print("Publikus fiók")
#print(publicprofile.get_comments())

print("Privát fiók")
#print(privateprofile.get_posts())
print("Business fiók")
#print(businessprofile.get_posts())
#Explore post

"""
explore_posts= bot.get_explore_posts()
for post in explore_posts:
    # Print the post's caption and number of likes
    print(f"Caption: {post.caption}")
    print(f"Number of likes: {post.likes}")
    print()
 """
"""
#Feed posts
feed_posts = bot.get_feed_posts()

# Iterate over the feed posts
for post in feed_posts:
    # Print the post's caption and number of likes
    print(f"Caption: {post.caption}")
    print(f"Number of likes: {post.likes}")
    print()
 """
"""
#get_likes
post_url = "https://www.instagram.com/p/CQ56bwHhvbj/"
post = instaloader.Post.from_shortcode(bot.context, post_url)

# Retrieve the likes for the post
likes = post.get_likes()

# Iterate over the likes
for like in likes:
    # Print the username of the user who liked the post
    print(like.username)

 """
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


""""
post = instaloader.Post.from_shortcode(bot.context, 'CBAQLopB6d3')

comments_from_loop_including_answers = []

for comment in post.get_comments():
    comments_from_loop_including_answers.append(comment)
    for answer in comment.answers:
        comments_from_loop_including_answers.append(answer)

print(len(comments_from_loop_including_answers))
print(post.comments)
"""


