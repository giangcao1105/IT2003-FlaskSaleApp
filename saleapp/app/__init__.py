from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babelex import Babel
import cloudinary

app = Flask(__name__)
app.secret_key = 'DangCuteOc'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost/sale_app?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
login = LoginManager(app=app)
babel = Babel(app=app)

cloudinary.config(could_name='dvw4ctufi', api_key='343499667495141', api_secret='oRuMhhtQvQPTbYSVkzQaQ1Ru0y4')
@babel.localeselector
def load_locale():
    return 'vi'