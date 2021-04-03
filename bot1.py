import telebot

bot = telebot.TeleBot("", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['send_nudes'])
def echo_all(message):
	chatId = message.chat.id
	photo = open("nudes.jpg", 'rb')
	bot.send_photo(chatId, photo)

bot.polling()
