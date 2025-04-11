import telebot
from config import TOKEN, values
from extensions import APIException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_help(message: telebot.types.Message):
    text = ('Чтобы начать работу, введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> <количество переводимой валюты> (через пробел)\nУзнать доступные валюты: /values')
    bot.reply_to(message, text)

@bot.message_handler(commands=['values', ])
def send_values(message: telebot.types.Message):
    text = 'Все доступные валюты:'
    for key in values.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'location', 'contact','sticker'])
def other_messages(message: telebot.types.Message):
    bot.reply_to(message, 'Бот принимает только текстовые сообщения!')

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        data = message.text.lower().split(' ')

        if len(data) != 3:
            raise APIException('Неверное количество параметров')

        base, quote, amount = data
        total = CurrencyConverter.get_price(base, quote, amount)

    except APIException as e:
        bot.reply_to(message, f'Ошибка.\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать запрос.\n{e}')

    else:
        text = f'Цена {amount} {base} в {quote} - {total:.2f}'
        bot.send_message(message.chat.id, text)

bot.polling()