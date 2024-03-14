def print_area(area):
    for i in area:
        print(i)


def check_winner(area):
    if area[0][2] == "кресло" and area[1][2] == "шкаф":
        return True
    else:
        return False


room = [
    ["стол", "стул", "шкаф"],
    ["стул", "", "кресло"]
]

print_area(room)

while not check_winner(room):

    current_row = int(input("Из какой строки взять ")) - 1
    current_column = int(input("Из каково столбца взять ")) - 1

    next_row = int(input("В какую строку поставить ")) - 1
    next_column = int(input("В какой столбец поставить ")) - 1

    item = room[current_row][current_column]

    if room[next_row][next_column] != "":
        print("ход не возможен")
    else:
        room[next_row][next_column] = item
        room[current_row][current_column] = ""

    print_area(room)

print("Поздравляю вы справились!")