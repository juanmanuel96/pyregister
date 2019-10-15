from flask_login import UserMixin

class Employee(UserMixin):
    is_authenticated = True
    is_active = True
    is_anonymous = False

    def __init__(self, uid, username, first_name, last_name, account_type, is_approved = False, dark_mode = False):
        self.uid = uid
        self.username = username
        self.first_name = first_name
        self.last_name = last_name,
        self.account_type = account_type
        self.is_approved = is_approved
        self.dark_mode = dark_mode
    
    def get_uid(self):
        return self.uid
    
    def user_to_json(self):
        return {
            'uid':self.uid,
            'username':self.username,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'account_type':self.account_type,
            'is_approved':self.is_approved,
            'dark_mode':self.dark_mode
        }