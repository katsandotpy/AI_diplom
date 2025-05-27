import telebot
from googletrans import Translator
import asyncio
import json
from transformers import AutoModelForCausalLM, AutoTokenizer




model = AutoModelForCausalLM.from_pretrained("/model")
tokenizer = AutoTokenizer.from_pretrained("/model")


with open("config.json", "r", encodinf="utf-8") as file:
    config = json.load(file)


API_KEY = config.get("API_KEY")

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler()
def z(message):
    input_text = asyncio.run(RU_EN(message.text))
    inputs = tokenizer(input_text, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs)
    answer = asyncio.run(EN_RU(tokenizer.decode(outputs[0], skip_special_tokens=True)))
    bot.send_message(message.chat.id, answer)


translator = Translator()
async def EN_RU(message):
    async with Translator() as translator:
        r = await translator.translate(message, src='en', dest='ru')
        return r.text

async def RU_EN(message):
    async with Translator() as translator:
        r = await translator.translate(message, src='ru', dest='en')
        return r.text


bot.polling(none_stop=True)