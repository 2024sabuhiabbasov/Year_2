class palindromic:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.palindromic_list = []

    def reverser(self, number: int):
        number = str(number)
        number = list(number)
        reversed_number = ''
        for i in range(len(number) - 1, -1, -1):
            reversed_number += number[i]
        return int(reversed_number)

    def reverse_checker(self, number: int):
        return number == self.reverser(number)

    def list_generator(self):
        for i in range(self.a, self.b + 1):
            if self.reverse_checker(i):
                self.palindromic_list.append(i)

        return self.palindromic_list


palindromic_numbers = palindromic(1, 999)
list_of_palindromic_numbers = palindromic_numbers.list_generator()
print(list_of_palindromic_numbers)
