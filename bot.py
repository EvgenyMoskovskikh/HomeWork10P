import telebot
import random
from config10 import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,
                                               row_width=2)
    item1 = telebot.types.KeyboardButton('Отгадай число')
    item2 = telebot.types.KeyboardButton('Гороскоп')

    markup.add(item1, item2)

    bot.send_sticker(message.chat.id,
                     'CAACAgIAAxkBAAEG9VRjpOrcD_PEsHThOGBP_Qmq2aBh3QACBwIAAtzyqwdVSve97Ve_kSwE')
    bot.send_message(message.chat.id,
                     f'{message.from_user.first_name}, Здравствуй, выбери что хочешь?)',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Отгадай число':
        mess = bot.send_message(message.chat.id,
                                'Отгадай число, которое я загадал (от 1 до 3)')
        bot.register_next_step_handler(mess, random_num)
    elif message.text == 'Гороскоп':
        botbot(message)
    else:
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAEG9PpjpNO_Kv1Aonp-47TJ8U-6vAWxWQACDwMAApzW5wpf0t9odCKbAywE')
        bot.send_message(message.chat.id,
                         f'{message.from_user.first_name}, что нибудь попроще, пожалуйста)')


def random_num(message):
    rnd = random.randint(1, 4)
    if message.text == str(rnd):
        bot.send_message(message.chat.id, 'Вау! ты угадал)))')
    else:
        bot.send_message(message.chat.id, f'Не-а!) я загадал {rnd}')


def botbot(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=3)

    item1 = telebot.types.InlineKeyboardButton('Овен', callback_data='Aries')
    item2 = telebot.types.InlineKeyboardButton('Телец', callback_data='Taurus')
    item3 = telebot.types.InlineKeyboardButton('Близнецы',
                                               callback_data='Twins')
    item4 = telebot.types.InlineKeyboardButton('Рак', callback_data='Cancer')
    item5 = telebot.types.InlineKeyboardButton('Лев', callback_data='Leo')
    item6 = telebot.types.InlineKeyboardButton('Дева', callback_data='Virgin')
    item7 = telebot.types.InlineKeyboardButton('Весы', callback_data='Scales')
    item8 = telebot.types.InlineKeyboardButton('Скорпион',
                                               callback_data='Scorpio')
    item9 = telebot.types.InlineKeyboardButton('Стрелец',
                                               callback_data='Sagittarius')
    item10 = telebot.types.InlineKeyboardButton('Козерог',
                                                callback_data='Capricorn')
    item11 = telebot.types.InlineKeyboardButton('Водолей',
                                                callback_data='Aquarius')
    item12 = telebot.types.InlineKeyboardButton('Рыбы', callback_data='Pisces')

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9,
               item10, item11, item12)

    bot.send_message(message.chat.id, 'Выбери знак:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    znak = zodiac_sign()
    try:
        if call.message:
            if call.data == 'Aries':
                bot.send_message(call.message.chat.id, znak['Овен'])
            elif call.data == 'Taurus':
                bot.send_message(call.message.chat.id, znak['Телец'])
            elif call.data == 'Twins':
                bot.send_message(call.message.chat.id, znak['Близнецы'])
            elif call.data == 'Cancer':
                bot.send_message(call.message.chat.id, znak['Рак'])
            elif call.data == 'Leo':
                bot.send_message(call.message.chat.id, znak['Лев'])
            elif call.data == 'Virgin':
                bot.send_message(call.message.chat.id, znak['Дева'])
            elif call.data == 'Scales':
                bot.send_message(call.message.chat.id, znak['Весы'])
            elif call.data == 'Scorpio':
                bot.send_message(call.message.chat.id, znak['Скорпион'])
            elif call.data == 'Sagittarius':
                bot.send_message(call.message.chat.id, znak['Стрелец'])
            elif call.data == 'Capricorn':
                bot.send_message(call.message.chat.id, znak['Козерог'])
            elif call.data == 'Aquarius':
                bot.send_message(call.message.chat.id, znak['Водолей'])
            elif call.data == 'Pisces':
                bot.send_message(call.message.chat.id, znak['Рыбы'])

            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Выбери знак:', reply_markup=None)
    except Exception as e:
        print(repr(e))


def zodiac_sign():
    znak = {}
    with open('botbot.txt', 'r', encoding='utf-8') as f:
        for i in range(12):
            str = f.readline().split(' ', 1)
            znak[str[0]] = str[1]
    return znak


bot.polling(none_stop=True)
