from flask import Flask, request, jsonify, render_template
import instaloader
from functools import wraps

app = Flask(__name__)

# Global Instagram loader instance
instagram_loader = None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if instagram_loader is None:
            return jsonify({"error": "Please login first"}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    global instagram_loader
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    try:
        instagram_loader = instaloader.Instaloader()
        instagram_loader.login(username, password)
        return jsonify({"message": "Login successful"})
    except Exception as e:
        instagram_loader = None
        return jsonify({"error": str(e)}), 401

@app.route('/logout', methods=['POST'])
def logout():
    global instagram_loader
    instagram_loader = None
    return jsonify({"message": "Logged out successfully"})

@app.route('/instagram', methods=['POST'])
@login_required
def check_followers():
    global instagram_loader
    userquery = request.json.get('username')
    if not userquery:
        return jsonify({"error": "Invalid username"}), 400

    try:
        follower_list = []
        following_list = []

        profile = instaloader.Profile.from_username(instagram_loader.context, userquery)

        # Returns followers
        followers = profile.get_followers()
        for follower in followers:
            follower_list.append(follower.username)

        # Returns people the user is following
        followings = profile.get_followees()
        for following in followings:
            following_list.append(following.username)

        # Checks who is not following the user back
        badfriends = [following for following in following_list if following not in follower_list]
        
        return jsonify({"badfriends": badfriends})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)