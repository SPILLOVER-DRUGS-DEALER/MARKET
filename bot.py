# coding=utf-8
import telebot
# import sqlite3 as sql
from telebot import types

TOKEN = '775824922:AAFYr6dQmidXHxrOG36Aklypew65NIIkF-Y'

bot = telebot.TeleBot(TOKEN)


def inline():
    inlinekey1 = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='Назад 🔙', callback_data='Nazad')
    but_2 = types.InlineKeyboardButton(text='Хиты ⭐️', callback_data='Xit')
    but_3 = types.InlineKeyboardButton(text='Добавить ➕', callback_data='dobav')
    inlinekey1.add(but_1, but_2, but_3)
    return inlinekey1

def inline2():
    inlinekey2 = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='1️⃣🔘️', callback_data='1krug')
    but_2 = types.InlineKeyboardButton(text='2️⃣⚪️', callback_data='2krug')
    but_3 = types.InlineKeyboardButton(text='3️⃣⚪️', callback_data='3krug')
    but_4 = types.InlineKeyboardButton(text='Добавить ➕', callback_data='DobavitPlus')
    but_5 = types.InlineKeyboardButton(text='Корзина 📦', callback_data='korzina')
    but_6 = types.InlineKeyboardButton(text='Оформить ✅', callback_data='oformit')
    inlinekey2.add(but_1, but_2, but_3)
    inlinekey2.add(but_4)
    inlinekey2.add(but_5, but_6)
    return inlinekey2

def inline3():
    inlinekey2 = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='1️⃣⚪️', callback_data='1krug')
    but_2 = types.InlineKeyboardButton(text='2️⃣🔘️', callback_data='2krug')
    but_3 = types.InlineKeyboardButton(text='3️⃣⚪️', callback_data='3krug')
    but_4 = types.InlineKeyboardButton(text='Добавить ➕', callback_data='DobavitPlus')
    but_5 = types.InlineKeyboardButton(text='Корзина 📦', callback_data='korzina')
    but_6 = types.InlineKeyboardButton(text='Оформить ✅', callback_data='oformit')
    inlinekey2.add(but_1, but_2, but_3)
    inlinekey2.add(but_4)
    inlinekey2.add(but_5, but_6)
    return inlinekey2

def inline4():
    inlinekey2 = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text='1️⃣⚪️', callback_data='1krug')
    but_2 = types.InlineKeyboardButton(text='3️⃣⚪️', callback_data='2krug')
    but_3 = types.InlineKeyboardButton(text='3️⃣🔘️', callback_data='3krug')
    but_4 = types.InlineKeyboardButton(text='Добавить ➕', callback_data='DobavitPlus')
    but_5 = types.InlineKeyboardButton(text='Корзина 📦', callback_data='korzina')
    but_6 = types.InlineKeyboardButton(text='Оформить ✅', callback_data='oformit')
    inlinekey2.add(but_1, but_2, but_3)
    inlinekey2.add(but_4)
    inlinekey2.add(but_5, but_6)
    return inlinekey2

@bot.message_handler(commands = ['start'])
def startpg(message):
        startmenu = types.ReplyKeyboardMarkup(True, False)
        startmenu.row('Мороженое 🍨', 'Прочие десерты 🍮')
        startmenu.row('Безлактозное мороженое 🍥', 'Хиты продаж ⭐️')
        startmenu.row('Корзина 📦', 'Мои заказы 📋')
        bot.send_message(message.chat.id, 'Вы в главном меню 🎯\n\nДля просмотра графика работы,'
                                      ' условий доставки и оплаты нажмите /info', reply_markup=startmenu)

