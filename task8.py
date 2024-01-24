def task8(minutes):
    if minutes == 0:
        return '0 hours, 0 minutes'
    elif minutes == 1:
        return '0 hours, 1 minute'
    else:
        hours = minutes // 60
        remainder_minutes = minutes % 60

        if hours == 1:
            hours_str = '1 hour'
        else:
            hours_str = f'{hours} hours'

        if remainder_minutes == 1:
            minutes_str = '1 minute'
        else:
            minutes_str = f'{remainder_minutes} minutes'

        return f'{hours_str}, {minutes_str}'

print(task8(0))    
print(task8(1))    
print(task8(60))   
print(task8(120))  
print(task8(121))  
print(task8(71))   
print(task8(133))  