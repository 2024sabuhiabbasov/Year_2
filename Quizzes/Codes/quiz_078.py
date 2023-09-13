class layer4_firewall:
    def __init__(self, data:str):
        self.data = data
        self.error = True
        self.message = 'None'
        self.length = len(data)

    def converter(self, data: str):
        decimal = 0
        power = 0
