import random
random_words = open('slova.txt',encoding="utf-8").read().split()
for i in range (random.randint(1, 10)):
    print (random.choice(random_words), end=' ')