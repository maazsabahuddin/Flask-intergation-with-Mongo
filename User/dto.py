

class UserDTO:

    def __init__(self, name, email):
        self.data = {'name': name, 'email': email}

    def returnData(self):
        return self.data
