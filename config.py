from secrets import token_hex

SECRET_KEY = token_hex(16)
SQLALCHEMY_DATABASE_URI = 'postgres://blog_user_db_user:aYcsq2E5YPHCn7JIK7duSpD0QSAXNrX5@dpg-cpm8c5qju9rs738mhnhg-a.oregon-postgres.render.com/blog_user_db'