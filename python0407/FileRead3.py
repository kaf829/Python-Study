fp = open("text.txt", "r", encoding='utf-8')

while True:
    line = fp.readline()
    if line == '':
        break
    print(line.strip())

fp.close()