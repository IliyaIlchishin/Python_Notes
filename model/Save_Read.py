from model.Note import Note
import csv



def write_file(array):
    # поля
    fields = ['id', 'Тема', 'Текст', 'Дата создания']
    rows = array
    with open('Notes.csv', 'w') as f:
        file = csv.writer(f)
        #file.writerow(fields)
        file.writerows(rows)

def read_file():
    array = []
    f = open('Notes.csv', 'r')
    lines = f.read().split("\n")  # "\r\n" if needed
    for line in lines:
        if line != "":
            temp = line.split(",")
            array.append(temp)
    return array
