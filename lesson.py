import datetime
import requests

class Lesson:
    def __init__(self, start_time, end_time,link,lesson_id):
        self.start_time = start_time
        self.end_time = end_time
        self.lesson_id = lesson_id
        self.link = self.get_zoom_link()

    def get_zoom_link(self):
        url = f'https://www.mintyazilim.com/get_zoom_link?lesson_id={self.lesson_id}'
        response = requests.get(url)
        if response.status_code == 200:
            link = response.json()['link']
            return link
        else:         
            print(f"Failed to fetch the Zoom link for lesson ID {self.lesson_id}. Status code: {response.status_code}")
            return None