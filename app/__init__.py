from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
app.config.update(dict(
    DEBUG = True,
    SECRET_KEY = "FOMIN123",
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'caioagoncalves@gmail.com',
    MAIL_PASSWORD = 'cag0711M@ri',
    SECURITY_EMAIL_SENDER = 'caioagoncalves@gmail.com'
))
mail = Mail(app)


from app.controllers import default
