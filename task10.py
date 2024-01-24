def task10(str1, str2):
    
    str1 = str1.lower()
    str2 = str2.lower()

  
    common_chars = set(str1) & set(str2)

    task10 = [char for char in common_chars if char.isalpha()]
    task10.sort()

    if len(task10) > 2:
        result = ', '.join(task10[:-1]) + " and " + task10[-1]
    elif len(task10) == 2:
        result = task10[0] + " and " + task10[1]
    elif len(task10) == 1:
        result = task10[0]
    else:
        result = "no common letters"

    print(result)


task10("House", "computers")  
task10("Hi", "there")        
task10("Foo", "bar")         
