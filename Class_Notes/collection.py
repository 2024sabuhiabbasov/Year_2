# collection
class collection:
    def __init__(self):
        self.data = []
        self.location = 0

    def addItem(self, item):
        self.data.append(item)

    def isEmpty(self) -> bool:
        return len(self.data) == 0


# imagining  how the user would use our ADI
x = collection()
x.addItem('bob')
print(x.isEmpty())
