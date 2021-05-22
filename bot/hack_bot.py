from cv2 import cv2

from bot import hack_user_database
from bot import hack_dvor_database

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from simple_car_detectiong.detector import detect_img

hack_dvor_database.create_table_cameras()
hack_dvor_database.create_new_camera(1, "ulica pushkina dom kolotushkina", {'lol': 'kek'})
hack_user_database.create_table_users()


def start_command(update: Update, _: CallbackContext):
    hack_user_database.create_table_users()
    hack_user_database.create_new_user(update.message.from_user.id)
    print("--" + str(hack_user_database.getinfo(update.message.from_user.id)))
    for i in range(3):
        update.message.reply_text(
            'Greetings! I can show you free space for parking.\n' +
            'To get this information use /getinfo.\n' +
            'To get help press /help.'
        )


def help_command(update: Update, _: CallbackContext):
    update.message.reply_text(
        'Greetings! I can show you free space for parking.\n' +
        'To get this information use /getinfo.\n' +
        'To get help press /help.'

    )


def where_is_camera(update: Update, _: CallbackContext):
    x = update.message.text
    if len(x) == 1 and is_number(x):
        if hack_user_database.getinfo(update.message.from_user.id) is not None:
            update.message.reply_text('some information about space near house ' + str(x) + '\n' + str(
                hack_dvor_database.getinfo(x)[0]))
        else:
            update.message.reply_text('no such camera id \n try another one')


def choose_mode(update: Update, _: CallbackContext) -> None:
    text = update.message.text
    if "camera" == text.split()[0]:
        if len(text.split()) == 3:
            send_camera_info(update, text.split()[1], text.split()[2])
        else:
            update.message.reply_text("write user id and yard id in format: camera user_id yard_id")

    elif "send_photo" == text.split()[0]:
        if len(text.split()) == 2:
            send_photo_and_update(update, text.split()[1])
        else:
            update.message.reply_text("write user id and yard id in format: send_photo user_id yard_id")
    elif "add_camera" == text.split()[0]:
        if len(text.split()) == 3:
            add_camera(update, text.split()[1], text.split()[2])
        else:
            update.message.reply_text("write user id and yard id in format: add_camera user_id camera_id")
    elif "count" == text.split()[0]:
        if len(text.split()) == 2:
            count_spaces(update, text.split()[1])
        else:
            update.message.reply_text("write user id and yard id in format: add_camera user_id camera_id")

    else:
        update.message.reply_text("write user id and yard id in format: camera/send_photo")


def count_spaces(update: Update, user_id):
    count = handle_count_output(detect_img("picture5.jpg"))
    if hack_user_database.getinfo(user_id) is not None:
        hack_dvor_database.update_latest(user_id, count)
        update.message.reply_text(str(count))
    else:
        update.message.reply_text('no such camera id \n try another one')


def handle_count_output(detector_out):
    count = 0
    for eachItem in detector_out:
        if eachItem["name"] == "car":
            count += 1
    return count


def add_camera(update: Update, user_id, camera_id):
    if not hack_dvor_database.is_id_in_table(camera_id):
        reply_add_camera(user_id, camera_id)
        update.message.reply_text('added')
    else:
        update.message.reply_text('this camera id is already existed \n try another one or write No')


def send_camera_info(update: Update, user_id, yard_id):
    try:
        if hack_user_database.getinfo(user_id) is not None:
            reply_yard_info(update, user_id, yard_id)
        else:
            update.message.reply_text("no such yard")
    except Exception as e:
        raise e


def send_photo_and_update(update: Update, user_id):
    try:
        if hack_user_database.getinfo(user_id) is not None:
            reply_photo(update)
        else:
            update.message.reply_text('no such camera id \n try another one')
    except Exception as e:
        raise e


def reply_add_camera(user_id, camera_id):
    hack_user_database.create_new_dvor_for_user(user_id, camera_id)


def reply_yard_info(update: Update, user_id, yard_id):
    try:
        update.message.reply_text('some information about space near house ' + str(user_id) + '\n' + str(
            hack_dvor_database.getinfo(int(yard_id))[0]))
    except Exception as e:
        raise e


def reply_photo(update: Update):
    photo = open("/home/runner/work/freeParking/freeParkingsimple_car_detectiong/output/newimage.jpg", 'rb')
    update.message.reply_photo(photo)


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
