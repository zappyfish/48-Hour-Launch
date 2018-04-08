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

    def save_review(self, major, course, review, user_id):
        self.firebase.database().child("all_majors").child(major).child("courses").child(course).child("reviews").child(user_id).set(review)

    def get_reviews(self, major, course):
        reviews = self.firebase.database().child("all_majors").child(major).child("courses").child(course).child("reviews").get()
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
