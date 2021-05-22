import asyncio
import pytest
# from tgintegration import BotController
from pyrogram import Client
from unittest.mock import create_autospec

api_id = "4478707"
api_hash = "ab986f838373378c37f0bb6bd0a6ac1e"
session_str = "1ApWapzMBu7x4E43vtsSlQzufDjuWAP-Qs5wPsjWv-1ZHq6lquRVljgAa793oLb_mFhQaBnqBMEEBEJ85BaxU5Z1A9nLf16fFh4bTliJ_yYI5s4HJNDJtsQIk2nfND9bT1H2iiNWqMafTxLRPkz8NQ5yk6dTih3ng6hRKvY2nimgpxrCk0yLFCn1N0awZGqKiPAM-QbOYp8rfOBGibKu9Uw7lyyC-OTDfKscyq05FdMEZotTfP_fOS4yxVzsEiNqLFsb0EJ_QSl15VEGfo9PSq7SytGpDqPUxG62YeTdqKu4QpcJSLJQfVx2_sgXGMFjcUpSQRPpTZPfC6A8bm8QvC93ay9RkV9M="

client = Client(
    session_name="@Vasily_Isaev",
    api_id=api_id,
    api_hash=api_hash
)


# controller = BotController(
#     peer="@taskFreeSolverbot",  # The bot under test is https://t.me/BotListBot 🤖
#     client=client,  # This assumes you already have a Pyrogram user client available
#     max_wait=60,  # Maximum timeout for responses (optional)
#     wait_consecutive=2,  # Minimum time to wait for more/consecutive messages (optional)
#     raise_no_response=True,  # Raise `InvalidResponseError` when no response is received (defaults to True)
#     global_action_delay=7  # Choosing a rather high delay so we can observe what's happening (optional)
# )

async def integration_start():
    await client.send_message("@taskFreeSolverbot", "/start")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text.split()[0] == "Greetings!"


async def integration_help():
    await client.send_message("@taskFreeSolverbot", "/help")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text.split()[0] == "Greetings!"


async def choose_mode_camera_input_incorrect1():
    await client.send_message("@taskFreeSolverbot", "camera ")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == "write user id and yard id in format: camera user_id yard_id"


async def choose_mode_camera_input_incorrect2():
    await client.send_message("@taskFreeSolverbot", "camera 1 1")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == "no such yard"


async def choose_mode_camera_input_incorrect3():
    await client.send_message("@taskFreeSolverbot", "camera vasy 5")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text is not None


async def choose_mode_camera_input_correct():
    await client.send_message("@taskFreeSolverbot", "camera vasy 1")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == 'some information about space near house vasy\nulica pushkina dom kolotushkina'


async def choose_mode_send_photo_input_incorrect1():
    await client.send_message("@taskFreeSolverbot", "send_photo 1 1 1 ")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == "write user id and yard id in format: send_photo user_id yard_id"


async def choose_mode_send_photo_input_incorrect2():
    await client.send_message("@taskFreeSolverbot", "send_photo no_known_user")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == 'no such camera id \n try another one'


async def choose_mode_send_photo_input_incorrect3():
    await client.send_message("@taskFreeSolverbot", "send_photo")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == "write user id and yard id in format: send_photo user_id yard_id"


async def choose_mode_send_photo_input_correct():
    await client.send_message("@taskFreeSolverbot", "send_photo vasy")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].photo is not None


async def add_camera_input_incorrect1():
    await client.send_message("@taskFreeSolverbot", "add_camera 1 1 1 1 1")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == "write user id and yard id in format: add_camera user_id camera_id"


async def add_camera_input_incorrect2():
    await client.send_message("@taskFreeSolverbot", "add_camera")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == "write user id and yard id in format: add_camera user_id camera_id"


async def add_camera_input_incorrect3():
    await client.send_message("@taskFreeSolverbot", "add_camera vasy 227")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == 'added'


async def add_camera_input_incorrect4():
    await client.send_message("@taskFreeSolverbot", "add_camera vasy 1")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == 'this camera id is already existed \n try another one or write No'


async def add_camera_input_correct():
    await client.send_message("@taskFreeSolverbot", "add_camera vasy 5")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == 'this camera id is already existed \n try another one or write No'


async def count_input_incorrect1():
    await client.send_message("@taskFreeSolverbot", "count 123 123 123")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == "write user id and yard id in format: add_camera user_id camera_id"


async def count_input_incorrect2():
    await client.send_message("@taskFreeSolverbot", "count")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == "write user id and yard id in format: add_camera user_id camera_id"


async def count_input_incorrect3():
    await client.send_message("@taskFreeSolverbot", "count UnknownUser")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == 'no such camera id \n try another one'


async def count_input_correct():
    await client.send_message("@taskFreeSolverbot", "count vasy")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text is not None


async def run_test_all():
    await client.start()
    to_test = [integration_start,
               integration_help,
               choose_mode_camera_input_incorrect1,
               choose_mode_camera_input_incorrect2,
               choose_mode_camera_input_incorrect3,
               choose_mode_camera_input_correct,
               choose_mode_send_photo_input_incorrect1,
               choose_mode_send_photo_input_incorrect2,
               choose_mode_send_photo_input_incorrect3,
               choose_mode_send_photo_input_correct,
               add_camera_input_incorrect1,
               add_camera_input_incorrect2,
               add_camera_input_incorrect3,
               add_camera_input_incorrect4,
               add_camera_input_correct,
               count_input_incorrect1,
               count_input_incorrect2,
               count_input_incorrect3,
               count_input_correct]
    right = 0
    wrong = 0
    for item in to_test:
        try:
            await item()
            right += 1
        except Exception as e:
            print(f"failed {item.__name__}")
            wrong += 1
    print(f"report: correct: {right} failed: {wrong}")


asyncio.run(run_test_all())
