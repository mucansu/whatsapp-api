import requests


class Students:
    def __init__(self,students_list):
        self.students_list = self.get_students()
    def get_students(self):
        #dayımın servisinden course_id ye tanımlı bütün
        #öğrencileri çekeceğim.
        #students_list = requests.get('url', data={'course_id': course_id})
        #if students_list.status_code == 200:
        #    return students_list
        return [
            {"mustafa": "whatsapp:+46733955229"},
            {"ilker": "whatsapp:+905537145870"},
            {"mehmet": "whatsapp:+905303177928"},
        ]