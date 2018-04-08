import pyrebase
import time

class UserManager:

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

    def add_grade(self, user_id, major, course, grade):
        self.firebase.database().child("users").child(user).child(major).child(course).set(grade)

    def get_user_info(self, user_id):
        return self.firebase.database().child("users").child(user_id).get().val()

    def login(self, username, password):
        # returns user_id on success, 0 on failure
        stored_password = self.firebase.database().child("login_info").child(username).child("password").get().val()
        if (stored_password == password):
            return self.firebase.database().child("login_info").child(username).child("user_id").get().val()
        else:
            return 0

    def create_account(self, username, password):
        # note: this doesn't scale as a user_id
        existing_user_id = self.firebase.database().child("login_info").child(username).get().val()
        if (existing_user_id != None):
            return 0
        else:
            user_id = int(time.time())
            self.firebase.database().child("login_info").child(username).child("user_id").set(user_id)
            self.firebase.database().child("login_info").child(username).child("password").set(password)
            return user_id

    def add_bio(self, user_id, bio):
        self.firebase.database().child("users").child(user_id).child("bio").set(bio)
