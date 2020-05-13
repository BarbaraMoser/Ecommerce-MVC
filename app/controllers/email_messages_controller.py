from app.models.messages.email_messages.email_messages import EmailMessages


class EmailMessagesController:

    @classmethod
    def send_email_messages(cls, status_purchase: str):
        return EmailMessages.send_message(status_purchase)
