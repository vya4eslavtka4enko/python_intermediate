#Optional Parameters Tutorial #1

def func(x=1):
    return x**2

call = func(5)
print(call)

def func_2(word, freq=1)
    print(word*freq)
    
call = func('mark')


class Car(object):
    def __init__(self,make,model,year,condition='New',kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms
        
    def display(self,showAll):
        if showAll:
            print("This car is a %s %s from %s,it is %s and has %s kms."%(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This car is a %s %s from %s" %(self.make, self.model, self.year))

whip = car("Ford", 'Fusion', 2012)
whip.display(True)

#Static and Class Methods #2

class person(object):
    population = 50
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    @classmethod
    def getPopulation(cls)
        return cls.population
    
    @staticmethod
    def isAdult(age):
        return age >= 18
    
    def display(self):
        print(self.name, 'is', self.age, 'years old')
        
        
newPerson = person('Mark',18)

#map function

li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

print(list(map(func,li)))

#print([func(x) for x in li])

#4 Filter Function

def add7(x):
    return x+7

def isOdd(x):
    return x%2 != 0

a = [1,2,3,4,5,6,7,8,9,10]

b = list(filter(isOdd,a))

c = list(map(add7,filter(isOdd,a)))

#Lambda Tutorial

a = [1,2,3,4,5,6,7,8,9,10]

newList = list(filter(lambda x: x%2==0))
print(newList)


#Containers
import collection
from collection import Counter

#list
#set
#dict
#tuple - inmuttable

#Types
#1 counter <- this video
#2 deque
#3 nameTuple()
#4 orderDict
#5 defaultdict

c = Counter(a=4,b=2,c=0,d=-2)
d = [a,b,b,c]

c.subtract(d)
print(c)
c.update(d)
    