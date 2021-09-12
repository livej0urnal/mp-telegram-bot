import telebot
import requests
from telebot import types

bot = telebot.TeleBot('1863460136:AAEqo1krS1Po9BR7RyVquLMfHqrP--t8teI')


@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://myprojects.info/"))
    bot.send_message(message.chat.id, "Отличный выбор, просто нажми на кнопку", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['facebook'])
def open_facebook(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти в Facebook", url="https://www.facebook.com/myprojects.webstudio"))
    bot.send_message(message.chat.id, "Отличный выбор, просто нажми на кнопку", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['portfolio'])
def open_portfolio(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Портфолио", url="https://myprojects.info/ua/cases/"))
    bot.send_message(message.chat.id, "Привет. Чтобы увидеть наше портфолио. Просто нажми на кнопку", parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(commands=['reviews'])
def open_reviews(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Ознакомиться с отзывами о компании", url="https://myprojects.info/ua/reviews/"))
    bot.send_message(message.chat.id, "Посмотреть отзывы можно просто нажав кнопку", parse_mode='html',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "создание интернет магазинов":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Разработка на Yii')
        btn2 = types.KeyboardButton('Разработка на Wordpress')
        btn3 = types.KeyboardButton('Разработка на Opencart')
        btn4 = types.KeyboardButton('Разработка на Joomla')
        btn5 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "Для дальнейшего понимания. Необходимо выбрать детальнее: "

    elif get_message_bot == "начать заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Создание интернет магазинов')
        btn2 = types.KeyboardButton('SEO оптимизация сайтов')
        btn4 = types.KeyboardButton('Веб разработка(сайты, приложения)')
        btn3 = types.KeyboardButton('SMM продвижение')
        btn7 = types.KeyboardButton('Оптимизация сайтов')
        btn5 = types.KeyboardButton('SEO аудит')
        btn8 = types.KeyboardButton('Обратная связь')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn7, btn8)
        final_message = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nКакое направление " \
                        f"нашей деятельности Вас интересует?"

    elif get_message_bot == "seo аудит":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('цены на аудит')
        btn2 = types.KeyboardButton('Связь с seo/smm')
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3)
        final_message = "Чем мы сможем помочь в данном направлении сделайте выбор: "

    elif get_message_bot == "smm продвижение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('цены на smm')
        btn2 = types.KeyboardButton('Связь с seo/smm')
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3)
        final_message = "Чем мы сможем помочь в данном направлении сделайте выбор: "

    elif get_message_bot == "seo оптимизация сайтов":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('цены на seo')
        btn2 = types.KeyboardButton('Связь с seo/smm')
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3)
        final_message = "Чем мы сможем помочь в данном направлении сделайте выбор: "

    elif get_message_bot == "цены на seo":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn3)
        final_message = "Подробнее можно узнать по ссылке: <a href='https://myprojects.info/ua/service/seo-optiomization/'>SEO продвижение</a>"

    elif get_message_bot == "цены на smm":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn3)
        final_message = "Подробнее можно узнать по ссылке: <a href='https://myprojects.info/ua/service/smm-optimization/'>SMM продвижение</a>"

    elif get_message_bot == "цены на аудит":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn3)
        final_message = "Подробнее можно узнать по ссылке: <a href='https://myprojects.info/ua/service/seo-audit/'>SEO аудит сайта</a>"

    elif get_message_bot == "оптимизация сайтов":
        bot.send_message(message.chat.id, "Оптимизация сайтов под Google Pagespeed, gmetrix. Оптимизация показателей "
                                          "w3c validator.", parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('цены на оптимизация сайтов')
        btn2 = types.KeyboardButton('Связь с сотрудником по оптимизации сайтов')
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3)
        final_message = "Чем мы сможем помочь в данном направлении сделайте выбор: "

    elif get_message_bot == "веб разработка(сайты, приложения)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('цены на web разработку')
        btn2 = types.KeyboardButton('Связь с сотрудником по разработке')
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3)
        final_message = "Чем мы сможем помочь в данном направлении сделайте выбор: "

    elif get_message_bot == "цены на web разработку":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn3)
        final_message = "Средняя цена на web разработку сайтов = 6000 грн. Подробнее можно узнать по ссылке: <a href='https://myprojects.info/ua/service/web-development/'>Web разработка</a>"

    elif get_message_bot == "разработка на opencart":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('цены на разработку сайтов')
        btn2 = types.KeyboardButton('Связь с сотрудником по разработке')
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3)
        final_message = "Чем мы сможем помочь в данном направлении сделайте выбор: "

    elif get_message_bot == "разработка на joomla":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('цены на разработку сайтов')
        btn2 = types.KeyboardButton('Связь с сотрудником по разработке')
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3)
        final_message = "Чем мы сможем помочь в данном направлении сделайте выбор: "

    elif get_message_bot == "разработка на wordpress":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('цены на разработку сайтов')
        btn2 = types.KeyboardButton('Связь с сотрудником по разработке')
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3)
        final_message = "Чем мы сможем помочь в данном направлении сделайте выбор: "

    elif get_message_bot == "цены на разработку сайтов":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn3)
        final_message = "Средняя цена на разработку на интернет магазинов на CMS = 7000 грн. Подробнее можно узнать по ссылке: <a href='https://myprojects.info/ua/service/ecommerce-development/'>Разработка интернет магазинов</a>"

    elif get_message_bot == "цены на оптимизация сайтов":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn3)
        final_message = "Средняя цена на оптимизацию интернет ресурсов = 2500 грн. Обратите внимание есть гарантия на результат. Подробнее можно узнать по ссылке: <a href='https://myprojects.info/ua/service/site-optimization/'>Оптимизация сайтов</a>"

    elif get_message_bot == "разработка на yii":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Цена на разработку yii')
        btn2 = types.KeyboardButton('Связь с сотрудником по разработке')
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn1, btn2, btn3)
        final_message = "Чем мы сможем помочь в данном направлении сделайте выбор: "

    elif get_message_bot == "цена на разработку yii":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn3)
        final_message = "Средняя цена на разработку с помощью Yii2+ framework = 15400 грн. Подробнее можно узнать по ссылке: <a href='https://myprojects.info/ua/service/ecommerce-development/'>Разработка на Yii2+</a>"

    elif get_message_bot == "связь с сотрудником по разработке":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn3)
        final_message = "Спасибо за Ваш выбор. Вы сможете получить консультацию на сайте в <a href='https://myprojects.info/ua/free-consultation/'>контактной форме</a>. И конечно же здесь в телеграмм вот <a href='https://t.me/seniourdevelop'>профиль</a>"

    elif get_message_bot == "связь с сотрудником по оптимизации сайтов":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn3)
        final_message = "Спасибо за Ваш выбор. Вы сможете получить консультацию на сайте в <a href='https://myprojects.info/ua/free-consultation/'>контактной форме</a>. И конечно же здесь в телеграмм вот <a href='https://t.me/seniourdevelop'>профиль</a>"

    elif get_message_bot == "связь с seo/smm":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn3)
        final_message = "Спасибо за Ваш выбор. Вы сможете получить консультацию на сайте в <a href='https://myprojects.info/ua/free-consultation/'>контактной форме</a>. И конечно же здесь в телеграмм вот <a href='https://t.me/VladaFlo'>профиль</a>"

    elif get_message_bot == "обратная связь":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn3 = types.KeyboardButton('Начать заново')
        markup.add(btn3)
        final_message = "Введите ваш номер телефона: "

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Начать заново')
        markup.add(btn1)
        phonenumber = f"Пришла новая форма обратной связи. Номер телефона : {str(message.text)}"
        chating = '-508116869'
        requests.get(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={-508116869}&parse_mode=html&text={phonenumber}")
        final_message = "Спасибо за Ваш выбор. Вы сможете получить консультацию на сайте в <a href='https://myprojects.info/ua/free-consultation/'>контактной форме</a>. "
        bot.send_message(chating, phonenumber, parse_mode='html')

    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Создание интернет магазинов')
    btn2 = types.KeyboardButton('SEO оптимизация сайтов')
    btn4 = types.KeyboardButton('Веб разработка(сайты, приложения)')
    btn3 = types.KeyboardButton('SMM продвижение')
    btn7 = types.KeyboardButton('Оптимизация сайтов')
    btn5 = types.KeyboardButton('SEO аудит')
    btn8 = types.KeyboardButton('Обратная связь')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn7, btn8)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nКакое направление " \
                f"нашей деятельности Вас интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)




bot.polling(none_stop=True)
