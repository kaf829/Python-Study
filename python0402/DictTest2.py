dict = {
    "name": "7D 건조 망고",
            "type": '식품',
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치차황색소"],
    "orgin": "필리핀"

}

keyName = input("Key를 입력하세요")

if keyName in dict:
    print(f"{dict[keyName]}가 존재합니다")
else:
    print("key가 존재하지 않습니다")