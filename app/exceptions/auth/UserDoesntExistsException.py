from app.exceptions.auth.ValidationException import ValidationException


class UserDoesntExistsException(ValidationException):
    ...
