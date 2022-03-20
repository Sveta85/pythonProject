#1----------------------
class TheExample:
    a=2
    b=3
    def __init__(self, t, r):
        self.t=t
        self.r=r

    def func(self):
        self.c=5
        print(self.c)

    def func1(self):
        return self.a+self.b

    def func2(self):
         return self.t**self.r

example=TheExample(4,2)
print(example.a)
print(example.func1())
print(example.func2())
example.func()

#2-----------------------
class TheExample:
    def __init__(self):
        self.func4()
    def func(self):
        return self.a + self.b
    def func1(self):
        return self.a - self.b
    def func2(self):
        return self.a * self.b
    def func3(self):
        if self.b == 0:
            return "error"
        else:
            return self.a / self.b
    def func4(self):
        self.a = int(input())
        self.b = int(input())
while True:
    print("+,-,*,/")
    x = input()
    print("Numbers:")
    example = TheExample()
    if x == "6":
        break
    if x == "+":
        print(example.func())
    if x == "-":
        print(example.func1())
    if x == "*":
        print(example.func2())
    if x == "/":
        print(example.func3())

#D\z-----------------------------------
class TheExample:

    def __init__(self):
        self.h = 0
        self.d = 0
        self.g = 0
        self.gl = []
        self.sgl = []

    def func(self,a):
        if type(a) is str:
            for i in a:
                if i in "aeoiu":
                    self.h +=1
                    self.gl.append(i)
                else:
                    self.d += 1
                    self.gl.append(i)
            print("Количество гласных", self.h)
            print("Количество согласных", self.d)
            print("Длина слова", self.func1(a))
            if (self.h * self.d) <= self.func1(a):
                print("Гласные:", self.gl)
            else:
                print("Согласные:", self.sgl)
        elif type(a) is int:
            for i in str(a):
                i = int(i)
                if (i % 2) == 8:
                    self.g +=i
            print("ПРоизведение:", self.g * self.func1(a))

    def func1(self, a):
        return len(str(a))

example = TheExample()
c = input()
if c.isalpha():
    example.func(c)
elif c.isdigit():
    example.func(int(c))