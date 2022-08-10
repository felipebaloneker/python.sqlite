import DB.db as db

MAIN_MENU = 99

def display_header():
    COLUMNS_NUMBER = 60
    print ("-" * COLUMNS_NUMBER)
    print ("{:^60}".format("TASKS"))
    print ("-" * COLUMNS_NUMBER)
    print ("{:^60}".format("Press 99 to go to main menu, [CTRL + C] to exit"))
    print ("-" * COLUMNS_NUMBER)

def display_task():
    "display registred task list"
    for task in db.get_task():
        check = u'\u2713' if task[2] == 1 else ""

        t = "- [{:>4}] {:<47} {:^3}".format(task[0],task[1], check)
        print(t)
    print("-"*60)

def display_new_task_option():
    new_task_text = input("Describe the task =>")
    print("Adding task ->"+ str(new_task_text))
    if new_task_text != str(MAIN_MENU):
        db.add_task(new_task_text)
