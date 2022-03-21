#1-------------------------
def a():
    sum = 0
    for i in range(10):
        sum +=i
    print(sum)

a()

#2-----------------------
def is_year_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(is_year_leap(int(input("Введите год: "))))

#3----------------------------
import math

def square(a):
    p=1*a
    s=a**2
    d=math.sqrt(2)*a

    return p, s, d

print(square(int(input("Введите сторону квадрата: "))))

#3----------------------------
def is_prime(n):
    d=2
    while n % d !=0:
        d+=1
    return d==n

n=int(input("Введите число: "))
print(is_prime(n))

#4------------------
import random
N=10
arr=[0]*N

for i in range(N):
    arr[i]=random.randint(1,100)

def average(arr):
    s=0
    for i in range(N):
        s+=arr[i]
    return s/N

print(arr)
print(average(arr))

#5---------------------------------
def season(num):
    if num==12<=2:
        print("зима")

    elif 3<=num<=5:
        print("весна")

    elif 6<=num<=8:
        print("лето")

    elif 9<=num<=11:
        print("осень")

    else:
        print("Неверно введен номер месяца!")

int(input("Введите номермесяца(1-12): "))

season(n)




