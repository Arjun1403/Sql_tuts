# import pypyodbc
import mysql.connector


def getConnection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="user368",
        password="Qwerty12345!"
    )
    
    return mydb

# Return the sql connection
# def getConnection():
#     # drivers = [item for item in pypyodbc.drivers()]
#     # driver = drivers[-1]
#     # print("driver:{}".format(driver))
#     # connection = pyodbc.connect(
#     #     "Driver={"+ config.DATABASE_CONFIG["Driver"] +"};Server=" + config.DATABASE_CONFIG[
#     #         "Server"] + ";Database=" + config.DATABASE_CONFIG["Database"] + ";uid ="+ config.DATABASE_CONFIG["UID"] +";pwd="+config.DATABASE_CONFIG["Password"])
#     # connection = pyodbc.connect('DATABASE=test;SOCKET=/var/run/mysqld/mysqld.sock')
#     connection = pyodbc.connect(
#         "driver={ODBC Driver 17 for SQL Server};database=test;SOCKET=/var/run/mysqld/mysqld.sock;server=192.168.3.255,1443;")
#     # connectionpyodbc.connect()
#     return connection
