sum = 0
sum += 1
sum += 2
sum += 3
sum += 4
print(sum)

sum = 1 + \
      2 + \
      3 + \
      4
print(sum)

sum = (
    1 +
    2 +
    3 +
    4
)
print(sum)

disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

furry = True
large = True
if furry:
    if large:
        print("It's a yeti.")
    else:
        print("It's a cat!")
else:
    if large:
        print("It's a whale!")
    else:
        print("It's a human. Or a hairless cat.")

color = "mauve"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know it is, but only bees can see it")
else:
    print("I've never heard of the color", color)

some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")

letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' \
or letter == 'o' or letter == 'u':
    print(letter, "is a vowel")
else:
    print(letter, "is not a vowel")

vowels = 'aeiou'
letter = 'o'
if letter in vowels:
    print(letter, 'is a vowel')

letter = 'o'
vowel_set = {'a', 'e', 'i', 'o', 'u'}
if letter in vowel_set:
    print(letter, 'is a vowel')
vowel_list = ['a', 'e', 'i', 'o', 'u']
if letter in vowel_list:
    print(letter, 'is a vowel')
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
if letter in vowel_tuple:
    print(letter, 'is a vowel')
vowel_dict = {'a':'apple','e':'elephant', 'i':'impala', 'o':'ocelot','u':'unicorn'}
if letter in vowel_dict:
    print(letter, 'is a vowel')
vowel_string = "aeiou"
if letter in vowel_string:
    print(letter, 'is a vowel')

tweet_limit = 280
tweet_string = "Blah" * 50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))

tweet_limit = 280
tweet_string = "Blah" * 50
diff = tweet_limit - len(tweet_string)
if diff := tweet_limit - len(tweet_string) >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))