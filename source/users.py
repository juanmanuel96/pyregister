from .libraries import UserMixin

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
        return self.uid
    
    def user_to_json(self):
        return {
            'uid':self.eid,
            'username':self.username,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'account_type':self.account_type,
            'is_approved':self.is_approved
        }