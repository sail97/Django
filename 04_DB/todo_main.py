'''
import todo_helper

def main():
    run=1
    todo_helper.create_table()

    while run:
        print("press 1 : To add todo")
        print("press 2 : To read todo")
        print("Press 3 : to update todo")
        print("Press 4 : To delete todo")
        print("press 5 : exit")

        ch=input("Enter your choice: ")

        if ch=='1':
            new_todo=input("Enter your todo: ")
            todo_helper.data_entry(new_todo)
        elif ch=='2':
            todo_helper.read_todos()
        elif ch=='3':
            id = int(input("Enter ID of todo you want to update: "))
            updated_todo=input("Enter updated todo: ")
            todo_helper.update_todo(id,updated_todo)
        elif ch=='4':
            id = int(input("Enter ID of todo you want to delete: "))
            todo_helper.delete_todo(id)
        elif ch=="5":
            run = 0
        else:
            print("Enter a valid option")
    todo_helper.close_connection()

main()

'''