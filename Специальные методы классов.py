class House:
    def __init__(self, number_of_floors = 0):
        self.number_of_floors = number_of_floors
    def setNew_number_of_floors(self, floors):
        self.floors = floors
        self.number_of_floors = floors
        return self.number_of_floors
h = House(3)
print(h.number_of_floors)






