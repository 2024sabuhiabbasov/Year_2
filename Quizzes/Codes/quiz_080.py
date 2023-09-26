import random


class average:
    def __init__(self, a: list):
        # Constructor to initialize an instance of the class with a list 'a' as its attribute
        self.a = a

    def sum(self):
        sum = 0
        for i in range(len(self.a)):
            sum += self.a[i]  # Add the current element 'a[i]' to the sum
        return sum  # Return the sum of elements in the list

    def average(self):
        l = len(self.a)  # Get the length of the list 'a'
        return self.sum() / l  # Calculate and return the average by dividing the sum by the length

    def average_2(self):
        i = 0
        l = len(self.a)  # Get the length of the list 'a'
        sum = 0
        while i < l:
            sum += self.a[i]  # Add the current element 'a[i]' to the sum
            i += 1  # Increment the loop counter
        return sum / l  # Calculate and return the average using a while loop

    def average_3(self):
        sum = 0
        for i in range(len(self.a)):
            # Generate a random integer 'k' between the minimum and maximum values in 'a'
            k = random.randint(min(self.a), max(self.a))
            while k != self.a[i]:
                # Keep generating 'k' until it matches the current element 'a[i]'
                k = random.randint(min(self.a), max(self.a))
            sum += k  # Add 'k' (which matches 'a[i]') to the sum
        return sum / len(self.a)  # Calculate and return the unusual average
