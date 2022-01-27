class Class1:
    def func1(self):
        print("Метод func1() класса Class1")

class Class2(Class1):
    def func2(self):
        print("Метод func2() класса Class2")

class Class3(Class1):
    def func1(self):
        print("Метод func1() класса Class3")
    def func2(selfs):
        print("Метод func2() класса Class3")
    def func3(self):
        print("Метод func3() класса Class3")
    def func4(self):
        print("Метод func4() класса Class3")

class Class4(Class2, Class3):
    func2 = Class3.func2
    def func4(self):
        print("Метод func4() класса Class4")

c = Class4()
c.func1()
c.func2()
c.func3()
c.func4()

print(Class1.__bases__)
print(Class2.__bases__)
print(Class3.__bases__)
print(Class4.__bases__)

print("Новая ветка")