import csv

f = open('output.csv', 'w', encoding= 'utf-8', newline='')

# quotchar = '"' : 데이터를 묶을 문자 지정
# csv.QUOTE_ALL : 모두 사용하겠다는 의미


wr = csv.writer(f, delimiter=",", quotechar='"', quoting= csv.QUOTE_ALL)
wr.writerow([1,"김정수", False])
wr.writerow([2,"박상미", True])

f.close()