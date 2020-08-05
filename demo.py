def isum(num1, num2):
    return "Sum of two arguments is: ", num1 + num2


isum_result = isum(5, 10)


class DemoClass:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return "{name}"
