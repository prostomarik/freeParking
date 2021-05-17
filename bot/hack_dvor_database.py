import sqlite3
import json


def create_table_cameras():  # if it is nesesary
    conn = sqlite3.connect("cameradatabase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS cameras
                      (camera_id text, info text, schema text, latest text)
                   """)
    conn.commit()


def create_new_camera(id, info, schema):
    conn = sqlite3.connect("cameradatabase.db")
    cursor = conn.cursor()
    if not is_id_in_table(id):
        sql = "INSERT INTO cameras ('camera_id', 'info', 'schema', 'latest') VALUES (?, ?, ?, ?)"
        data = (id, info, json.dumps(schema), json.dumps({'latest': 'no info yet'}))
        cursor.execute(sql, data)
        conn.commit()


def getinfo(id):
    conn = sqlite3.connect("cameradatabase.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM cameras WHERE camera_id=?"
    cursor.execute(sql, [(id)])
    x = cursor.fetchone()
    if x == None:
        print('no such camera: ' + str(id) + ' (getinfo)')
        return None
    else:
        return [x[1], json.loads(x[2]), json.loads(x[3])]


def is_id_in_table(id):  # True - in table; False - not in table
    if getinfo(id) == None:
        return False
    else:
        print("also in table")
        return True


def update_latest(camera_id, latest):  # 2 - no user, 1 - user has this  dvor, 0 - updated
    conn = sqlite3.connect("cameradatabase.db")
    cursor = conn.cursor()
    if not is_id_in_table(camera_id):
        print('no such camera_id: ' + str(camera_id) + ' (update_latest)')
        return 2
    else:
        sql = 'UPDATE cameras SET latest = ? WHERE camera_id = ?'
        cursor.execute(sql, ((json.dumps(latest)), camera_id))
        conn.commit()
        return 0


def delete_camera(id):
    conn = sqlite3.connect("cameradatabase.db")
    cursor = conn.cursor()
    sql = "DELETE FROM cameras WHERE camera_id = ?"
    cursor.execute(sql, [(id)])
    conn.commit()
    print('camera ' + str(id) + " deleted")


create_table_cameras()
delete_camera(1)
create_new_camera(1, "ulica pushkina dom kolotushkina", {'lol': 'kek'})
print(getinfo(1))
update_latest(1, {'sasat': '+lezhat'})
print(getinfo(1))
