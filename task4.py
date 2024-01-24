def task4(a, b, c):

    s = (a + b + c) / 2

    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    rounded_area = int(area)

    return rounded_area

result1 = task4(3, 4, 5)
print(result1)  

result2 = task4(7, 8, 10)
print(result2)  
