import re
class ValidCarNumber:
    def __init__(self, number):
        self.number = number
    def is_valid(self, number):
        is_valid = re.search(r"([0-9]{2})(KG)([0-9]{3})([A-Z]{3})", number)
        if is_valid != None:
            print('Номер валидный!')
        else:
            print('Номер не валидный!')



nomer = ValidCarNumber(0)
nomer.is_valid('01KG123ABC')
