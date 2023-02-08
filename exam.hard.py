number_vasia = '58976'
number_vasia = [int(_) for _ in number_vasia]
position_slice = 0
for position in range(len(number_vasia)-1):
    if number_vasia[position] < number_vasia[position+1]:
        position_slice = position
# print(position_slice)
# print(number_vasia[position_slice:])
slice_iteration = number_vasia[position_slice+1:]
max_iter_number = number_vasia[position_slice]
if max_iter_number < max(slice_iteration):
    part_1 = number_vasia[:position_slice+1]
    a = part_1[-1]
    part_2 = number_vasia[position_slice+1:]
    b = part_2.index(a+1)
    part_1[-1], part_2[b] = part_2[b], part_1[-1]
    part_1.extend(sorted(part_2))
    print(part_1)


# elif number_vasia[position_slice+1] < min(slice_iteration):



print(number_vasia)