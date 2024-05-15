from twilio.rest import Client
import datetime
#from lesson import get_zoom_link

class NotificationService:
    def __init__(self, account_sid, auth_token):
        self.client = Client(account_sid, auth_token)

    def create_notification(self, students_list):
            notification_time=datetime.timedelta(hours=1)
    #    if datetime.datetime.now() + notification_time > lesson.start_time:                
            #message = "{lesson} dersiniz başlamak üzere. Canlı ders linki: {link}".format(lesson=lesson, link=lesson.link)
            message = "Bu bir test mesajıdır. https://www.mintyazilim.com/"
            for student in students_list:
                self.client.messages.create(
                    body=message,
                    from_="whatsapp:+14155238886",
                    to="whatsapp:+905303177928"
                )
    def set_notification_time(self,hours,minutes):
        return datetime.timedelta(hours=hours,minutes=minutes)
