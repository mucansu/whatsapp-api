import datetime
import requests
from twilio.rest import Client
import json
from lesson import Lesson
from students import Students
from notification_service import NotificationService

if __name__ == "__main__":
  with open('config.json') as json_file:
    config = json.load(json_file)
  account_sid = config['TWILIO_ACCOUNT_SID']
  auth_token = config['TWILIO_AUTH_TOKEN']
  client = Client(account_sid, auth_token)
  lesson = Lesson(datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(hours=1), "https://zoom.us/j/1234567890?pwd=QWERTY", 1)
  Students = Students()
  students_list = Students.get_students()
  notification_service = NotificationService(client)
  notification_service.create_notification(students_list)

          