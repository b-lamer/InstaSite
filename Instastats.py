import instaloader
from config import logins

userquery = ""
#Creates instance of instaloader
L = instaloader.Instaloader()

#(Optional) Logs in with credentials, might be required if account is private
L.login(logins['username'], logins['password'])

#Loads profile
while userquery != "quit":
    userquery = input("Enter the instagram username you'd like to search: ")

    profile = instaloader.Profile.from_username(L.context, userquery)

    #Returns followers
    followers = profile.get_followers()

    for follower in followers:
        print(follower.username)