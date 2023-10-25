class Citizen:
    def __init__(self, name: str, city: str, status: str):
        self.name = name
        self.city = city
        self.status = status

    def getName(self):
        return self.name

    def getCity(self):
        return self.city

    def getStatus(self):
        return self.status


class Employee(Citizen):
    def __init__(self, name, city, status, salary: int):
        self.annual_salary = salary
        Citizen.__init__(self, name, city, status)


class PartTimeEmployee(Employee):
    def __init__(self, name, city, status, salary, fraction: int, union: bool):
        Employee.__init__(name, city, status, salary)
        self.fraction = fraction
        self.union_member = union


citizen = Citizen('Bob', 'Tokyo', 'alive')
print(f"{citizen.getName()} is in {citizen.getCity()} and {citizen.getStatus()}")

employee = Employee('alice', 'Kyoto', 'alive', 100000)

part_timer = PartTimeEmployee('Joe', 'Nagano', 'alive', 500000, 0.5, False)

