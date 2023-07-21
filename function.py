def is_leap(year):
    leap = False
    
    # Write your logic here
    return bool(not(year%400) if not(year%100) else not(year%4))
    return leap

year = int(input())
print(is_leap(year))