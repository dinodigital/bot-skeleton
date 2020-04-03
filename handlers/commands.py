from telegram import Update
from telegram.ext import CallbackContext

from models import User


def start(update: Update, ctx: CallbackContext):
    u, is_created = User.get_or_create(
        tg_id=update.message.from_user.id,
        defaults={
            'username': update.message.from_user.username
        })

    msg = 'Hi, new user.' if is_created else 'Hi, old user.'
    ctx.bot.send_message(u.tg_id, msg)