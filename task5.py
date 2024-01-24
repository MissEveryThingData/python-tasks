def task5(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

outcome1 = task5(4, 9, 25)
outcome2 = task5(3, 8, 12)
outcome3 = task5(28, 10, 11)

print(outcome1)  
print(outcome2) 
print(outcome3)  
