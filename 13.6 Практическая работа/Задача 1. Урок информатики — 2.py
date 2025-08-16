import math

num_1 = float(input("Введите число: "))
if num_1 < 0:
    print("Число не соответствует условию!")
else:
    exponent = math.floor(math.log10(num_1))
    mantissa = num_1 / (10 ** exponent)

    x = mantissa * 10 ** exponent
    print(f"{mantissa} * 10 ** {exponent}")