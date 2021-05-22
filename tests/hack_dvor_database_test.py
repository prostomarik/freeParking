import sqlite3

from bot.hack_dvor_database import create_new_camera, getinfo, is_id_in_table, update_latest, \
    delete_camera, create_table_cameras


def checkTableExists(tablename, url):
    conn = sqlite3.connect(url)
    try:
        conn.execute(f"SELECT * FROM {tablename}")
    except Exception as E:
        conn.close()
        return False
    return True


def test_create_table_cameras():
    create_table_cameras()
    assert checkTableExists("cameras", "/home/runner/work/freeParking/freeParking/bot/cameradatabase.db")


def test_create_new_camera():
    camera_id = 0
    info = "test_info"
    schema = "test_schema"
    create_new_camera(camera_id, info, schema)
    assert getinfo(camera_id) == ['test_info', 'test_schema', {'latest': 'no info yet'}]


def test_is_id_in_table():
    camera_id = 0
    info = "test_info"
    schema = "test_schema"
    create_new_camera(camera_id, info, schema)
    assert is_id_in_table(0)


def test_update_latest():
    camera_id = 0
    info = "test_info"
    schema = "test_schema"
    create_new_camera(camera_id, info, schema)
    latest = "latest info"
    update_latest(camera_id, latest)
    assert getinfo(camera_id) == ['test_info', 'test_schema', 'latest info']


def test_delete_camera():
    camera_id = 0
    info = "test_info"
    schema = "test_schema"
    create_new_camera(camera_id, info, schema)
    delete_camera(0)
    assert not is_id_in_table(0)
