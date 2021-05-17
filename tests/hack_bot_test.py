from bot.hack_bot import start_command, where_is_camera, choose_mode


def test_start_command_creation(updater, callback_context):
    try:
        start_command(updater, callback_context)
    except TypeError as t:
        assert 0


def test_start_command_creation_response(updater, callback_context):
    start_command(updater, callback_context)
    assert updater.message.reply_text_answer == 'Greetings! I can show you free space for parking.\n' + 'To get this information use /getinfo.\n' + 'To get help press /help.'


def test_where_is_camera_creation_error(updater, callback_context):
    try:
        where_is_camera(updater, callback_context)
        assert 0
    except TypeError as t:
        assert True


def test_where_is_camera_creation(updater, callback_context):
    updater.message.text = "99"
    where_is_camera(updater, callback_context)
    assert updater.message.reply_text_answer is None


def test_where_is_camera_response(updater, callback_context):
    updater.message.text = "1"
    where_is_camera(updater, callback_context)
    assert updater.message.reply_text_answer == 'some information about space near house 1\nulica pushkina dom kolotushkina'


def test_where_is_camera_no_camera(updater, callback_context):
    updater.message.text = "1"
    updater.message.from_user.id = 10
    where_is_camera(updater, callback_context)
    assert updater.message.reply_text_answer == "no such camera id \n try another one"


def test_choose_mode_wrong_camera_data(updater, callback_context):
    updater.message.text = "camera 1"
    choose_mode(updater, callback_context)
    assert updater.message.reply_text_answer == "write user id and yard id in format: camera user_id yard_id"


def test_choose_mode_correct_camera_data(updater, callback_context):
    updater.message.text = "camera vasy 1"
    choose_mode(updater, callback_context)
    assert updater.message.reply_text_answer == 'some information about space near house vasy\nulica pushkina dom kolotushkina'


def test_choose_mode_wrong_send_photo_data(updater, callback_context):
    updater.message.text = "send_photo 1 1"
    choose_mode(updater, callback_context)
    assert updater.message.reply_text_answer == 'write user id and yard id in format: send_photo user_id yard_id'


def test_choose_mode_correct_send_photo_data_text(updater, callback_context):
    updater.message.text = "send_photo vasy"
    choose_mode(updater, callback_context)
    assert updater.message.reply_text_answer == None


def test_choose_mode_correct_send_photo_data_media(updater, callback_context):
    updater.message.text = "send_photo vasy"
    choose_mode(updater, callback_context)
    assert updater.message.reply_photo_answer is not None
