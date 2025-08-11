from telebot import types

def create_keyboard(*args,row_width=2, resize_keyboard=True):
    """This function create a keyboard from recived keys for telegram bot

    Args:
        row_width (int, optional): _description_. Defaults to 2.
        resize_keyboard (bool, optional): _description_. Defaults to True.

    Returns:
        keyboard: a keyboard that could be used for telegram bot
    """    
    keyboard = types.ReplyKeyboardMarkup(row_width=row_width,
                                          resize_keyboard=resize_keyboard)
    keyboard.add(*args)
    return keyboard