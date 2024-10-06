from flask import Flask, request, jsonify, render_template
import instaloader
from config import logins

app = Flask(__name__)

# Creates instance of instaloader
L = instaloader.Instaloader()

# (Optional) Logs in with credentials
L.login(logins['username'], logins['password'])

@app.route('/')
def index():
    return render_template('index.html')  # Renders the HTML file

@app.route('/instagram', methods=['POST'])
def check_followers():
    userquery = request.json.get('username')
    if userquery:
        follower_list = []
        following_list = []

        profile = instaloader.Profile.from_username(L.context, userquery)

        # Returns followers
        followers = profile.get_followers()
        for follower in followers:
            follower_list.append(follower.username)

        # Returns followees
        followings = profile.get_followees()
        for following in followings:
            following_list.append(following.username)

        badfriends = [following for following in following_list if following not in follower_list]
        if not badfriends:
            badfriends.append("None")

        return jsonify({"badfriends": badfriends})
    return jsonify({"error": "Invalid username"}), 400

if __name__ == '__main__':
    app.run(debug=True)
