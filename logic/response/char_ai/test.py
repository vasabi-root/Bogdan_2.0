from characterai import aiocai, authGuest
import asyncio
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv('config\.env')

token = os.getenv("CAI_TOKEN")
# print(token)

async def main():
    char = 'ql8RTLD8EmJNH4cDJr2n91RohXLo5_Aw0GMMCaZQeNg'

    client = aiocai.Client(token)

    me = await client.get_me()

    voices = await client.get_voices()

    for voice in voices:
        pprint(voice)

    # async with await client.connect() as chat:
    #     new, answer = await chat.new_chat(
    #         char, me.id
    #     )

    #     print(f'{answer.name}: {answer.text}')
        
    #     while True:
    #         text = input('YOU: ')

    #         message = await chat.send_message(
    #             char, new.chat_id, text
    #         )

    #         print(f'{message.name}: {message.text}')

asyncio.run(main())