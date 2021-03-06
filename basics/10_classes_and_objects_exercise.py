class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def __init__(self, name, color, kind, value):
        self.name = name
        self.color = color
        self.kind = kind
        self.value = value

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (
            self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle("Fer", "red", "convertible", 60000.00)
car2 = Vehicle("Jump", "blue", "van", 10000.00)

print(car1.description())
print(car2.description())
