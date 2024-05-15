import requests


class Students:

    def get_students(self, course_id):
        #dayımın servisinden course_id ye tanımlı bütün
        #öğrencileri çekeceğim.
        students_list = requests.get('url', data={'course_id': course_id})
        if students_list.status_code == 200:
            return students_list
        return [
            {"mustafa": "+46733955229"},
            {"ilker": "+905537145870"},
            {"mehmet": "+905303177928"},
        ]