a = {6, 7, 8, 9, 10}
b = {5, 6, 7, 8, 9}

b.add(4)
print(b)
b.add(3)
print(b)
y = a.difference(b)
print(y)
x=a.union(b)
print(x)
z=a.intersection(b)
print(z)
# quiz2
def list_work():
    lst = [11, 99, 100, 1000, 999, 99]
    print(lst)
    lst.insert(0, -1)
    print(lst)
    print(lst[1])
    print(lst[6])
    count = lst.count(99)
    print(count)
    lst = [11, 99, 100, 1000, 999, 99]
    product = 0
    for x in lst:
        product += x
        print(product)
    least=min(lst)
    print(least)
list_work()
def year_leap():
    for year in range(202,2070):
        if year % 400 == 0 and year % 100 != 0:
            print(year)
        elif year % 4 == 0:
            print(year)
year_leap()
def divisible_by_7():
    for num in range(1000,2000):
        if num%7==0:
            print(num)
        elif num % 5 != 0:
            print(num)
        else:
            print("not a number")
divisible_by_7()
def count():
    for num in range( 10):
        print(num)
count()


def sum(x,y,z):
    print(x+y+z)
sum(23, 45, 12)
def likes(**kwargs):
    for key,value in kwargs.items():
        print ("Students who perform best has {} and are {}".format(key, value))
likes(value="discipline", ability="focused")