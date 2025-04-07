with open('info.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, weight, height = line.strip().split(", ")

        if not name or not weight or not height:
            continue

        bmi = int(weight) / (float(height) / 100) ** 2

        if bmi >= 25:
            result = "과체중"
        elif bmi >= 18.5:
            result = "정상체중"
        else:
            result = "저체중"

        print(f"이름: {name} 몸무게: {weight}  키: {height} BMI: {bmi:.2f} 결과: {result}")