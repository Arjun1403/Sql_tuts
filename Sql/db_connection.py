import mysql.connector

from .config import database_config


def getConnection():
    mydb = mysql.connector.connect(
        host=database_config['Host'],
        user=database_config['User'],
        password=database_config['Password']
    )

    return mydb
