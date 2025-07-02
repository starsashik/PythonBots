def add_student(x):
    students[x[0]] = [int(x[1]), float(x[2]), float(x[3]), float(x[4])]


def show_student(x):
    print(x, *students[x])


def del_student(x):
    del students[x]


def show_info(x):
    if x == 0:
        dat = sorted(students.items(), key=lambda y: y[0])
    else:
        dat = sorted(students.items(), key=lambda y: y[1][x - 1])
    for i in dat:
        print(i[0], *i[1])


def save_file(x):
    with open(x, mode='w', encoding='utf8') as f:
        for i in students:
            f.write(f'{i} {students[i][0]} {students[i][1]} {students[i][2]} {students[i][3]}\n')


def load_file(x):
    global students
    with open(x,mode='r',encoding='utf8') as f:
        students = {}
        for i in f:
            dat = i.split()
            students[dat[0]] = [int(dat[1]), float(dat[2]), float(dat[3]), float(dat[4])]


"""Пример

ДОБАВИТЬ ПетровСА 2005 2.71 3.14 4 
ДОБАВИТЬ ИвановПС 2006 4.5 3.9 5 
ДОБАВИТЬ ОшибкаВВ 2004 2 3 4 
СВОДКА 0 
УДАЛИТЬ ОшибкаВВ 
ПОКАЗАТЬ ПетровСА 
СОХРАНИТЬ db.txt 
УДАЛИТЬ ПетровСА 
СВОДКА 1 
ЗАГРУЗИТЬ db.txt 
СВОДКА 2
"""

students = {}
print("""
1. ДОБАВИТЬ 
2. ПОКАЗАТЬ 
3. УДАЛИТЬ 
4. СВОДКА
5. СОХРАНИТЬ 
6. ЗАГРУЗИТЬ 
""")
while True:
    s = input("Введите команду:")
    data = s.split()
    if data[0] == "ДОБАВИТЬ":
        add_student(data[1:])
    elif data[0] == "ПОКАЗАТЬ":
        show_student(data[1])
    elif data[0] == "УДАЛИТЬ":
        del_student(data[1])
    elif data[0] == 'СВОДКА':
        show_info(int(data[1]))
    elif data[0] == 'СОХРАНИТЬ':
        save_file(data[1])
    elif data[0] == 'ЗАГРУЗИТЬ':
        load_file(data[1])
    else:
        break
