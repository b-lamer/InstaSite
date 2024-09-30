import instaloader
from config import logins

userquery = ""
#Creates instance of instaloader
L = instaloader.Instaloader()

#(Optional) Logs in with credentials, might be required if account is private
L.login(logins['username'], logins['password'])

#Loads profile
while userquery != "quit":
    follower_list = []
    following_list = []

    userquery = input("Enter the instagram username you'd like to search: ")

    profile = instaloader.Profile.from_username(L.context, userquery)

    #Returns followers
    followers = profile.get_followers()
    for follower in followers:
        follower_list.append(follower.username)
    print(follower_list)

    followings = profile.get_followees()
    for following in followings:
        following_list.append(following.username)
    print(following_list)