import view.UI



def run():
    view.UI.start()
    print('1 - Вывести список команд\n2-Завершение')
    choice = int(input())
    if choice == 1:
        run()
    else:
        return "Завершение"

