import cv2.cv2 as cv2
import pytest

from bot.utils import showImage, update, load_exchange


@pytest.fixture
def example_response():
    return str({"status":"ok"})


@pytest.fixture
def example_link():
    return "https://reputate-backend.ru/"


# def test_show_image():
#     assert showImage([], []).size == cv2.imread('/home/vasily/PycharmProjects/freeParking/bot/bot.jpg').size


def test_update(example_response, example_link):
    assert update(example_link) == example_response


def test_load_exchange(example_response, example_link):
    assert load_exchange(example_link) == example_response
