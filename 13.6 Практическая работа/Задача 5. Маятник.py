amplitude = float(input("Введите начальную амплитуду: "))
if amplitude > 
amplitude_copy = amplitude
stop = float(input("Введите амплитуду остановки: "))
fluctuations = 0

while amplitude > stop:
    fluctuations += 1
    amplitude -= (amplitude * 8.4) / 100

print(f"Маятник считается остановившимся через {fluctuations} \nНачальная амплитуда {amplitude}, конечная амплитуда {amplitude_copy}")

