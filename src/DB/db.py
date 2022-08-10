import sqlite3
#connect in database
conn = sqlite3.connect("src/DB/todo-app.db")

def create_table_todo():
    "create table where not exists "
    cursor = conn.cursor()
    create = """
        create table if not exists task (
        cd_task integer primary key autoincrement,
        task text,
        complete integer
    )
    """
    cursor.execute(create)

def add_task(task):
    "add one task"
    conn.execute("insert into task (task,complete) values(?, 0)",(task,))
    conn.commit()

def delete_task(cd_task):
    conn.execute("delete from task where cd_task = ?",(cd_task,))
    conn.commit()

def complete_task(cd_task):
    "mark task as complete"
    conn.execute("update task set complete = 1 where cd_task = ?",(cd_task,))
    conn.commit()

def get_task():
    return conn.execute("select cd_task, task, complete from task")