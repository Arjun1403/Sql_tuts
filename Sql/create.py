from Sql import db_connection as dbConn


class Create:
    def func_CreateData(self):
        to_continue = True

        while (to_continue):
            connection = dbConn.getConnection()
            cursor = connection.cursor()
            cursor.execute("use tutorial")
            # Get the sql connection


            # name = input('Enter Name = ')
            query = input('Enter query = ')



            try:
                if query[-1] != ";":
                    raise Exception("enter semicolon")

                # cursor.execute("SHOW TABLES")
                # cursor.execute("INSERT INTO Employee VALUES (1, 'banana')")

                # query = "Insert Into Employee(id, name) Values(%s,%s)"

                # Execute the sql query
                cursor.execute(query[:-1])

                print(cursor.column_names)
                ""
                print('\\')
                print('-------------------------------------------')
                for row in cursor:
                    print(row[0])
                print('-------------------------------------------')

                # Commit the data
                connection.commit()
                print('Data Saved Successfully')
                y_or_n = input("wanna continue (y/n) \n")
                if y_or_n.lower() == "y":
                    to_continue = True
                else:
                    to_continue = False

            except Exception as e:
                print(e)
                print('Something wrong, please check')

            finally:
                # Close the connection
                connection.close()
