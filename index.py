import time
import datetime
from threading import Thread
import telebot
from telebot import types
from database import add_user, get_users, update_advice, update_news
from utils import get_advice, get_news, get_catalog_text

bot = telebot.TeleBot('5185239971:AAHiQNA37X6TlqgeDmVNPrFKzZWxHvrBe68')
schedule = ([10, 13, 16, 19], [11, 14, 18], [12, 17], [15])
offset = datetime.timezone(datetime.timedelta(hours = 3))

def send_news():
    while True:
        news = get_news()
        users = get_users()
        if update_news(news[0]):
            for id in users:
                markup = types.InlineKeyboardMarkup()
                url_btn = types.InlineKeyboardButton(text = 'Подробнее', url = news[1])
                markup.add(url_btn)
                try:
                    bot.send_message(id, news[0], reply_markup = markup)
                except Exception as e:
                    print(e)
        time.sleep(600)

def send_catalog():
    while True:
        users = get_users()
        time_now = datetime.datetime.now(offset).hour
        if time_now in schedule[0]:
            for id in []:
                try:
                    bot.send_message(id, get_catalog_text(0), parse_mode = 'Markdown')
                except Exception as e:
                    print(e)
                time.sleep(60)
                try:
                    bot.send_message(id, get_catalog_text(1), parse_mode = 'Markdown')
                except Exception as e:
                    print(e)
        if time_now in schedule[1]:
            for id in users:
                try:
                    bot.send_message(id, get_catalog_text(2), parse_mode = 'Markdown')
                except Exception as e:
                    print(e)
        if time_now in schedule[2]:
            for id in users:
                try:
                    bot.send_message(id, get_catalog_text(3), parse_mode = 'Markdown')
                except Exception as e:
                    print(e)
        if time_now in schedule[3]:
            for id in users:
                try:
                    bot.send_message(id, get_catalog_text(4), parse_mode = 'Markdown')
                except Exception as e:
                    print(e)
        time.sleep(3600)

def send_advice():
    while True:
        advice = get_advice()
        users = get_users()
        if update_advice(advice[0]):
            for id in users:
                markup = types.InlineKeyboardMarkup()
                url_btn = types.InlineKeyboardButton(text = 'Читать далее', url = advice[2])
                markup.add(url_btn)
                try:
                    bot.send_message(id, "*" + advice[0] + "*\n\n" + advice[1], reply_markup = markup, parse_mode = 'Markdown')
                except Exception as e:
                    print(e)
        time.sleep(21600)

@bot.message_handler(commands=['start'])
def start(message):
    id = message.chat.id
    users = get_users()
    if id not in users:
        add_user(id)
        news = get_news()
        markup = types.InlineKeyboardMarkup()
        url_btn = types.InlineKeyboardButton(text = 'Подробнее', url = news[1])
        markup.add(url_btn)
        try:
            bot.send_message(id, news[0], reply_markup = markup)
        except Exception as e:
            print(e)

@bot.message_handler(commands=['growth_stocks'])
def gs(message):
    id = message.chat.id
    try:
        bot.send_message(id, get_catalog_text(0), parse_mode = 'Markdown')
    except Exception as e:
        print(e)

@bot.message_handler(commands=['falling_stocks'])
def fs(message):
    id = message.chat.id
    try:
        bot.send_message(id, get_catalog_text(1), parse_mode = 'Markdown')
    except Exception as e:
        print(e)

@bot.message_handler(commands=['exchange_rates'])
def er(message):
    id = message.chat.id
    try:
        bot.send_message(id, get_catalog_text(2), parse_mode = 'Markdown')
    except Exception as e:
        print(e)

@bot.message_handler(commands=['valuable_goods'])
def vg(message):
    id = message.chat.id
    try:
        bot.send_message(id, get_catalog_text(3), parse_mode = 'Markdown')
    except Exception as e:
        print(e)

@bot.message_handler(commands=['market_indexes'])
def mi(message):
    id = message.chat.id
    try:
        bot.send_message(id, get_catalog_text(4), parse_mode = 'Markdown')
    except Exception as e:
        print(e)


Thread(target = send_news).start()
Thread(target = send_catalog).start()
Thread(target = send_advice).start()
bot.polling(none_stop = True, interval = 0)