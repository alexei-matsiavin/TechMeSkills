number = '231456897'
audience = 4
place = 5
place_number = number[audience:]
place_number = sorted(place_number)
place_number = place_number[::-1]
place_number = ''.join(place_number)
print(place_number)