from app.models.messages.email_messages.email_messages import EmailMessages
from app.models.messages.sms_messages.sms_messages import SmsMessages
from app.models.messages.whatsapp_messages.whatsapp_messages import WhatsappMessages


class FactoryMessages:

    @classmethod
    def get_message(cls, type_message: str, status_purchase: str):
        if type_message == 'email':
            return EmailMessages.send_message(status_purchase)
        elif type_message == 'whatsapp':
            return WhatsappMessages.send_message(status_purchase)
        else:
            return SmsMessages.send_message(status_purchase)

