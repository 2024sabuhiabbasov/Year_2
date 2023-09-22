class stack:
    def __init__(self):
        self.data = []

    def pop(self):
        l = len(self.data)
        end_code = "\033[00m"
        red = "\033[0;31m"
        if self.data:
            item = self.data[l - 1]
            self.data = self.data[:l - 1]
        else:
            item = f"{red}[ERROR] Stack out of index{end_code}"
        return item

    def push(self, item):
        data = [item]
        self.data = data + self.data

    def __repr__(self):
        return f"<Stack> {self.data}"

stack = stack()
stack.push(1)
print(stack)
print(stack.pop())
print(stack.pop())


class queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        end_code = "\033[00m"
        red = "\033[0;31m"
        if self.data:
            item = self.data[0]
            self.data = self.data[1:]
            return item
        else:
            return f"{red}[ERROR] Queue out of index{end_code}"

    def __repr__(self):
        return f"<Queue> {self.data}"


queue = queue()
queue.enqueue("test")
print(queue)
queue.enqueue("test 1")
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
queue.enqueue("test 2")
print(queue)
print(queue.dequeue())
print(queue)


class collection:
    def __init__(self):
        self.data = []
        self.location = 0

    def addItem(self, item):
        self.data.append(item)

    def isEmpty(self) -> bool:
        return len(self.data) == 0

    def hasNext(self) -> bool:
        return self.location == len(self.data) - 1

    def getNext(self):
        end_code = "\033[00m"
        red = "\033[0;31m"
        if self.hasNext():
            item = self.data[self.location]
            self.location += 1
        else:
            item = f"{red}[ERROR] Collection out of index{end_code}"
        return item

    def resetNext(self):
        self.location = 0

    # My own method to attract customers
    def removeLast(self):
        self.data = self.data[0:len(self.data) - 1]
        self.location -= 1


# imagining  how the user would use our ADI
x = collection()
x.addItem('bob')
print(x.hasNext())
print(x.getNext())
x.addItem('john')
print(x.getNext())
x.removeLast()
print(x.getNext())
