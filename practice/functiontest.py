# Function and Constructs
def my_function():
    print('hello world!')

my_function()

def my_function1(name):
    print('hello '+name+'!')

my_function1('DevOps')

def my_function2(**fruits):
    print('First fruit is {} and count is {}'.format(fruits["fruit"],fruits["count"]))

my_function2(fruit="apple", count=2)

#class with a constructor#

class Fruits:
    def __init__(self,name,count):
        self.name=name
        self.count=count
    def showFruits(self):
        print('Fruit name is {} and count {}'.format(self.name,self.count))

apple=Fruits("apple",2)
orange=Fruits("orange",3)

apple.showFruits()
orange.showFruits()