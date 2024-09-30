import instaloader

#Creates instance of instaloader
L = instaloader.Instaloader()
username = input("Enter your instagram username: ")
password = input("Enter your instagram password: ")

#(Optional) Logs in with credentials, might be required if account is private
L.login(username, password)

#Loads profile
while True:
    follower_list = []
    following_list = []

    userquery = input("Enter the instagram username you'd like to search: ")
    print("")

    if userquery == "quit":
        break

    profile = instaloader.Profile.from_username(L.context, userquery)

    #Returns followers
    followers = profile.get_followers()
    for follower in followers:
        follower_list.append(follower.username)
    #print(follower_list)
    #print ("\n")

    followings = profile.get_followees()
    for following in followings:
        following_list.append(following.username)
    #print(following_list)
    #print("\n" + "-----------------------------------" + "\n")

    print("These users are not following " + userquery + " back: ")
    badfriends = []
    for following in following_list:
        if following not in follower_list:
            badfriends.append(following)
    if badfriends == []:
        badfriends.append("None")
    print(badfriends)
    print("")