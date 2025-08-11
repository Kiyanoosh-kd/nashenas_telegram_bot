from types import SimpleNamespace
from telebot import types
from src.utils.keyboard import create_keyboard
import emoji

keys = SimpleNamespace(
    random_connect=types.KeyboardButton(f'{emoji.emojize(":globe_with_meridians:Random Connect")}'),
    settings=types.KeyboardButton(f'{emoji.emojize(":gear:Settings")}')
)


keyboards = SimpleNamespace(
    main = create_keyboard(keys.random_connect, keys.settings)
)

