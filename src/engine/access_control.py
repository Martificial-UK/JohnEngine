# access_control.py
class AccessControl:
    def __init__(self):
        self.roles = {}
    def add_user(self, user, role):
        self.roles[user] = role
    def check(self, user, required_role):
        return self.roles.get(user) == required_role
