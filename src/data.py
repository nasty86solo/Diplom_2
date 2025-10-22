# Набор сообщений/подсказок и допустимых статусов.
# Статус‑коды могут отличаться в окружениях, поэтому в тестах используем разумные диапазоны.
class Msg:
    USER_CREATED = "success"
    USER_EXISTS_SUBSTR = "already exists"
    REQUIRED_FIELDS_SUBSTR = "required"
    LOGIN_SUCCESS = "success"
    INVALID_CREDENTIALS_SUBSTR = "email or password are incorrect"

    NO_INGREDIENTS_SUBSTR = "must be provided"
    INVALID_INGREDIENTS_SUBSTR = "Internal Server Error"

class Status:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    CONFLICT = 409
    SERVER_ERROR = 500
