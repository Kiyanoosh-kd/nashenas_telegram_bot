from loguru import logger

from src.utils.io import write_json
from src.utils.constanc import keyboards
from src.utils.filters import IsAdmin
import emoji
from src.bot import bot


class Bot:
    """ Template for telegram bot.
    """    
    def __init__(self, telebot):
        self.bot = telebot

        # add custom filters
        self.bot.add_custom_filter(IsAdmin())

        # register handelers
        self.handlers()
        self.markup = keyboards.main
        self.bot.infinity_polling()
        

    def handlers(self):
        """This is as handeler method
        """ 
        @self.bot.message_handler(is_admin=True)
        def admin_of_group(message):
            self.send_message(message.chat.id, '<strong>Hi Kianoush</strong>') 

        @self.bot.message_handler(func=lambda m: True)
        def echo_all(message):
            """This method send reply and message in the response to the sent message

            Args:
                message (dict): the message that hes been sent to bot
            """        
            self.send_message(message.chat.id, 'Hello',reply_markup=self.markup)



    def send_message(self, chat_id, text, reply_markup=None, emojize = True):
        """Method for sending message to users

        Args:
            chat_id (_type_): _description_
            text (str): _description_
            reply_markup (_type_, optional): _description_. Defaults to None.
        """   
        if emoji :
            text = emoji.emojize(text)     
        self.bot.send_message(chat_id, text, reply_markup = reply_markup)
    
if __name__ == '__main__':
    logger.info('The Bot has just started...')
    nashenas_bot = Bot(telebot = bot)
    