@bot.message_handler(commands=['info'])
def startpg1(message):
    bot.send_message(message.chat.id, '📍 Адрес точки самовывоза:\nНаш цех: г. Долгопрудный ул. Якова Гунина 1\n\n'
                                          '📋 Минимальный заказ – 1500 рублей, доставка в пределах \n'
                                          'МКАД бесплатно. После заказа с вами свяжется менеджер для \n'
                                          'уточнения времени доставки.\n\n💠 Вы можете дополнительно заказать сухой лёд для \n'
                                          '"автономного" хранения (500 руб.)\n\n\n👨 Оператор: @daddycool84\n'
                                          '☎️ Контактный телефон: +79266532299')


@bot.message_handler(content_types=['text'])
def morojenoe(message):
    if message.text == 'Мороженое 🍨':
        global moroj
        moroj = 'moroj'
        replykey1 = types.ReplyKeyboardMarkup(True, False)
        replykey1.row('Назад 🔙')
        replykey1.row('Мятное с шоколадом - 100р.')
        replykey1.row('Мятное с брауни - 400р.')
        replykey1.row('Вишня-миндаль  - 400р.')
        bot.send_message(message.chat.id, 'Выберите товар', reply_markup=replykey1)
        bot.send_message(message.chat.id, """\r
        <a href="http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg">🛎</a> <b>Мятное с шоколадом</b>
        \n⚖️ Объем: 130мл\n💵 Цена: 100р.\n📋 Описание: Для этого мороженого мы настаиваем молоко на\nсвежей мяте. В сезон используем местную мяту, а зимой, когда \nнаша мята теряет свой аромат — переходим на импортную. В\nмороженое добавляем мелко дробленный бельгийский \nшоколад для контраста и удовольствия.
        """, parse_mode="HTML", reply_markup=inline())
    elif message.text == 'Прочие десерты 🍮':
        if moroj != 'moroj':
            replykey1 = types.ReplyKeyboardMarkup(True, False)
            replykey1.row('Назад 🔙')
            replykey1.row('Панна-котта апельсин-манго-маракуйя - 150р.')
            replykey1.row('Кешью в какао - 200р.')
            bot.send_message(message.chat.id, 'Выберите товар', reply_markup=replykey1)
            bot.send_message(message.chat.id, """\r
        🛎​ <b>Панна-котта апельсин-манго-маракуйя </b>
        \n⚖️ Вес: 160г\n💵 Цена: 150р.""", parse_mode="HTML", reply_markup=inline())
    elif message.text == 'Назад 🔙':
        moroj = 'exit'
        startpg(message)
    elif message.text == 'Мятное с шоколадом - 100р.':
        if moroj == 'moroj':
            bot.send_message(message.chat.id, """\r
            <a href="http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg">🛎</a> <b>Мятное с шоколадом</b>
            \n⚖️ Объем: 130мл\n💵 Цена: 100р.\n📋 Описание: Для этого мороженого мы настаиваем молоко на\nсвежей мяте. В сезон используем местную мяту, а зимой, когда \nнаша мята теряет свой аромат — переходим на импортную. В\nмороженое добавляем мелко дробленный бельгийский \nшоколад для контраста и удовольствия.
            """, parse_mode="Markdown", reply_markup=inline())
    elif message.text == 'Мятное с брауни - 400р.':
        if moroj == 'moroj':
            bot.send_message(message.chat.id, """\r
            <a href="http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg">🛎</a> <b>Мятное с брауни</b>
            \n⚖️ Объем: 500мл\n💵 Цена: 400р.\n📋 Описание: Мороженое приготовлено на основе\nнатурального коровьего молока и сливок. В рецепте\nиспользуют свежую мяту, для каждой новой партии на\nпроизводстве пекут шоколадные пирожные брауни
            """, parse_mode="HTML", reply_markup=inline())
    elif message.text == 'Вишня-миндаль  - 400р.':
        if moroj == 'moroj':
            bot.send_message(message.chat.id, """\r
            <a href="http://res.cloudinary.com/muzicius/image/upload/v1493211955/foodservice-icecake/xbtwx6waomzxurcje6zf.jpg">🛎</a> <b>Вишня-миндаль</b>
            \n⚖️ Объем: 500мл\n💵 Цена: 400р.\n📋 Описание:  Мороженое с миндально-вишневым вкусом,\nприготовленное на основе натурального коровьего молока и \nсливок. Для производства этого мороженого сырой миндаль\nнарезают и обжаривают вручную. Засахаривают свежую или \nзамороженную вишню, в зависимости от сезона.
            """, parse_mode="HTML", reply_markup=inline())
    elif message.text == 'Панна-котта апельсин-манго-маракуйя - 150р.':
        bot.send_message(message.chat.id, """\r
        🛎​ <b>Панна-котта апельсин-манго-маракуйя </b>
        \n⚖️ Вес: 160г\n💵 Цена: 150р.""", parse_mode="HTML", reply_markup=inline())
    elif message.text == 'Панна-котта апельсин-манго-маракуйя - 150р.':
        bot.send_message(message.chat.id, """\r
        🛎​ <b>Кешью в какао - 200р.</b>
        \n⚖️ Вес: 75г\n💵 Цена: 200р.""", parse_mode="HTML", reply_markup=inline())
    elif message.text == 'Хиты продаж ⭐️':
        bot.send_message(message.chat.id, """\r
        🛎​ <b>Панна-котта апельсин-манго-маракуйя </b>
        \n⚖️ Вес: 160г\n💵 Цена: 150р.""", parse_mode="HTML", reply_markup=inline2())


