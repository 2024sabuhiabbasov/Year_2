class layer4_firewall:
    def __init__(self, data: str):
        self.data = data
        self.error = True
        self.message = 'None'
        self.length = len(data)

    def converter(self, data: str):
        decimal = 0
        power = 15
        for i in range(self.length - 1, self.length - 17, -1):
            integer = int(data[i])
            decimal += integer * (2 ** power)
            power -= 1
        return decimal

    def msg(self):
        decimal = self.converter(self.data)
        if decimal == 80 or decimal == 22123:
            self.error = False
        if self.error:
            self.message = 'None'
            return "Filtered", self.message
        else:
            return "Allowed", self.data[16: self.length]


layer_4 = layer4_firewall("0000000010100001111")

print(layer_4.msg())
