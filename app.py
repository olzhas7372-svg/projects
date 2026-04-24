from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt, datetime

app = Flask(__name__)
CORS(app)

SECRET = "secret123"

# ================= JWT =================
def create_token(user_id):
    return jwt.encode({
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }, SECRET, algorithm="HS256")


# ================= AUTH =================
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if data["username"] == "admin":
        return jsonify({"token": create_token(1)})
    return jsonify({"error": "wrong"})


# ================= ADS =================
ads = [
    {"title": "iPhone", "description": "Good phone"},
    {"title": "BMW", "description": "Car"}
]

@app.route("/ads")
def get_ads():
    return jsonify(ads)


# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)
