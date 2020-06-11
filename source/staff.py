from .libraries import UserMixin, current_app

class Staff(UserMixin):
    is_authenticated = True
    is_active = True
    is_anonymous = False

    def __init__(self, eid, username, first_name, last_name, account_type, is_approved = False):
        self.eid = eid
        self.username = username
        self.first_name = first_name
        self.last_name = last_name,
        self.account_type = account_type
        self.is_approved = is_approved
    
    def get_uid(self):
        return self.eid
    
    def user_to_json(self):
        return {
            'uid':self.eid,
            'username':self.username,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'account_type':self.account_type,
            'is_approved':self.is_approved
        }
    
    # Static Method for geting the user to be used by Login Manager
    @staticmethod
    def get_user(uid=0):
        if uid == 0:
            pass
        else:
            collection = current_app.mongo_flask.set_Collection('users')
            return collection.find_one({'eid' : uid})
