from datetime import datetime
import uuid
import itertools


class Note(object):
    #итерируемый id
    id = itertools.count()

    def __init__(self, topic, text, date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = next(self.id)
        self.topic = topic
        self.text = text
        self.date = date

    def get_id(note):
        return note.id

    def get_topic(note):
        return note.title

    def set_topic(note):
        print('Введите тему заметки');
        note.topic =input()
        return note

    def get_text(note):
        return note.body

    def set_text(note):
        print('Введите текст заметки');
        note.text = input()
        return note

    def get_date(note):
         return note.date

    def to_string(self):
        info = "id - " + str(self.id) + "\nТема - " + self.topic + "\n" + self.text + "\nДата создания - " + self.date
        a = 10
        return info

    def NotePrint (self):
        print(self.to_string())


