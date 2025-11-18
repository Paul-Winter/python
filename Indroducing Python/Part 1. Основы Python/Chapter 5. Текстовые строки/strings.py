print('Snap')
print("Crackle")

poem = '''There was a Young Lady of Norway,
Who casually sat in a doorway;
When th door squeezed her flat,
She exclaimed, "What of that?"
This courageous Young Lady of Norway.'''

print(poem)

print('Give', "us", '''some''', """space""")

print(str(98.4))
print(str(1.0e4))
print(str(True))

palindrome = 'A man,\nA plan,\nA canal:\nPanama.'
print(palindrome)

print('\tabc')
print('a\tbc')
print('ab\tc')
print('abc\t')

info = r'Type a \n to get a new line in a normal string'
print(info)

vowels = ('a' + "e" + '''i''' + 'o' + """u""")
print(vowels)

a = 'Duck. '
b = a
c = 'Grey Duck!'
print(a + b + c)
print(a, b, c)

print(a * 4)
print(c * 3)

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[1])
print(letters[-1])
print(letters[-2])
print(letters[25])
print(letters[5])

name = 'Henny'
print(name)
print(name.replace('H', "P"))
print(name)
print('P' + name[1:])