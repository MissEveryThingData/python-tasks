def task9(input_string):
    
    vowels = 'aeiou'

    extracted_vowels = []

    for char in input_string:
       
        if char.lower() in vowels:
            extracted_vowels.append(char.lower())

    sorted_vowels = sorted(extracted_vowels)

    return sorted_vowels


result1 = task9('Two Owls and a Hen,')
print(result1)  

result2 = task9('')
print(result2) 
    