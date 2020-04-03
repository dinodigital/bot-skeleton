from telegram.ext import Updater, CommandHandler

from bot import bot
from handlers.commands import start
from jobs.sample import broadcast_job


def bot_run():
    # TODO::CREATE setup logging

    updater = Updater(bot=bot, workers=4, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))

    updater.job_queue.run_repeating(broadcast_job, interval=60, first=0)

    updater.start_polling(clean=True)
    updater.idle()


if __name__ == '__main__':
    bot_run()