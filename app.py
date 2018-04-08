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
    username = request.form.get('username')
    password = request.form.get('password')
    user_id = um.create_account(username, password)
    return jsonify(
        user_id=user_id
    )

@app.route('/reviews/save', methods = ['POST'])
def save_review():
    user_id = request.form.get('user_id')
    review = request.form.get('review')
    grade = request.form.get('grade')
    major = request.form.get('major')
    course = request.form.get('course')
    instructor = request.form.get('instructor')
    difficulty = request.form.get('difficulty')
    learning = request.form.get('learning')
    semester = request.form.get('semester')
    year = request.form.get('year')
    study_hours = request.form.get('study_hours')
    code = request.form.get('code')
    workload = request.form.get('workload')
    rm.save_review(major, course, review, grade, instructor, difficulty, learning, semester, year, study_hours, code, workload, user_id)
    um.add_grade(user_id, major, code, grade)
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

@app.route('/users/major_minors', methods = ['POST'])
def set_majors_minors():
    user_id = request.form.get('user_id')
    major = request.form.get('major')
    minor = request.form.get('minor')
    um.set_major_minor(user_id, major, minor)
    return "OK"

@app.route('/users/bio', methods = ['POST'])
def set_bio():
    user_id = request.form.get('user_id')
    bio = request.form.get('bio')
    um.add_bio(user_id, bio)
    return "OK"

@app.route('/majors/obtain', methods = ['GET'])
def get_majors():
    return jsonify(
        majors=rm.get_majors()
    )

@app.route('/majors/classes/obtain', methods = ['GET'])
def get_classes():
    major = request.args.get('major')
    return jsonify(
        classes=rm.get_classes(major)
    )

if __name__ == "__main__":
    app.run()
