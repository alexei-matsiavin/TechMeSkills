text = 'MR.OWLATEMYMETALWORM'
new_text = text[::-1]
print(new_text)
if text == text[::-1]:
    print(True)
else:
    for position in range(int(len(text)/2)+1):
        a = text[position]
        b = new_text[position]
        c = text[position+1]
        if text[position] != new_text[position]:
            if text[position+1] != new_text[position]:
                if text[position] != new_text[position]:
                    print(False)
                    break
    else:
        print(True)



