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

print(letters[20:])
print(letters[12:15])
print(letters[-3:])
print(letters[18:-3])
print(letters[-6:-2])
print(letters[::7])
print(letters[4:20:3])
print(letters[19::4])
print(letters[:21:3])
print(letters[-1::-1])
print(letters[::-1])

print(len(letters))
empty = ""
print(len(empty))

tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
print(tasks.split(','))

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals: ', crypto_string)

setup = 'a duck goes into a bar...'
print(setup)
print(setup.replace('duck', 'marmoset'))
print(setup)
print(setup.replace('a ', 'a famous ', 100))
print(setup.replace('a', 'a famous ', 100))

world = "      earth      "
print(world)
print(world.strip())
print(world.strip(' '))
print(world.lstrip())
print(world.rstrip())
print(world.strip('!'))

blurt = "What the...!!?"
print(blurt)
print(blurt.strip('.?!'))

import string
print(string.whitespace)
print(string.punctuation)
print(blurt.strip(string.punctuation))
prospector = "What in tarnation ...??!!"
print(prospector)
print(prospector.strip(string.whitespace + string.punctuation))