@bot.callback_query_handler(func=lambda c: True)
def inlin(c):
    if c.data == 'Nazad':
        global moroj
        moroj = 'exit'
        startmenu = types.ReplyKeyboardMarkup(True, False)
        startmenu.row('Мороженое 🍨', 'Прочие десерты 🍮')
        startmenu.row('Безлактозное мороженое 🍥', 'Хиты продаж ⭐️')
        startmenu.row('Корзина 📦', 'Мои заказы 📋')
        bot.send_message(c.message.chat.id,'Вы в главном меню 🎯\n\nДля просмотра графика работы, условий доставки и оплаты нажмите /info', reply_markup=startmenu)
    elif c.data == '1krug':
        bot.edit_message_text("""\r
        🛎​ <b>Панна-котта апельсин-манго-маракуйя </b>
        \n⚖️ Вес: 160г\n💵 Цена: 150р.""", parse_mode="HTML", chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=inline2())
    elif c.data == '2krug':
        bot.edit_message_text("""\r
        <a href="http://res.cloudinary.com/muzicius/image/upload/v1493211922/foodservice-icecake/n1adsq6uewmttsht1vax.jpg">🛎</a> <b>Соленая карамель </b> 
        \n📏 Объем: 130мл / 500мл\n💵 Цена: 100р. / 400р.\n📋 Описание: Для каждой новой партии мороженого на \nпроизводстве вручную готовят карамельный соус по рецептам \nфранцузских кондитеров. В этом рецепте соль добавляется в \nготовую смесь, в самом конце перед замораживанием.""", parse_mode="HTML", chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=inline3())
    elif c.data == '3krug':
        bot.edit_message_text("""\r
        <a href="http://res.cloudinary.com/muzicius/image/upload/v1493211964/foodservice-icecake/h4l5buzcle7v0qtsnux8.jpg">🛎</a> <b>Бельгийский шоколад </b> 
        \n📏 Объем: 130мл / 500мл\n💵 Цена: 100р. / 400р.\n📋 Описание: Фактически, это "двойной шоколад", потому что в \nрецепте используется и какао-порошок, и темный шоколад \nпремиального бельгийского бренда Barry Callebaut. Благодаря \nэтому  мороженое имеет глубокий, насыщенный и по-\nнастоящему шоколадный вкус. Именно поэтому мы не стали\nдобавлять в этот рецепт никаких других наполнителей. """,
        parse_mode="HTML", chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=inline4())


bot.polling()