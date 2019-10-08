from Sql import db_connection as dbConn


class Delete:
    def func_DeleteData(self):
        # Get the SQL connection
        connection = dbConn.getConnection()
        cursor = connection.cursor()
        cursor.execute("use tutorial")

        id = input('Enter Employee Id = ')

        try:
            # Get record which needs to be deleted
            sql = "Select * From student Where Id = ?"
            cursor = connection.cursor()
            cursor.execute(sql, [id])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t Name\t\t\t Age')
            print('-------------------------------------------')
            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            confirm = input('Are you sure to delete this record (Y/N)?')

            # Delete after confirmation
            if confirm == 'Y':
                deleteQuery = "Delete From student Where Id = ?"
                cursor.execute(deleteQuery, [id])
                connection.commit()
                print('Data deleted successfully!')
            else:
                print('Wrong Entry')
        except:
            print('Something wrong, please check')
        finally:
            connection.close()