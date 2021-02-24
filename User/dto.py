import datetime


class UserDTO:

    __id = None
    name = ''
    phone_number = ''
    email = ''
    is_active = False
    is_admin = False
    debit = 0
    credit = 0
    created = datetime.datetime.now()

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.phone_number = kwargs.get('phone_number')
        self.is_active = kwargs.get('is_active')
        self.is_admin = kwargs.get('is_admin')
        self.debit = kwargs.get('debit')
        self.credit = kwargs.get('credit')
        self.created = kwargs.get('created')

    def returndtodata(self):
        data = {'name': self.name, 'email': self.email, 'phone_number': self.phone_number, 'is_active': self.is_active,
                'is_admin': self.is_admin, 'debit': str(self.debit), 'credit': str(self.credit), 'created': self.created}
        return data
