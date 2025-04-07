fp = open("text.txt", "r", encoding='utf-8')
lines = fp.readlines()
print(lines)
fp.close()