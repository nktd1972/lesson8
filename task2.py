def _math(a, b):
    c = a * a / b
    return c


while True:
    try:
        num_a = int(input(f'Enter number a = '))
        num_b = int(input(f'Enter number b = '))
        cc = _math(num_a, num_b)
        print(f'Result c={cc}')
    except ValueError:
        print("Oops!  That was no valid number(must be a number).  Try again...")
    except ZeroDivisionError:
        print("Oops!  That was no valid number(must be not 0).  Try again...")
