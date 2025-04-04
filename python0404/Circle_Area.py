def circle_area(r):
    result = 3.14 * (r ** 2)
    return result

if __name__ == "main":
    radius = 3
    area = circle_area(radius)
    print("반지름: %d, 면저기 %.2f" % (radius, area))
