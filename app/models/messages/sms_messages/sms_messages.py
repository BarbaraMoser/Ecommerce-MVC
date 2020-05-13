from app.models.messages.abstract_messages import AbstractMessages


class SmsMessages(AbstractMessages):

    def __init__(self):
        super().__init__()

    @classmethod
    def send_message(cls, status_purchase: str):
        return f'SMS - Your purchase was {status_purchase}'
