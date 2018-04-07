from flask import Flask, jsonify, request
from reviews import ReviewManager

rm = ReviewManager()

app = Flask(__name__)

@app.route('/users/login', methods = ['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    return jsonify(
        user_id=um.login(username, password)
    )

@app.route('/users/register', methods = ['POST'])
    username = request.args.get('username')
    password = request.args.get('password')
    user_id = um.create_account(username, password)
    if user_id != 0:
        return jsonify(
            user_id=user_id
        )
    else:
        return jsonify(
            user_id=0
        )

@app.route('/reviews/save', methods = ['POST'])
    user_id = request.args.get('user_id')
    req
    return "OK"

@app.route('/reviews/obtain', methods = ['GET'])
    class_reviews = rm.get_reviews()
    return jsonify(
        reviews=class_reviews
    )

if __name__ == "__main__":
    app.run()
