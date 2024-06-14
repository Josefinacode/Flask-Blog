from secrets import token_hex

SECRET_KEY = token_hex(16)
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'