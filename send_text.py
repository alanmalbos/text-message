# First, you need download twilio, install with pip
from twilio.rest import Client

# SID of your test account, find at twilio.com/console
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token, find at twilio.com/console
auth_token  = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Instance a Client from twilio
client = Client(account_sid, auth_token)

# Create a message and set a numbers to and from
# The from phone can be find in twilio.com/console
message = client.messages.create(
    to="+XXX", 
    from_="+XXX",
    body="E ai gata! Transadinha de leve hoje?")

# send the message
print(message.sid)