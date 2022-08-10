import DB.db as db
import helpers.messages as msg

def main():
    NEW_TASK = 1
    COMPLETE_TASK = 2

    while True:
        msg.display_header()
        msg.display_task()
        try:
            #display options
            option = int(input("What you want to do? 1 = New Task, 2 = Complete Task =>"))
            if option == NEW_TASK:
                msg.display_new_task_option()
            elif option == COMPLETE_TASK:
                msg.display_task()
            else: 
                print("Invalid Option")
        except ValueError as e:
            print("Invalid Option, Please enter a number: ")
        except Exception:
            exit(0)
if __name__ == "__main__":
    db.create_table_todo()
    main()