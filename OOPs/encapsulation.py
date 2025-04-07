class car:
    __brand = "BMW"
    def get_brand(self):
        return self.__brand

newCar = car()

# print(newCar.__brand)
print(newCar.get_brand())
