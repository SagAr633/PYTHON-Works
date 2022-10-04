# Overriding
# Same method name and same no of arguments
# child class method overrides parent class

class Parent:
    def selectmobile(self):
        print('take samsung s21')
class Child(Parent):
    def selectmobile(self):
        print('take iphone 13')
c=Child()
c.selectmobile()

#Child class method overrides parent class method.

#if there's 2 more child class methods, the latest
#child method is the one going to work.