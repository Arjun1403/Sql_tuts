from main_connection import connect
from prettytable import PrettyTable
from PIL import Image, ImageTk
from tkinter import *
import os


class Execute:
    def func_run(self, query):
        connection, cursor = connect()
        to_continue = True

        while to_continue:
            # Get the sql connection
            if not query:
                query = input('Enter query = ')

            try:
                if query[-1] != ";":
                    raise Exception("enter semicolon")

                cursor.execute(query[:-1])

                # print(cursor.column_names)
                if cursor.description:
                    print('-------------------------------------------')
                    output_string = '-------------------------------------------\n'
                    fields = ",".join(map(lambda column: str(column[0]), cursor.description)).split(",")
                    table = PrettyTable(field_names=fields, border=True, padding_width=3)
                    output_string += '\n-------------------------------------------\n'
                    for row in cursor:
                        print("    ".join(map(str, row)))

                        row = ",".join(map(lambda column: str(column), row)).split(",")
                        table.add_row(row)
                        output_string += "\n"
                    output_string += '\n -------------------------------------------\n'

                    print('-------------------------------------------')
                    print(table)
                    # Commit the data
                    connection.commit()
                    output_string += "\n Data Saved Successfully"
                    print('Data Saved Successfully')
                    return table
                connection.commit()
                return "\n Data Saved Successfully"

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
