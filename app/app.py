from numbers import numbers

checked_numbers = []



def check_num(num):
    if type(num) == int:
        checked_numbers.append(num)
    else:
        raise ValueError('NUMARA OLMAYAN DEĞER')
    
    
    # if num.isdigit() == True:
    #     print(number)
    # else:
    #     raise('Dizi içinde alfabetik öğe var!')

for number in numbers:
    check_num(number)
    print(checked_numbers)