from Sql import db_connection as dbConn;


class Update:
    def func_UpdateData(self):
        # Get the SQL connection
        connection = dbConn.getConnection()
        cursor = connection.cursor()
        cursor.execute("use tutorial")

        id = input('Enter student Id = ')

        try:
            # Fetch the data which needs to be updated
            sql = "Select * From student Where Id = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [id])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t Name\t\t\t Age')
            print('-------------------------------------------')
            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            print('Enter New Data To Update Employee Record ')

            name = input('Enter New Name = ')
            # age = input('Enter New Age = ')
            query = "Update student Set Name = %s Where Id =%s"

            # Execute the update query
            cursor.execute(query, [name, id])
            connection.commit()
            print('Data Updated Successfully')

        except:
            print('Something wrong, please check')

        finally:
            # Close the connection
            connection.close()
