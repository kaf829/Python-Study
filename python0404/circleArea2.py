pi = 3.141592

def circle_area_with_pi(r):
    pi = 3.14
    result = pi * (r**2)
    return result

def circle_area_without_pi(r):
    result = pi * (r **2)
    return result

def sum_areas():
    result = [circle_area_with_pi(3), circle_area_without_pi(3)]
    return sum(result)


if __name__ =="__main__":
    print("PI:" , pi)
    print("반지름", 3 ,"면적", circle_area_with_pi(3))
    print("반지름", 3 ,"면적", circle_area_without_pi(3))
    print(sum_areas())
