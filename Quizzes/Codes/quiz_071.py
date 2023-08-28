import random
import time

class ipv6machine():
    def __init__(self, number: int):
        self.number = number

    def sixtec_generator(self):
        characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F']
        ip_address = ''
        for i in range(0, 8):
            sixtec = ''
            for j in range(0, 4):
                random_num = random.randint(0, 16)
                sixtec = sixtec + characters[random_num]
            ip_address = ip_address + sixtec
            if i != 7:
                ip_address = ip_address + ':'
        return ip_address

    def list_generator(self):
        list = []
        for i in range(0, self.number):
            ip = self.sixtec_generator()
            while ip in list:
                ip = self.sixtec_generator()
            list.append(ip)
        return list

# start_time = time.time()
ipv6 = ipv6machine(1000)
# end_time = time.time()
print(ipv6.list_generator())
# print(end_time-start_time)