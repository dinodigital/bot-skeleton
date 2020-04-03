from telegram.ext import CallbackContext

from models import User


def broadcast_job(ctx: CallbackContext):
    for u in User.select():
        ctx.bot.send_message(u.tg_id, 'Sample broadcast')
