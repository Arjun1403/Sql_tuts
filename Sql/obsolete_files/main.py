from Sql.execute import Create
from Sql.obsolete_files.delete import Delete
from Sql.obsolete_files.read import Read
from Sql.obsolete_files.update import Update


def main():
    # print('Available Options: C=Create, R=Read, U=Update, D=Delete ')
    createObj = Create()
    createObj.func_CreateData()

    choice = ""

    if choice == 'C':
        createObj = Create()
        createObj.func_CreateData()
    elif choice == 'R':
        readObj = Read()
        readObj.func_ReadData()
    elif choice == 'U':
        updateObj = Update()
        updateObj.func_UpdateData()
    elif choice == 'D':
        deleteObj = Delete()
        deleteObj.func_DeleteData()
    else:
        print('Wrong choice, You are going exist.')


# Call the main function
if __name__ == '__main__':
    main()
