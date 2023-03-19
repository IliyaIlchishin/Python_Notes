import model.Commands as commands
import time


def start():
    delay()
    print("Выберите действие: \n1.Добавить заметку\n2.Изменить\n3.Посмотреть все заметки\n4.Поиск  \n5.Удалить")
    mode = input()

    match mode:
        case "1":
            delay()
            commands.add_note()
        case "2":
            print("-" * 50)
            commands.note_edit()
        case "3":
            delay()
            commands.show_notes()
        case "4":
            delay()
            commands.search()
        case "5":
            delay()
            commands.delete_note()
        case _:
            return "Неизвестная команда"



def delay():
    time.sleep(0.5)
    print("-" * 50)
    time.sleep(0.5)