from app.models.messages.sms_messages.sms_messages import SmsMessages


class SmsMessagesController:

    @classmethod
    def send_sms_messages(cls, status_purchase: str):
        return SmsMessages.send_message(status_purchase)
