import pyrebase

class ReviewManager:
    config = {
        "apiKey": "AIzaSyACItb_I9bZ933z1kVBSK_hwBarqbHAalQ",
        "authDomain": "hourlaunch.firebaseapp.com",
        "databaseURL": "https://hourlaunch.firebaseio.com",
        "projectId": "hourlaunch",
        "storageBucket": "hourlaunch.appspot.com",
        "messagingSenderId": "299028938869"
    }

    def __init__(self):
        self.firebase = pyrebase.initialize_app(self.config)

    def save_review(self, major, course, review, grade, instructor, difficulty, learning, semester, year, study_hours, code, user_id):
        self.firebase.database().child("reviews").child("all_majors").child(major).child("courses").child(code).child("reviews").child(user_id).child("code").set(code)
        self.firebase.database().child("reviews").child("all_majors").child(major).child("courses").child(code).child("reviews").child(user_id).child("major").set(major)
        self.firebase.database().child("reviews").child("all_majors").child(major).child("courses").child(code).child("reviews").child(user_id).child("review").set(review)
        self.firebase.database().child("reviews").child("all_majors").child(major).child("courses").child(code).child("reviews").child(user_id).child("grade").set(grade)
        self.firebase.database().child("reviews").child("all_majors").child(major).child("courses").child(code).child("reviews").child(user_id).child("instructor").set(instructor)
        self.firebase.database().child("reviews").child("all_majors").child(major).child("courses").child(code).child("reviews").child(user_id).child("difficulty").set(difficulty)
        self.firebase.database().child("reviews").child("all_majors").child(major).child("courses").child(code).child("reviews").child(user_id).child("learning").set(learning)
        self.firebase.database().child("reviews").child("all_majors").child(major).child("courses").child(code).child("reviews").child(user_id).child("semester").set(semester)
        self.firebase.database().child("reviews").child("all_majors").child(major).child("courses").child(code).child("reviews").child(user_id).child("year").set(year)
        self.firebase.database().child("reviews").child("all_majors").child(major).child("courses").child(code).child("reviews").child(user_id).child("study_hours").set(study_hours)
        self.firebase.database().child("reviews").child("all_majors").child(major).child("courses").child(code).child("reviews").child(user_id).child("code").set(code)

    def get_reviews(self, major, course):
        reviews = self.firebase.database().child("reviews").child("all_majors").child(major).child("courses").child(course).child("reviews").get()
        review_dict = {}
        for review in reviews.each():
            review_dict[review.key()] = review.val()
        return review_dict

    def get_majors(self):
        return self.firebase.database().child("all_majors").get().val()

    def add_major(self, major):
        self.firebase.database().child("all_majors").child(major).child("name").set(major)

    def get_classes(self, major):
        return self.firebase.database().child("all_majors").child(major).child("courses").get().val()

    def add_class(self, major, course):
        self.firebase.database().child("all_majors").child(major).child("courses").push(course)
