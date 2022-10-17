#вариант Страна	Узор	Функция	Условие
#5       Литва	e	    y=|x|	Для возраста 12 лет и остальные
import csv
import os
import time
END = '\u001b[0m'
def rgb(r, g, b): return f"\u001b[48;2;{r};{g};{b}m"
Orange = rgb(255,165,0)
Green = rgb(0,100,0)
Red = rgb(139,0,0)
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
BLACK = "\u001b[40m"

#1
def country_flag():
    for i in range(3):
        print(Orange + ' ' * 35 + END)
    for i in range(3):
        print(Green + ' ' * 35 + END)
    for i in range(3):
        print(Red + ' ' * 35 + END)

country_flag()
print('||||')
#2
plot = [[0 for col in range(11)] for row in range(5)]

def draw_pattern(array):
    for i in range(5):
        for j in range(11):
            if i == 0 and j in [0, 1, 9, 10]:
                array[i][j] = 1
            if i == 1 and j in [2, 3, 7, 8]:
                array[i][j] = 1
            if i == 2 and j in [4, 6]:
                array[i][j] = 1
            if i in [3, 4] and j == 5:
                array[i][j] = 1
    return array


def draw_plot(array_pl, times):
    for i in range(5):
        line = ''
        for j in range(11):
            if j == 0:
                line += WHITE
            if array_pl[i][j] == 0:
                line += '  '
            if array_pl[i][j] == 1:
                line += BLACK + '  ' + WHITE
        line += END
        print(line * times)

def start():
    inp = input('Введите количество повторений узора: ')
    draw_plot(plot, int(inp))

draw_pattern(plot)
draw_plot(plot, 1)

start()
print('||||')

#3
def array_init():
    arr = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(10):
        for j in range(10):
            if i == j:
                arr[i][j] = 1
    for i in range(9, 0, -1):
        for j in range(9):
            if i + j == 8:
                arr[i][10+j] = 1
    arr[0][-1] = 1
    return arr

def draw_plot(arr):
    for i in range(10):
        line = ''
        for j in range(19):
            if j == 0:
                line += WHITE + str(9-i) + '\t'
            if arr[i][j] == 0:
                line += '   '
            if arr[i][j] == 1:
                line += Red + '   ' + WHITE
        line += END
        print(line)
    print(f'{WHITE}     -9 -8 -7 -6 -5 -4 -3 -2 -1 0 +1 +2 +3 +4 +5 +6 +7 +8 +9 {END}')


draw_plot(array_init())
print('|||||')

#4
with open('books.csv', 'r', encoding='cp1251') as f:

    table = csv.reader(f, delimiter=';')
    older_than_12 = 0
    younger_than_12 = 0
    for row in table:
        if row[5].isdigit():
            if int(row[5]) == 12:
                older_than_12 += 1
            else:
                younger_than_12 += 1

plot = [[0 for col in range(8)] for row in range(21)]

older_percent = round(older_than_12 / (older_than_12 + younger_than_12) * 100)
younger_percent = round(younger_than_12 / (older_than_12 + younger_than_12) * 100)

for i in range(21):
    plot[i][0] = f'{100-i*5}%'

for i in range(21):
    for j in range(8):
        if older_percent > 100-i*5:
            plot[i][2] = 1
            plot[i][3] = 1
        if younger_percent > 100-i*5:
            plot[i][5] = 2
            plot[i][6] = 2

for i in range(21):
    line = ''
    for j in range(8):
        if j == 0:
            line += f'{WHITE}{plot[i][0]}\t {END}'
        elif plot[i][j] == 0:
            line += f'{WHITE}   {END}'
        elif plot[i][j] == 1:
            line += f'{Red}   {END}'
        elif plot[i][j] == 2:
            line += f'{BLUE}   {END}'
    print(line)

print(f'\n{Red} Для 12 лет - {older_than_12} книг\t{END}\n{BLUE} Для остальных - {younger_than_12} книг\t{END}')
