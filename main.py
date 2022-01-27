class Objetos:
    count = 0
    def __init__(self):
        Objetos.count += 1
        self.number = self.count


c1 = Objetos()
print(Objetos.count)
c2 = Objetos()
print(Objetos.count)
c3 = Objetos()
print(Objetos.count)


print(c1.count, c2.count, c3.count)
print(c1.number, c2.number, c3.number)
