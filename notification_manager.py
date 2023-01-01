from twilio.rest import Client

TWILIO_SID = "ACb7cc1fcd9a3ae4510b35a2bd8c7f1601"
TWILIO_AUTH_TOKEN = "dc763d2ff9ddf18f950d6e18faa9dcac"
TWILIO_VIRTUAL_NUMBER = "+13393310995"
TWILIO_VERIFIED_NUMBER = "+254722366973"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
