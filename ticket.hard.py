text = '123459' # не счачтливый билет 123789
text_list = [int(num) for num in text]
new_list = text_list.copy()
sum_1, sum_2, n = 0, 1, 0
if sum(text_list) % 2 == 0:
    while sum_1 != sum_2:
        for num_j in range(4):
            sum_1 = sum(text_list[:3])
            sum_2 = sum(text_list[3:])
            if sum_1 != sum_2:
                text_list.append(text_list.pop(2))
            else:
                print(True)
                break
        text_list.append(text_list.pop(1))
        n += 1
        if n >= 5:
            print(False)
            break
else:
    print(False)

