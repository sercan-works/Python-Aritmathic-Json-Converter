import json


from Sort import *

checked_numbers = []

f = open('numbers.json')

data = json.load(f)


def check_num(num):
    if type(num) == int :
        checked_numbers.append(num)
    else:
        raise TypeError("Listede sadece sayısal değerler olmalıdır." )
     
    if len(data['numbers']) <= 1:
        raise Exception("Listeye birden fazla değer giriniz.")

 
 
 
for number in data['numbers']:
    check_num(number)
    
    
print('Default___________:',data['numbers'])    
# print('Aritmetik sıralı__:\n',json.dumps(sorted(checked_numbers),indent=3))

quickSort(checked_numbers,0,len(checked_numbers)-1)
print('Aritmetik QuickSort sıralı__:\n',json.dumps(sorted(checked_numbers),indent=3))

f.close()