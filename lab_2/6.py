def ordinal_date(day, month, year):
    
    import datetime
    date = datetime.date(year, month, day)
    start_of_year = datetime.date(year, 1, 1)
    return (date - start_of_year).days + 1

print("\nВведите дату для вычисления порядкового номера дня:")
day = int(input("День: "))
month = int(input("Месяц: "))
year = int(input("Год: "))

ordinal = ordinal_date(day, month, year)
print(f"Порядковый номер дня: {ordinal}")