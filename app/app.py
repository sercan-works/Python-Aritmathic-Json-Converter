import json
from numbers import numbers

from sort import *

checked_numbers = []



def check_num(num):
    if type(num) == int :
        checked_numbers.append(num)
    else:
        raise TypeError("Listede sadece sayısal değerler olmalıdır." )
     
    if len(numbers) <= 1:
        raise Exception("Listeye birden fazla değer giriniz.")

 
 
 
for number in numbers:
    check_num(number)
    
    
print('Default___________:',numbers)    
# print('Aritmetik sıralı__:\n',json.dumps(sorted(checked_numbers),indent=3))

quickSort(checked_numbers,0,len(checked_numbers)-1)
print('Aritmetik QuickSort sıralı__:\n',json.dumps(sorted(checked_numbers),indent=3))