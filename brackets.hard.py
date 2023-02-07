# text = '()(()[([()])])'
# text = '[(()()]([]))'
# text = '(([[])[]]()()'
text = '[4 * (45 - 6 * (56 -1 )+ 45 - (56 + 34)]*(4 - 6 *[34 - 43])'
text = [symb for symb in text if symb =='(' or symb ==')' or symb =='[' or symb ==']']
text = ''.join(text)
counter_1 = len([symb for symb in text if symb =='('])
counter_2 = len([symb for symb in text if symb =='['])
n = 0
while n < max(counter_1, counter_2):
    text = text.split('()')
    text = ''.join(text)
    text = text.split('[]')
    text = ''.join(text)
    n += 1
if text == '':
    print(True)
else:
    print(False)

