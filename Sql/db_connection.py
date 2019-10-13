# import mysql.connector
import pymysql
from .config import database_config


def getConnection():
    mydb = pymysql.connect(
        host=database_config['Host'],
        user=database_config['User'],
        passwd=database_config['Password']
    )

    return mydb