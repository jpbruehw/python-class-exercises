"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        "sets the initial start value, default is 100"
        self.start = start
        self.initial_start = start

    def __repr__(self):
        "Shows current value of the incrementor"
        return f"<Current values is: {self.start}"

    def generate(self):
        "Increments the function by one when generate is called"
        next_val = self.start
        next_val += 1
        self.start = next_val
        return next_val

    def reset(self):
        "Resets the value to what was initially passed in"
        self.start = self.initial_start


serial = SerialGenerator()

print(serial.generate())
print(serial.generate())
print(serial.generate())

serial.reset()
print(serial.generate())
print(serial.generate())

print(serial)
