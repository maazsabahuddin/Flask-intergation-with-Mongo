

class UserException:

    status_code = 400
    message = ""

    def __init__(self, status_code=status_code, message=message):
        self.status_code = status_code
        self.message = message


class TokenException(UserException, Exception):
    pass


class MissingBody(UserException, Exception):
    pass


class InvalidArguments(UserException, Exception):
    pass


class NotANumber(UserException, Exception):
    pass
