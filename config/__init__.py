from enum import Enum
from dotenv import load_dotenv

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

DEFAULT_CHANCE = 10
CHANCE = 'chance'
CONTEXT = 'context'
CACHE = {}
DEFAULT_CACHE = { 
    CHANCE: DEFAULT_CHANCE,
    CONTEXT: [],
}

START_TEXT = f'''
Здарова, кожаные мешки.
Я буллинг-бот Богдан.
Можно настроить вероятность моих высеров в процентах командой /chance50. 
По умолчанию я буллю с шансом {DEFAULT_CHANCE}%.'''
             
CANCEL_TEXT = 'Цирк уехал.'

GET_CHANCE_TEXT = 'Шанс моего высера равен '
SET_CHANCE_TEXT = 'Теперь шанс моего высера равен '

UNKNOWN_TEXT = 'Доигрался. Удаляю каталог `/etc`.'

load_dotenv()