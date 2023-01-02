from telegram import Update
from datetime import datetime
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup


def get_news_sv():
    list_news = []
    r = requests.get("https://sv.ut.edu.vn/sinh-vien/dm-tin-tuc/thong-bao-chung.html")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs = soup.find_all("div", {"class": "desc-txt"})

    for new in mydivs:
        newdict = {}
        newdict["link"] = new.a.text
        list_news.append(newdict)

    return list_news


def get_news1():
    list_news1 = []
    r = requests.get("https://vnexpress.net/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs1 = soup.find_all("h3", {"class": "title-news"})

    for new in mydivs1:
        newdict1 = {}
        newdict1["link"] = new.a.get("href")
        newdict1["title"] = new.a.get("title")
        list_news1.append(newdict1)

    return list_news1


def get_news2():
    list_news2 = []
    r = requests.get("https://thanhnien.vn/")
    soup = BeautifulSoup(r.text, 'html.parser')
    mydivs2 = soup.find_all("h2")

    for new in mydivs2:
        newdict2 = {}
        newdict2["link"] = new.a.get("href")
        newdict2["title"] = new.a.get("title")
        list_news2.append(newdict2)

    return list_news2


def news(update: Update, context: CallbackContext) -> None:
    data = get_news_sv()

    for item in data:
        update.message.reply_text(f'{item["link"]}')


def news1(update: Update, context: CallbackContext) -> None:
    data1 = get_news1()

    for item in data1:
        update.message.reply_text(f'{item["link"]}')


def news2(update: Update, context: CallbackContext) -> None:
    data2 = get_news2()

    for item in data2:
        update.message.reply_text(f'{item["link"]}')


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'xin chào {update.effective_user.first_name} {update.effective_user.last_name}, tôi có thể giúp gì cho bạn?')


def myid(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'ID của bạn là: {update.effective_user.id}')


def date(update: Update, context: CallbackContext) -> None:
        now = "Hôm nay là: " + datetime.now().strftime("%d-%m-%y, %H:%M:%S")
        update.message.reply_text(now)


def get_user_text(update: Update, context: CallbackContext) -> None:
    tus = "Trần Minh Tú_2051120175_CN20B" + "\n" + "contact:https://www.facebook.com/profile.php?id=100011632725758"
    trung = "Hồ Ngọc Trung_2051120194_CN20B" + "\n" + "contact:https://www.facebook.com/trung.hongoc.3304"
    thanh = "Nguyễn Huỳnh Gia Thạnh_2051120181_CN20B" + "\n" + "contact:https://www.facebook.com/profile.php?id=100010621290250"
    phu = "Hồ Đình Phú_2051120153_CN20B" + "\n" + "contact:https://www.facebook.com/profile.php?id=100039516442236"

    update.message.reply_text(tus)
    update.message.reply_text(trung)
    update.message.reply_text(thanh)
    update.message.reply_text(phu)


updater = Updater('5905259707:AAFgAqQ4wr1YczY0ZiI-QKA9zSpMBBIzMII')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('notif_sv', news))
updater.dispatcher.add_handler(CommandHandler('news1', news1))
updater.dispatcher.add_handler(CommandHandler('news2', news2))
updater.dispatcher.add_handler(CommandHandler('date', date))
updater.dispatcher.add_handler(CommandHandler('info', get_user_text))
updater.dispatcher.add_handler(CommandHandler('id', myid))
updater.start_polling()
updater.idle()

