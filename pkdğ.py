from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Merhaba!")

def main():
    # Telegram botunuzun tokenını buraya girin
    token = '6181887397:AAE1MKVuEiX8ce_QLBiT4N37iQO7h5Gqgrg'
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()
