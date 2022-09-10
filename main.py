import os
import sys
import keyboard
import time
import datetime

# root linux test
try:
    if keyboard.is_pressed("W"):
        pass
except ImportError:
    print("Для запуска на Linux нужны root-права.")
    quit()

# variables
input_delay = 0.1
now_time = datetime.datetime.now().timestamp()
old_time = datetime.datetime.now().timestamp()
alert_delay = 1
now_time_alert = datetime.datetime.now().timestamp()
old_time_alert = datetime.datetime.now().timestamp()
name = ""
hero = "0"
cell_list = {
    "grass": "#",
    "pond": " ",
    "trap": "t"
}
X = 0
Y = 0
old_x = X
old_y = Y
map = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", " ", " ", "#", "#", "#"],
       ["#", "#", "#", "#", "#", " ", " ", " ", " ", "#"],
       ["#", "#", "#", "#", "#", " ", " ", " ", " ", "#"],
       ["#", "#", "#", "#", "#", "#", " ", " ", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]
map_copy = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", " ", " ", "#", "#", "#"],
            ["#", "#", "#", "#", "#", " ", " ", " ", " ", "#"],
            ["#", "#", "#", "#", "#", " ", " ", " ", " ", "#"],
            ["#", "#", "#", "#", "#", "#", " ", " ", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]
pond = []
map_width = len(map[0])
map_height = len(map)
alert = ""
clear_command = None

# start
if os.uname().sysname == "Linux":  # os checker
    clear_command = "clear"
else:
    clear_command = "cls"

for pond_y in range(map_height):  # find pond cells
    for pond_x in range(map_width):
        if map[pond_y][pond_x] == cell_list.get("pond"):
            pond.append([pond_y, pond_x])

os.system(clear_command)

print("Введи ник")
name = input()

while True:
    if len(name) == 0:
        os.system(clear_command)
        print("Ты не ввёл ник.\nВведи ник:")
        name = input()
    else:
        break


# main cycle
while True:
    now_time = datetime.datetime.now().timestamp()
    diff_time = now_time - old_time
    now_time_alert = datetime.datetime.now().timestamp()
    diff_time_alert = now_time_alert - old_time_alert

    # keyboard checker
    if keyboard.is_pressed("W") and diff_time > input_delay or keyboard.is_pressed("up") and diff_time > input_delay:
        Y = Y - 1
        old_time = datetime.datetime.now().timestamp()
    if keyboard.is_pressed("A") and diff_time > input_delay or keyboard.is_pressed("left") and diff_time > input_delay:
        X = X - 1
        old_time = datetime.datetime.now().timestamp()
    if keyboard.is_pressed("S") and diff_time > input_delay or keyboard.is_pressed("down") and diff_time > input_delay:
        Y = Y + 1
        old_time = datetime.datetime.now().timestamp()
    if keyboard.is_pressed("D") and diff_time > input_delay or keyboard.is_pressed("right") and diff_time > input_delay:
        X = X + 1
        old_time = datetime.datetime.now().timestamp()

    # render
    os.system(clear_command)
    # print(f"X:{X} Y:{Y} msX:{map_width} msY:{map_height}") # DEBUG
    # print(f"now:{now_time} old:{old_time} diff:{diff_time}") # DEBUG
    # print(f"{pond}") # DEBUG

    for i in range(map_height):  # map render
        print(str(map[i]).translate({ord(n): None for n in "',[]"}))

    print(alert)

    print(f"{hero} - {name}")

    # map refiller
    map[old_y][old_x] = map_copy[old_y][old_x]
    for pond_cell in pond:
        map[pond_cell[0]][pond_cell[1]] = map_copy[pond_cell[0]][pond_cell[1]]

    # logic and other
    if X > map_width - 1:
        X = map_width - 1
    if X < 0:
        X = 0

    if Y > map_height - 1:
        Y = map_height - 1
    if Y < 0:
        Y = 0

    # hero move
    for pond_cell in pond:
        # print(pond_cell) # DEBUG
        if Y == pond_cell[0] and X == pond_cell[1]:
            X, Y = old_x, old_y
            map[Y][X] = hero
            alert = "!!!На пруд нельзя наступить, можно промокнуть!!!!"
            old_time_alert = datetime.datetime.now().timestamp()
        else:
            map[Y][X] = hero
            if diff_time_alert > 1:
                alert = ""

    if keyboard.is_pressed("esc"):  # exit
        os.system(clear_command)
        print("Закрытие...")
        time.sleep(1)
        quit()

    old_x = X
    old_y = Y

    time.sleep(1 / 60)  # set framerate
