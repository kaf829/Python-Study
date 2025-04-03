def print_n_time(value, n=2):
    for i in range(n):
        print(value)

print_n_time(3,5)


def print_n_time(*values ,n =2 ):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_time("12","123", "123", n = 3)





