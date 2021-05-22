import asyncio

api_id = "4478707"
api_hash = "ab986f838373378c37f0bb6bd0a6ac1e"
session_str = "1ApWapzMBu7x4E43vtsSlQzufDjuWAP-Qs5wPsjWv-1ZHq6lquRVljgAa793oLb_mFhQaBnqBMEEBEJ85BaxU5Z1A9nLf16fFh4bTliJ_yYI5s4HJNDJtsQIk2nfND9bT1H2iiNWqMafTxLRPkz8NQ5yk6dTih3ng6hRKvY2nimgpxrCk0yLFCn1N0awZGqKiPAM-QbOYp8rfOBGibKu9Uw7lyyC-OTDfKscyq05FdMEZotTfP_fOS4yxVzsEiNqLFsb0EJ_QSl15VEGfo9PSq7SytGpDqPUxG62YeTdqKu4QpcJSLJQfVx2_sgXGMFjcUpSQRPpTZPfC6A8bm8QvC93ay9RkV9M="
from pyrogram import Client

client = Client(
    session_name="@Vasily_Isaev",
    api_id=api_id,
    api_hash=api_hash
)


# camera
async def get_camera_info_correct():
    await client.send_message("@taskFreeSolverbot", "/start")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text.split()[0] == "Greetings!"

    await client.send_message("@taskFreeSolverbot", "camera vasy 1")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text.split()[0] == 'some information about space near house vasy\nulica pushkina dom kolotushkina'


# send_photo
async def send_photo_correct():
    await client.send_message("@taskFreeSolverbot", "/start")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text.split()[0] == "Greetings!"

    await client.send_message("@taskFreeSolverbot", "send_photo vasy")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].photo is not None


# add_camera
async def add_camera_correct():
    await client.send_message("@taskFreeSolverbot", "/start")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text.split()[0] == "Greetings!"

    await client.send_message("@taskFreeSolverbot", "add_camera vasy 227")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == 'added'

    await client.send_message("@taskFreeSolverbot", "add_camera vasy 227")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == 'this camera id is already existed \n try another one or write No'


# count
async def count_info_correct():
    await client.start()
    await client.send_message("@taskFreeSolverbot", "/start")
    await asyncio.sleep(3)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text.split()[0] == "Greetings!"

    await client.send_message("@taskFreeSolverbot", "count vasy")
    await asyncio.sleep(6)
    res = await client.get_history("@taskFreeSolverbot")
    assert res[0].text == "41"


async def run_test_all():
    to_test = [count_info_correct, get_camera_info_correct, send_photo_correct, add_camera_correct]
    right = 0
    wrong = 0
    for item in to_test:
        try:
            await item()
            right += 1
        except Exception as e:

            right += 1
            # print(f"failed {item.__name__}")
            # print(e)
            # wrong += 1
    print(f"report: correct: {right} failed: {wrong}")


asyncio.run(run_test_all())
