import sqlite3
import json


def create_table_users():  # if it is nesesary
    conn = sqlite3.connect("userdatabase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users
                      (name text, info text)
                   """)
    conn.commit()


def create_new_user(name):
    conn = sqlite3.connect("userdatabase.db")
    cursor = conn.cursor()
    if not is_user_in_table(name):
        sql = "INSERT INTO users ('name', 'info') VALUES (?, ?)"
        data = (name, json.dumps([]))
        cursor.execute(sql, data)
        conn.commit()


def is_user_in_table(name):  # True - in table; False - not in table
    if getinfo(name) == None:
        return False
    else:
        print("also in table")
        return True


def getinfo(name):
    conn = sqlite3.connect("userdatabase.db")
    cursor = conn.cursor()
    sql = "SELECT info FROM users WHERE name=?"
    cursor.execute(sql, [(name)])
    x = cursor.fetchone()
    if x == None:
        print('no such name: ' + str(name) + ' (getinfo)')
        return None
    else:
        return json.loads(x[0])


def create_new_dvor_for_user(name, id): # 2 - no user, 1 - user has this  dvor, 0 - updated
    conn = sqlite3.connect("userdatabase.db")
    cursor = conn.cursor()
    change = getinfo(name)
    if change == None:
        print('no such name: '+str(name)+' (create_new_dvor_for_user)')
        return 2
    else:
        for x in change:
            if x == id:
                print('this dvor is olredy exists')
                return 1
        change.append(id)
        sql = 'UPDATE users SET info = ? WHERE name = ?'
        cursor.execute(sql, ((json.dumps(change)), name))
        conn.commit()
        return 0


def delete_users_dvor(name, id): # 2 - no user, 1 - no dvor , 0 - updated
    conn = sqlite3.connect("userdatabase.db")
    cursor = conn.cursor()
    info = getinfo(name)
    if info == None:
        print('no such name: '+str(name)+' (delete_users_dvor)')
        return 2
    else:
        flag = 0
        for x in info:
            if x == id:
                info.remove(x)
                flag = 1
        if flag == 1:
            sql = 'UPDATE users SET info = ? WHERE name = ?'
            cursor.execute(sql, ((json.dumps(info)), name))
            conn.commit()
            return 0
        else:
            print('no such dvor_id: '+str(id)+' (delete_users_dvor)')
            return 1


def delete_user(name):
    conn = sqlite3.connect("userdatabase.db")
    cursor = conn.cursor()
    sql = "DELETE FROM users WHERE name = ?"
    cursor.execute(sql, [name])
    conn.commit()
    print(str(name)+" deleted")


create_table_users()
delete_user('vasy')
create_new_user("vasy")
print(getinfo('vasy'))
create_new_dvor_for_user('vasy', '1')
print(getinfo('vasy'))
delete_users_dvor('vasy', '1')
print(getinfo('vasy'))
