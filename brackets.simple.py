text = '(345 - (345 + 1) *2) -5)*( 5+ 6*( 1- (45-23)*7 +56)'
count = 0
for symbol in text:
    if symbol == '(':
        count += 1
    elif symbol == ')':
        count -= 1
    if count < 0:
        print(False)
        break
else:
    if count == 0:
        print(True)
    else:
        print(False)
