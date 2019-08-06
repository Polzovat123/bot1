import telebot
from flask import Flask, request
import os
from telebot.types import InlineQueryResultArticle
from telebot.types import InputTextMessageContent



TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)	
server = Flask(__name__)

@bot.inline_handler(func = lambda query: 'help' in query.query)
def answer_alias(inline_query):
	username = inline_query.from_user.username
	myid = inline_query.from_user.id
	alias_article = InlineQueryResultArticle(
		id = '0',
		title = 'Send my nombEr',
		description = 'press to me FASST!!!!!',
		input_message_content = InputTextMessageContent(
			message_text = f'You`r ali: @{username}'
			)
		)
	bot.answer_inline_query(
		inline_query_id = inline_query.id,
		results = [alias_article],
		cache_time = 0
		switch_pm_text('Start')
		)



@bot.message_handler(func=lambda message:True)
def echo_informatio_user_telegram(message):
	bot.send_message(chat_id = message.chat.id,
					text='Id:'+str(message.from_user.id)+"\n First:"+str(message.from_user.first_name))
	bot.send_message(chat_id = message.chat.id,
					text='Id:'+str(message.chat.id)+"\n First:"+str(message.chat.first_name))




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