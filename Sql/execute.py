from Sql import db_connection as dbConn


class Execute:
    def func_run(self,query):
        to_continue = True

        while to_continue:
            connection = dbConn.getConnection()
            cursor = connection.cursor()
            cursor.execute("use tutorial")
            # Get the sql connection
            if not query:
                query = input('Enter query = ')

            try:
                if query[-1] != ";":

                    raise Exception("enter semicolon")


                cursor.execute(query[:-1])

                print(cursor.column_names)

                print('-------------------------------------------')
                output_string = '-------------------------------------------\n'
                output_string += "    ".join(map(str, cursor.column_names))
                output_string += '\n-------------------------------------------\n'
                for row in cursor:
                    print("    ".join(map(str, row)))
                    output_string += "    ".join(map(str, row))
                    output_string += "\n"
                output_string += '\n -------------------------------------------\n'

                print('-------------------------------------------')

                # Commit the data
                connection.commit()
                output_string += "\n Data Saved Successfully"
                print('Data Saved Successfully')
                return output_string
                # y_or_n = input("wanna continue (y/n) \n")
                # if y_or_n.lower() == "y":
                #     to_continue = True
                # else:
                #     to_continue = False


            except Exception as e:
                print(e)
                print('Something wrong, please check')

                return str(e) + "\n" + "Something wrong, please check"

            finally:
                # Close the connection
                connection.close()


execute_sql = Execute()
