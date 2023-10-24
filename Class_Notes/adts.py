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

#
# stack = stack()
# stack.push(1)
# print(stack)
# print(stack.pop())
# print(stack.pop())


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


# queue = queue()
# queue.enqueue("test")
# print(queue)
# queue.enqueue("test 1")
# print(queue)
# print(queue.dequeue())
# print(queue)
# print(queue.dequeue())
# print(queue)
# print(queue.dequeue())
# print(queue)
# queue.enqueue("test 2")
# print(queue)
# print(queue.dequeue())
# print(queue)


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
# x = collection()
# x.addItem('bob')
# print(x.hasNext())
# print(x.getNext())
# x.addItem('john')
# print(x.getNext())
# x.removeLast()
# print(x.getNext())


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        out_str = f"Node[{self.data}]"
        temp = self.next
        while temp is not None:
            out_str += f"->Node[{temp.data}]"
            temp = temp.next
        return out_str

    def addNode(self, node):
        if self.next:
            temp = self.next
            node.next = temp
            self.next = node

        else:
            self.next = node


my_list = Node("alice")
print(my_list)
bob_node = Node("bob")
my_list.addNode(bob_node)
print(my_list)
amy_node = Node("amy")
carl_node = Node("carl")
cam_node = Node("cam")

my_list.next.addNode(carl_node)
my_list.addNode(amy_node)
my_list.next.next.addNode(cam_node)

print(my_list)
