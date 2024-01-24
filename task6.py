def task6(*args):
    if not args:
        raise ValueError("No arguments provided")
    
    max_num = args[0]
    for num in args[1:]:
        if num > max_num:
            max_num = num
    return max_num

outcome1 = task6(1, 2, 44, 3)
outcome2 = task6(-1, -2, -44, -3, -5)
outcome3 = task6(8, 8, 8, 8, 8, 8, 8)

print(outcome1)  
print(outcome2)  
print(outcome3)  
