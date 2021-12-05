words = 0
chars = 0
num_chars = 0
uniques = set()
for line in open('tekst.txt', encoding = 'utf-8'):
    chars += len(line)
    word_list = ' '.join(line.splitlines()).split()
    for x in word_list:
        num_chars += len(x)
    pos = 'out'
    for char in line:
        if char != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif char == ' ':
            pos = 'out'
    uniques |= set(line.split())
print("Загальна кількість символів:", chars)
print ("Кількість символів без пробілів:", num_chars)
print("Кількість слів:", words)
print ("Кількість унікальних слів:", len(uniques))