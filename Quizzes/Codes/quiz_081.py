class EmployeeSorter:
    def __init__(self, names):
        self.names = names

    def bubble_sort(self):
        n = len(self.names)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                # Extract the last names for comparison
                last_name1 = self.names[j].split(", ")[0]
                last_name2 = self.names[j + 1].split(", ")[0]

                # Compare and swap if necessary
                if last_name1 > last_name2:
                    self.names[j], self.names[j + 1] = self.names[j + 1], self.names[j]

    def get_sorted_names(self):
        return self.names
