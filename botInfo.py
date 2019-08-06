import telebot
from flask import Flask, request
import os

TOKEN = '748088742:AAETJ2Hp4GCVoPU74hrsQFZ-BQ6ZqZ7GBb4'

bot = telebot.TeleBot(TOKEN)	
server = Flask(__name__)



@bot.message_handler(func=lambda message:True)
def echo_informatio_user_telegram(message):
	bot.send_message(chat_id = message.chat.id,
					text='Id:'+message.from_user.id+"\n First:"+message.from_user.first_name)
	bot.send_message(chat_id = message.chat.id,
					text='Id:'+message.chat.id+"\n First:"+message.chat.first_name)




@server.route('/'+TOKEN, methods=['POST'])
def get_message():
	json_update = request.stream.read().decode('utf-8')
	update = telebot.types.Update.de_json(json_update)

	bot.process_new_updates([update])
	return '', 200

if __name__ == '__main__':
	bot.remove_webhook()
	bot.set_webhook(url=os.getenv('WEBHOOK_URL')+TOKEN)

	server.run(host = "0.0.0.0", port = int(os.getenv('PORT', 8443)))
