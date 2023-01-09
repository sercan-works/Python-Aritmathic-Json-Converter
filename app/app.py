import json
from Sort import *
from validators import validate_numbers

checked_numbers = []

f = open('numbers.json')

data = json.load(f)
 
def sort_numbers(data):
    
    if len(data) <= 1: 
        raise Exception("Listeye birden fazla değer giriniz.")
    else:
        
        for number in data:
            validate_numbers(number)
            checked_numbers.append(number)
            
        return QuickSort(checked_numbers)
    
    
try:   
    sort_numbers(data["numbers"])   
    print('Default___________:',data['numbers'])    
    # print('Aritmetik sıralı__:\n',json.dumps(sorted(checked_numbers),indent=3))
    
    print('Aritmetik QuickSort sıralı__:\n',json.dumps(QuickSort(checked_numbers),indent=3))

    f.close()
except:
    print('Bir hata oluştu.Listede en az 2 değer ve sadece number kullanılmalı.')

    
