class Animal():
    legs = 4
    eyes = 2
    tail = True
    ears = 2
    teeths = True

    def eat(self):
        print("Ням ням ням")

    def sleep(self):
        print("Zz-Zz-Zz-Zz")

    def walk(self):
        print("Гуляю")

murzik = Animal()
bobik = Animal()
print(murzik.legs)
murzik.sleep()