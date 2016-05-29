'''
Controls the login page view.
'''
from flask import Flask
import flask
from flask.helpers import url_for
from flask.templating import render_template
from flask_login import LoginManager, login_user
from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context
from werkzeug.utils import redirect

from login.user import User
from utils.dbUtils import DBConnector


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DBConnector.getDbUri();
app.config['SECRET_KEY'] = 'tinkerbell'
db = SQLAlchemy(app);
loginManager = LoginManager()

class LoginView():
    """
    Class which contains methods for the login page. Although
    at the moment there is no need, I'm trying to keep this class
    as an instantiable object. I'll change all methods to static
    if necessary.
    """
    
    """
    Constructor
    :arg:loginManager: a Flask-Login LoginManager to use for authentication
    """
#     def __init__(self, loginManager):
#         self.loginManager = loginManager
     
    def loginPage(self):
        """
        Returns a rendered template for the login page
        """
        return render_template('login.html')
    
    def performLogin(self):
        username = flask.request.args.get('username')
        password = flask.request.args.get('password')
        if not username or not password:
            return redirect(url_for('login'))
        
        user = User.query.get(username)
        if not user:
            return redirect(url_for('login'))
        if custom_app_context.encrypt(password) == user.passHash:
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            return redirect("restricted")
        return redirect(url_for('login'))
            
            
    