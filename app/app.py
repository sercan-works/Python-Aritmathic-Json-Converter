import json
from Sort import *
from validators import validate_numbers

checked_numbers = []

 
def sort_numbers(data=None):
    if data==None:
        f = open('numbers.json')

        data = json.load(f)
        f.close()
 
        numbers = data['numbers']
    
    else:
        numbers = data
        
    if len(numbers) <= 1: 
        raise Exception("Listeye birden fazla değer giriniz.")
    else:

        for number in numbers:
            validate_numbers(number)
            checked_numbers.append(number)
    
        return QuickSort(checked_numbers)
    
    
    
try:   
    sort_numbers()  
    
    print('Aritmetik QuickSort sıralı__:\n',json.dumps(QuickSort(checked_numbers),indent=3))

        
except:
    print('Bir hata oluştu.Listede en az 2 değer ve sadece number kullanılmalı.')

    
