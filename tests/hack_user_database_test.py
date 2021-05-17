import pytest

from bot.hack_user_database import create_table_users, getinfo, create_new_user, is_user_in_table, \
    create_new_dvor_for_user, delete_users_dvor, delete_user
from tests.hack_dvor_database_test import checkTableExists


def test_create_table_users():
    create_table_users()
    assert checkTableExists("users", "/home/vasily/PycharmProjects/freeParking/bot/userdatabase.db")


def test_is_user_in_table():
    test_user = "test_user"
    create_new_user(test_user)
    assert is_user_in_table(test_user)


def test_create_new_user():
    test_user = "test_user"
    create_new_user(test_user)
    assert getinfo(test_user) == []


def test_create_new_dvor_for_user():
    test_user = "test_user"
    dvor_id = 0
    delete_users_dvor(test_user, dvor_id)
    assert create_new_dvor_for_user(test_user, dvor_id) == 0


def test_create_new_dvor_for_user_exist():
    test_user = "test_user"
    dvor_id = 0
    assert create_new_dvor_for_user(test_user, dvor_id) == 1


def test_create_new_dvor_for_user_no_exist():
    test_user = "test_user123"
    dvor_id = 0
    assert create_new_dvor_for_user(test_user, dvor_id) == 2


def test_delete_users_dvor_deleted():
    test_user = "test_user"
    dvor_id = 0
    delete_users_dvor(test_user, dvor_id)
    assert delete_users_dvor(test_user, dvor_id) == 1


def test_delete_users_dvor():
    test_user = "test_user"
    dvor_id = 0
    assert delete_users_dvor(test_user, dvor_id) == 1


def test_delete_users_dvor_not_exist_user():
    test_user = "test_user"
    dvor_id = 0
    delete_users_dvor(test_user, dvor_id)
    assert delete_users_dvor("aaa", dvor_id) == 2


def test_delete_user_with_dvor():
    test_user = "test_user"
    create_new_user(test_user)
    delete_user(test_user)
    assert not is_user_in_table(test_user)
