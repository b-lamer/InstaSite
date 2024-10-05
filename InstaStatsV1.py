import instaloader
from flask import Flask, request, jsonify

app = Flask(__name__)
#Creates instance of instaloader
L = instaloader.Instaloader()

username = input("Enter your instagram username: ")
password = input("Enter your instagram password: ")

#(Optional) Logs in with credentials, might be required if account is private
L.login(username, password)

@app.route('/instagram', methods=['POST'])
#Loads profile
def checkfollowers():
    userquery = request.json.get('username')
    if userquery:
        follower_list = []
        following_list = []

        profile = instaloader.Profile.from_username(L.context, userquery)

        #Returns followers
        followers = profile.get_followers()
        for follower in followers:
            follower_list.append(follower.username)

        followings = profile.get_followees()
        for following in followings:
            following_list.append(following.username)

        print("These users are not following " + userquery + " back: ")
        badfriends = [following for following in following_list if following not in follower_list]
        if badfriends == []:
            badfriends.append("None")
        return jsonify({"Bad friends: ": badfriends})
    return jsonify({"error": "No username provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)