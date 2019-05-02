import random
import string


class Generator:

    def __init__(self, num, count):
        self.set_num_count(num, count)

    def set_num_count(self, num, count):
        if (num <= 0) or (count <= 0):
            raise ValueError("None of the numbers can not be 0 or negative !")
        self.num = num
        self.count = count

    def gener_number(self):
        passw_count = []
        i = 1
        while i <= self.count:
            var = "".join(random.choices(string.digits, k=self.num))
            passw_count.append(var)
            i = i + 1
        return passw_count

    def gener_letters(self):
        passw_count = []
        i = 1
        while i <= self.count:
            var = "".join(random.choices(string.ascii_letters, k=self.num))
            passw_count.append(var)
            i = i + 1
        return passw_count

    def gener_letters_numbers(self):
        passw_count = []
        i = 1
        while i <= self.count:
            var = "".join(random.choices(
                string.ascii_letters+string.digits, k=self.num))
            passw_count.append(var)
            i = i + 1
        return passw_count

    def gener_custom(self, symbols):
        passw_count = []
        i = 1
        while i <= self.count:
            var = "".join(random.choices(symbols, k=len(symbols)))
            passw_count.append(var)
            i = i + 1
        return passw_count