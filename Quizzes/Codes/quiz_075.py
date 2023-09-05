class converter():
    def __init__(self, data: str):
        self.data = data
        self.ascii_codes = []
        self.binary = ''

    def ascii_converter(self):
        for letter in self.data:
            self.ascii_codes.append(odr(letter))