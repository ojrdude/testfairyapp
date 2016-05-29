""""
Definition of user for flask authentication.
"""
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from utils.dbUtils import DBConnector


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = DBConnector.getDbUri();
# app.config['SECRET_KEY'] = 'tinkerbell'
db = SQLAlchemy(app);
loginManager = LoginManager()


class User(SQLAlchemy(app).Model):
    """
    A class that represents a user in the application.
    """
    __tableName = 'users'
    id = db.Column('username', db.String(20), primary_key=True)
    passHash = db.Column('passhash', db.String(67))
    authenticated = db.Column('authenticated', db.Boolean)
    
    def is_active(self):
        """
        Currently, all users are 'active'
        """
        return True
        
    def is_autheticated(self):
        """
        Checks the "authenticated" column for this user in the db.
        """
        return self.authenticated;
    
    def get_id(self):
        """
        Returns the ID for the user.
        """
        return self.id
    
    def is_anonymous(self):
        """
        No support for annonymous users
        """
        return False