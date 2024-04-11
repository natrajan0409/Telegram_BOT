from email import message
import logging.config
from aiogram import Bot,Dispatcher,executor,types
from dotenv import load_dotenv
import os 
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import requests



load_dotenv()
telegram_TOKEN = os.getenv('telegram_TOKEN')
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": "Bearer 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"}

# huggingface_key = os.getenv('huggingface_key')
# huggingface_API_URL = os.getenv('huggingface__API_URL')

# API_token =os.getenv('telegram_TOKEN')
# # bot_apikey_from_Huggingface = os.getenv('huggingface_key')
# API_URL=os.get('huggingface__API_URL')


modelname ="blenderbot-400M-distill"

## bot initialize 
bot =Bot(token=telegram_TOKEN)
dp=Dispatcher(bot)

# headers ={"Authorization":huggingface_key}
headers = {"Authorization": "Bearer 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"}

	


class Reference:
    def __init__(self):
        self.response = ""

reference = Reference()

def clear_past():
    reference.response=""
        


@dp.message_handler(commands=['start','hi'])
async def start_function(message: types.message):
    """
    This handler receives messages with `/start` command
    """
    await message.reply("I'm  bot power by  hugging face gpt")



@dp.message_handler(commands=['help'])
async def helper_function(message: types.Message):
    """
    This handler sends a help menu in response to the '/help' command
    """
    help_command = """
    This handler receives messages with `/start` command
    /help  to get help menu
    /clear clear old conversation 
    """
    await message.reply(help_command)


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    return response.json()

@dp.message_handler()
async def GPT_bot_main(message: types.Message):
    """
    A handler to process the user's input and generate a response using the Hugging Face API.
    """
    print(f">>> USER: \n\t{message.text}")

    try:
        response = query({
            "inputs": "Can you please let us know more details about your " + message.text,
        })

        if isinstance(response, list) and response:
            first_item = response[0]
            if isinstance(first_item, dict) and 'generated_text' in first_item:
                response_text = first_item['generated_text']
        else:
            response_text = "Sorry, I couldn't understand that."
    except (KeyError, IndexError):
        response_text = "Sorry, I couldn't understand that."

    print(f">>> chatGPT: \n\t{response_text}")

    await message.reply(response_text)
    
if __name__ == "__main__":
 executor.start_polling(dp,skip_updates=True)



