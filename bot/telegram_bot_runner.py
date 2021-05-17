from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from bot.hack_bot import start_command, where_is_camera, choose_mode, help_command

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("992803506:AAFFDf2TXt8SQuVO9UvEUznRxHrdc-7Idjw")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("where_is_camera", where_is_camera))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, choose_mode))
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
