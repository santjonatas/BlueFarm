from app.exceptions.auth.ValidationException import ValidationException


class UserAlreadyExistsException(ValidationException):
    ...
