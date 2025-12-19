class chai:
    def __init__(self, sweetness_level, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level


    def sip(self):
        print("Sipping Chai")


    def add_sugar(self, amount):
        print("Added The Sugar")

my_chai(sweetness=3, milk_level=2)

my_chai.add_sugar(3)