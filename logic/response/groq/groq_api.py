import asyncio
from dotenv import load_dotenv
import os
import json
from pprint import pprint
from groq import Groq

if __name__ != '__main__':
    from logic.response.core import AiApiWrapper
else:
    load_dotenv('config/.env')
    class AiApiWrapper: pass


class GroqApi(AiApiWrapper):
    def __init__(self, model="llama3-70b-8192", meaner_count=1, chat_to_str=None):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key)

        self.model = model # llama3-8b-8192

        self.summary_prompt = open('logic/response/groq/prompts/sammary_prompt.txt', "r").read()
        self.shorten_prompt = open('logic/response/groq/prompts/shorten_prompt.txt', "r").read()
        self.joke_prompt = open('logic/response/groq/prompts/joke_prompt.txt', "r").read()

        if chat_to_str is None:
            self.chat_to_str = lambda chat: '\n'.join([f"{m['name']}: {m['text']}" for m in chat])
        else: 
            self.chat_to_str = chat_to_str

        self.meaner_count = meaner_count

    
    def process_chat(self, chat):
        print("getting sammary")
        sammary = self.get_sammary_from_chat(chat)[-1]['content']

        print("getting shorten sammary")
        shorten = self.get_shorten_from_sammary(sammary)[-1]['content']

        print("getting joke")
        joke = self.get_joke_from_chat(chat, sammary=shorten)

        print("getting meaner joke")
        meaner = self.get_meaner_joke(joke)[-1]['content']

        return meaner

    def request(self, history, max_tokens=200, temperature=1.2):
        response = self.client.chat.completions.create(model=self.model,
                                        messages=history,
                                        max_tokens=max_tokens,
                                        temperature=temperature)
        history.append({'role': 'assistant', 'content' : response.choices[0].message.content})
        return history
    def get_sammary_from_chat(self, chat):
        chat_history = [{'role': 'system', 'content': self.summary_prompt}]

        chat_history.append({'role': 'user', 'content': self.chat_to_str(chat)})

        return self.request(chat_history)

    def get_shorten_from_sammary(self, sammary):
        chat_history = [{'role': 'system', 'content': self.shorten_prompt}]

        chat_history.append({'role': 'user', 'content': sammary})

        return self.request(chat_history)

    def get_joke_from_chat(self, chat, sammary = None, references = None):
        chat_history = [{'role': 'system', 'content': self.joke_prompt}]

        msg_for_mock = self.chat_to_str(chat) + sammary if sammary else '' + f'\n\n\Make a punch for {chat[-1]["name"]}'

        chat_history.append({'role': 'user', 'content': msg_for_mock})

        return self.request(chat_history)

    def get_meaner_joke(self, history):
        for i in range(self.meaner_count):
            history.append({'role': 'user', 'content' : 'rephrase it in a more toxic and hurtful way'})
            history = self.request(history)
            
        return history


if __name__ == '__main__':
    load_dotenv()
    groq = GroqApi(meaner_count=5)

    tg_chat = json.load(open('result.json', encoding='utf-8'))
    messages = tg_chat['messages']
    msgs = [{'name': m['from'], 'text': m['text']} for m in messages if m['type'] == 'message' and isinstance(m['text'], str)]

    print(groq.process_chat(msgs[-15:]))
