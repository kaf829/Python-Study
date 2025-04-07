fp = open("text.txt", "r", encoding='utf-8')
lines = fp.readlines()

for line in lines:
    print(line, end = '')

fp.close()