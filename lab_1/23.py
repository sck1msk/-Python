def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False 
    elif year % 4 == 0:
        return True
    else: 
        return False


year = int(input("введите год:"))


if is_leap_year(year):
    print (f"Год {year} является високосным")
else:  
    print(f"Год {year} не является високосным")


