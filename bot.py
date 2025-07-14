from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "SEU_TOKEN_AQUI"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Olá! Eu sou seu bot no Telegram!")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
