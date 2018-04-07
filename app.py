from flask import Flask, jsonify, request
from reviews import ReviewManager
from users import UserManager

rm = ReviewManager()
um = UserManager()

app = Flask(__name__)

@app.route('/users/login', methods = ['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    return jsonify(
        user_id=um.login(username, password)
    )

@app.route('/users/register', methods = ['POST'])
def register():
    username = request.args.get('username')
    password = request.args.get('password')
    user_id = um.create_account(username, password)
    return jsonify(
        user_id=user_id
    )

@app.route('/reviews/save', methods = ['POST'])
def save_review():
    user_id = request.args.get('user_id')
    review = request.args.get('review')
    grade = request.args.get('grade')
    major = request.args.get('major')
    course = request.args.get('course')
    rm.save_review(major, course, review, user_id)
    um.add_grade(user_id, major, course, grade)
    return "OK"

@app.route('/reviews/obtain', methods = ['GET'])
def obtain_reviews():
    major = request.args.get('major')
    course = request.args.get('course')
    class_reviews = rm.get_reviews(major, course)
    return jsonify(
        reviews=class_reviews
    )

@app.route('/users/info', methods = ['GET'])
def obtain_user_info():
    user_id = request.args.get('user_id')
    return jsonify(
        info=um.get_user_info(user_id)
    )

@app.route('/users/bio', methods = ['POST'])
def set_bio():
    user_id = request.args.get('user_id')
    bio = request.args.get('bio')
    um.add_bio(user_id, bio)
    return "OK"

if __name__ == "__main__":
    app.run()