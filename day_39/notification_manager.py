from twilio.rest import Client
SID = "AC483fc1a82272eaa0d724b46755dd617c"
TOKEN = "e9fb0ee7b2e72a0efaae914e505b6384"
VIRTUAL_NUMBER = "+16076526399"
MY_NUMBER = ""

class NotificationManager:
  #This class is responsible for sending notifications with the deal flight details.
  def __init__(self):
    self.clent = Client(SID, TOKEN)

  def send_sms(self, message):
    message = self.clent.messages.create(
      body=message,
      from_=VIRTUAL_NUMBER,
      to=MY_NUMBER
    )
    print(message.sid)