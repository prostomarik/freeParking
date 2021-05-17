import pytest


class FakeCallbackContext:
    pass


class FakeFromUser:
    id = 0


class FakeMesage:
    text = None
    reply_text_answer = None
    reply_photo_answer = None
    from_user = FakeFromUser

    def reply_text(self, text):
        self.reply_text_answer = text

    def reply_photo(self, photo):
        self.reply_photo_answer = photo


class FakeUpdater:
    def __init__(self):
        self.message = FakeMesage()


@pytest.fixture
def callback_context():
    return FakeCallbackContext()


@pytest.fixture
def updater():
    return FakeUpdater()