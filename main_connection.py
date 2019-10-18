import pymysql

from Sql.config import database_config

def connect():
    connection = pymysql.connect(database_config["Host"], database_config["User"], database_config["Password"],
                                 database_config['DatabaseName'])
    cur = connection.cursor()
    return connection, cur

