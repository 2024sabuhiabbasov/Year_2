class checker:
    def __init__(self, data: str):
        self.data = data
        self.error = False

    def error_check(self):
        length = len(self.data) // 3
        data_arr = []
        for letter in self.data:
            data_arr.append(letter)
        original = data_arr[0:length]
        copy_1 = data_arr[length:length*2]
        copy_2 = data_arr[length*2:length*3]
        for i in range(0, length):
            if original[i] == copy_1[i] and copy_2[i] != original[i]:
                self.error = True
                pass
            elif original[i] == copy_2[i] and copy_1[i] != original[i]:
                self.error = True
                pass
            elif copy_1[i] == copy_2[i] and original[i] != copy_2[i]:
                self.error = True
                original[i] = copy_1[i]
        output = ''
        for binary in original:
            output = output + str(binary)
        return self.error, output

error_checker = checker("101010101011")
output = error_checker.error_check()
print(output)