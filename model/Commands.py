from model.Note import Note
import csv
import model.Save_Read as SR



def add_note():
    #Создаем заметку
    print ("Тема: ")
    topic = input()
    print("Текст заметки: ")
    text = input()
    new_note = Note(topic,text)

    # считываем csv базу в архив
    notes_db = SR.read_file()

    # сплитуем заметку для добавления в массив
    array = [new_note.id, new_note.topic, new_note.text, new_note.date]
    notes_db.append(array)
    SR.write_file(notes_db)
    print("Заметка сохранена")


def show_notes():
    notes_array = SR.read_file()
    length = len(notes_array)
    for b in range(length):
        print(notes_array[b])
#Изменение. Выбор между поиском и дальнейшим изменение по id или по теме
def note_edit():
    print("Режим изменения заметок")
    print("1 - Поиск по id \n2 - Поиск по теме\n")
    choice= int(input())
    if choice == 1:
        print('ok')
        id_edit()
    if choice == 2:
        print('ok')
        topic_edit()
    else:
        print("Ошибка. Комманда не обнаружена")

def id_edit():
    print('Введите id необходимой заметки: ')
    id = input('id: ')
    # считываем csv базу в архив
    notes_db = SR.read_file()
    numrows = len(notes_db)
    numcols = len(notes_db[0])
    for i in range(1, (numrows)):
        if notes_db[i][0] == id:
            notes_db[i][1] = input('Введите тему: ')
            notes_db[i][2] = input('Введите текст: ')
        else:
            print("Такого id нет")
    SR.write_file(notes_db)
    print("Заметка сохранена")


def topic_edit():
    print('Введите Тему заметки, которую хотите изменить: ')
    topic = input('Тема: ')
    # считываем csv базу в архив
    notes_db = SR.read_file()
    numrows = len(notes_db)
    numcols = len(notes_db[0])
    for i in range(1, (numrows)):
        if notes_db[i][1] == topic:
            notes_db[i][1] = input('Введите тему: ')
            notes_db[i][2] = input('Введите текст: ')
        else:
            print("Такой заметки нет")
    SR.write_file(notes_db)
    print("Заметка сохранена")


#Поиск. Выбор между поисом по id или по теме
def search():
    print("Режим поиска")
    print("1 - Поиск по id \n2 - Поиск по теме\n")
    choice = int(input())
    if choice == 1:
        print('ok')
        id_search()
    if choice == 2:
        print('ok')
        topic_search()
    else:
        print("Ошибка. Комманда не обнаружена")

def id_search():
    print('Введите id заметки для поиска: ')
    id = input('id: ')
    # считываем csv базу в архив
    notes_db = SR.read_file()
    numrows = len(notes_db)
    numcols = len(notes_db[0])
    for i in range(1, (numrows)):
        if notes_db[i][0] == id:
            print(notes_db[i][0],notes_db[i][1],notes_db[i][2],notes_db[i][3])
        else:
            print("Такого id нет")

def topic_search():
    print('Введите тему заметки для поиска: ')
    topic = input('тема: ')
    # считываем csv базу в архив
    notes_db = SR.read_file()
    numrows = len(notes_db)
    numcols = len(notes_db[0])
    for i in range(1, (numrows)):
        if notes_db[i][1] == topic:
            print(notes_db[i][0], notes_db[i][1], notes_db[i][2], notes_db[i][3])
        else:
            print("Такой заметки нет")

#Удаление. Выбор между моментальным удалением по id или же первоначальным выводом всех заметок
def delete_note():
    print("Режим удаления")
    print('1 - Показать список всех заметок, 2 - Удаление по id')
    choice = int(input())
    if choice == 1:
        show_notes()
        id_delete()
    if choice == 2:
        id_delete()
    else:
        print("Ошибка. Комманда не обнаружена")

def id_delete():
    print('Введите id заметки, которую хотите удалить: ')
    id = input('id: ')
    # считываем csv базу в архив
    notes_db = SR.read_file()
    numrows = len(notes_db)
    numcols = len(notes_db[0])
    for i in range(1, (numrows)):
        if notes_db[i][0] == id:
            b = 0
            while b < 4:
                del(notes_db[i][0])
                b += 1
        else:
            print("Такой заметки нет")
    SR.write_file(notes_db)
    print("Заметка удалена")




