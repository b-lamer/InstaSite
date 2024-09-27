import instaloader

#Creates instance of instaloader
L = instaloader.Instaloader()

#(Optional) Logs in with credentials, might be required if account is private
L.login("xxx", "xxx")

#Loads profile
profile = instaloader.Profile.from_username(L.context, "phichiuww")

#Returns followers
followers = profile.get_followers()

for follower in followers:
    print(follower.username)