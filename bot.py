from telegram import Bot
from telegram.ext import messagequeue as mq

from config import TG_TOKEN


class MQBot(Bot):
    def __init__(self, *args, is_queued_def=True, mqueue=None, **kwargs):
        super(MQBot, self).__init__(*args, **kwargs)
        self._is_messages_queued_default = is_queued_def
        self._msg_queue = mqueue or mq.MessageQueue()

    def __del__(self):
        try:
            self._msg_queue.stop()
        except Exception as e:
            pass

    @mq.queuedmessage
    def send_message(self, *args, **kwargs):
        return super(MQBot, self).send_message(*args, **kwargs)

    @mq.queuedmessage
    def send_photo(self, *args, **kwargs):
        return super(MQBot, self).send_photo(*args, **kwargs)


bot = MQBot(TG_TOKEN)
