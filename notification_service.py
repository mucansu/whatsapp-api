from twilio.rest import Client
import datetime
from students import Students
#from lesson import get_zoom_link

class NotificationService:
    def __init__(self, client):
        self.client = client

    def create_notification(self, students_list):
            notification_time=datetime.timedelta(hours=1)
    #    if datetime.datetime.now() + notification_time > lesson.start_time:                
            #message = "{lesson} dersiniz başlamak üzere. Canlı ders linki: {link}".format(lesson=lesson, link=lesson.link)
            message = "Bu bir test mesajıdır. https://www.mintyazilim.com/"
            student_instance = Students()
            students_list = student_instance.get_students()
            for name, phone_number in students_list.items():
                self.client.messages.create(
                    body=message,
                    from_="whatsapp:+14155238886",
                    to=phone_number
                )
    def set_notification_time(self,hours,minutes):
        return datetime.timedelta(hours=hours,minutes=minutes)
