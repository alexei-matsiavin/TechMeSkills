number_vasia = '59876'
number_vasia = [_ for _ in number_vasia]
position_slice = 0
for position in range(len(number_vasia)-1):
    if number_vasia[position] < number_vasia[position+1]:
        position_slice = position
# print(position_slice)
# print(number_vasia[position_slice:])
slice_iteration = number_vasia[position_slice+1:]
max_iter_number = number_vasia[position_slice]
if number_vasia[position_slice+1] > min(slice_iteration[1:]):

elif number_vasia[position_slice+1] < min(slice_iteration):



# print(place_number)