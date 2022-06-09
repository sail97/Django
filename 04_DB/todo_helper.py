'''
import sqlite3

# database name
db = 'my_todos.db'
# make connection
con = sqlite3.connect(db)

# creating a cursor to execute all the commands
cur = con.cursor()

# creating a table
def create_table():
    # create a table if not exists table_name (id INTEGER PRIMARY KEY AUTOINCREMENT ,taskname TEXT ')
    sql = 'CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT ,taskname TEXT) '
    cur.execute(sql)
    cur.execute("pragma table_info('todos')");

# Enter a todo
def data_entry(todo):
    # insert into table_name(column_name) values(column_values)
    cur.execute("INSERT INTO todos(taskname) values(?)",[todo])
    print("todo added successfully")
    con.commit()

# Read todos
def read_todos():
    #select*from table_name
    #select column_name from table_name
    cur.execute("SELECT id,taskname from todos")
    for row in cur.fetchall():
        #print(f'{row[0]} -----> {row[1]}')
        print(row)


# Update a todo
def update_todo(ind,updated_todo):
    # update table_name set column_name=new_name where id = index
    cur.execute("UPDATE todos SET taskname = (?) where id = (?)",[updated_todo,ind])
    print("todo updated successfully")
    con.commit()

# Delete a todo
def delete_todo(ind):
    # delete from table_name where id = 
    cur.execute("DELETE FROM todos WHERE id = (?)",[ind])
    print("todo deleted successfully")
    con.commit()

# close the connection
def close_connection():
    cur.close()
    con.close()    


'''