dict = {
    "name": "7D 건조 망고",
            "type": '식품',
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치차황색소"],
    "orgin": "필리핀"

}




for key,value in dict.items():
    print(f"{key}: {value}")
print()


dict["name"] = "8D건조망고"
print("name:", dict["name"])
print(dict)