from email import message
import logging.config
from aiogram import Bot,Dispatcher,executor,types
from dotenv import load_dotenv
import os 
# import resource
import logging


load_dotenv()
API_token =os.getenv('telegram_TOKEN')
bot_apikey_from_Huggingface=os.get('huggingface_key')
API_URL=os.get('huggingface__API_URL')


#configure logging
logging.basicConfig(level=logging.INFO)


## bot initialize 
bot =Bot(token=API_token)
dp=Dispatcher(bot)


@dp.message_handler(commands=['start', 'help', 'hi'])
async def command_start_handler(message: types.message):
    """
    This handler receives messages with `/start` command
    """
    await message.reply("I'm  bot power by  hugging face gpt")
    
    
@dp.message_handler()
async def echo(message:types.message):
    """_summary_

    Args:
        message (types.message): _description_
    """
    await message.reply(message.text)
    

if __name__ == "__main__":
 executor.start_polling(dp,skip_updates=True)
