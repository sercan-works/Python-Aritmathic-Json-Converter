import json
from Sort import *
from validators import validate_numbers

checked_numbers = []

f = open('numbers.json')

data = json.load(f)


# def check_int(num):
#     if type(num) == int :
#         checked_numbers.append(num)
#     else:
#         raise TypeError("Listede sadece sayısal değerler olmalıdır." )
     
def sort_numbers(): 
    if len(data['numbers']) <= 1: 
        raise Exception("Listeye birden fazla değer giriniz.")
    else:
        for number in data['numbers']:
            validate_numbers(number)
            checked_numbers.append(number)
        return bool(True)
    
    
try:   
    sort_numbers()   
    print('Default___________:',data['numbers'])    
    # print('Aritmetik sıralı__:\n',json.dumps(sorted(checked_numbers),indent=3))

    quickSort(checked_numbers,0,len(checked_numbers)-1)
    print('Aritmetik QuickSort sıralı__:\n',json.dumps(sorted(checked_numbers),indent=3))

    f.close()
except:
    print('Bir hata oluştu')

    
