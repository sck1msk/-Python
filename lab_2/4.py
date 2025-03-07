def calculate_median (a, b, c):
    
    if ( b<= a <= c ) or (c <= a <= b):
        return a
    elif (a <= b <= c) or (c <= b <= a):
        return b 
    else:
        return c 

try: 
    print("Введите три числа для нахождения медианы:")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))

    median = calculate_median(num1, num2, num3)
    print(f"Медиана введенных чисел: {median}")

except ValueError:
    print("Пожалуйста, введите корректное значение.")5
    