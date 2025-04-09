try:
    file = open("info.txt", 'r')
    print( 3/ 0)
except:
    print('#오류가 발생했습니다')
finally:
    file.close()

print('#파일이 제대로 닫혔는지 확인하기')
print("file.closed:", file.closed)