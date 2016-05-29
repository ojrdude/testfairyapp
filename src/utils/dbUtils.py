"""
Utilities for database connection
"""
import os
import pymysql
from fairygeneration.FairyImage import FairyImageGen

class DBConnector():
    
    @staticmethod
    def getConnection():
        """
        Get a connection to the DB. Which DB is connected will depend
        on the environment.
        :return: a connection to the correct database
        """
        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
            con = pymysql.connect(
                            host='104.197.55.21',
                            unix_socket='testflask-1315:fairydb',
                            user='root',
                            passwd='TestFlask',
                            database='My_Fairy_Kingdom')
        else:
        
            con = pymysql.connect(host='localhost',
                                      user=FairyImageGen.LOCAL_DB_USERNAME,
                                      passwd='TestFlask',
                                      database='My_Fairy_Kingdom',
                                      charset='utf8mb4',
                                      cursorclass=pymysql.cursors.DictCursor)
            
        return con
    
    @staticmethod
    def getDbUri():
        """
        Return the correct URI for the DB. Intended for use with Flask
        SQL alchemy. Returns the correct URI depending on the platform.
        :return: The URI for the DB.
        """
        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
            return "mysql://root:TestFlask@104.197.55.21/My_Fairy_Kingdom"
        else:
            return "mysql://{}:TestFlask@localhost/My_Fairy_Kingdom".format(FairyImageGen.LOCAL_DB_USERNAME)