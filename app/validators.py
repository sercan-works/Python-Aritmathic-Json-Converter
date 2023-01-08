def validate_numbers(number):
    if type(number) == int :
        return bool(True)
    else:
        raise TypeError("Listede sadece sayısal değerler olmalıdır." )