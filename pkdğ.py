from telegram.ext import Updater, CommandHandler
from telegram import Bot

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Merhaba!")

def main():
    # Telegram botunuzun tokenını buraya girin
    token = 'YOUR_BOT_TOKEN'
    bot = Bot(token=token)
    updater = Updater(bot=bot, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()
