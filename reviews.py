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
        self.firebase.database().child(major).child(course).child(user_id).set(review)

    def get_reviews(self, major, course):
        reviews = self.firebase.database().child(major).child(course).get()
        review_dict = {}
        for review in reviews.each():
            review_dict[review.key()] = review.val()
        return review_dict
