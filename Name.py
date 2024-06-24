my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
indeks = 0
while indeks < len(my_list):
    if my_list[indeks] > 0:
        print(my_list[indeks])
        indeks += 1
    elif my_list[indeks] == 0:
        indeks += 1
    else:
        break
