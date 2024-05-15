import datetime
import requests
from twilio.rest import Client
import json

with open('config.json') as json_file:
    config = json.load(json_file)
account_sid = config['TWILIO_ACCOUNT_SID']
auth_token = config['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='There is the link : https://us04web.zoom.us/j/73569223136?pwd=tZTulrcYgU5opVgYEDYiwLaOoFhbUd.1',
  to='whatsapp:+46733955229'
)


       	