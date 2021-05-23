class employee:
    pass
obj = employee()
#####Creating Class and Object in Python
class employees:

    # class attribute
    position = "worker"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the employee class
gautami = employees("gautami", 35)
watson = employees("watson", 25)

# access the class attributes
print("gautami is a {}".format(gautami.__class__.position))
print("Watson is also a {}".format(watson.__class__.position))

# access the instance attributes
print("{} is {} years old".format( gautami.name, gautami.age))
print("{} is {} years old".format( watson.name, watson.age))


###Creating Methods in Python
class employees:

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def DA(self, python):
        return "{} DA {}".format(self.name, python)

    def ENGG(self):
        return "{} is now scientist ".format(self.name)


# instantiate the object
gautami = employees("gautami", 35)

# call our instance methods
print(gautami.DA("'also'"))
print(gautami.ENGG())


##Use of Inheritance in Python
# parent class
class employee:

    def __init__(self):
        print("employee is coder")

    def whoisThis(self):
        print("employee")

    def run(self):
        print("code faster")


# child class
class dataAnalyst(employee):

    def __init__(self):
        # call super() function
        super().__init__()
        print("dataAnalyst is coder")

    def whoisThis(self):
        print("dataAnalyst")

    def plan(self):
        print("faster")


gautami = dataAnalyst()
gautami.whoisThis()
gautami.run()


##Data Encapsulation in Python
class CellPhone:

    def __init__(self):
        self.__maxprice = 850

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = CellPhone()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()


####Using Polymorphism in Python
class ITEmployee:

    def code(self):
        print("ITEmployee can code")

    def plan(self):
        print("ITEmployee can't plan")


class MarketingAnalyst:

    def code(self):
        print("MarketingAnalyst can't code")

    def plan(self):
        print("MarketingAnalyst can plan")


# common interface
def coding_test(person):
    person.code()


# instantiate objects
gautami = ITEmployee()
watson = MarketingAnalyst()

# passing the object
coding_test(gautami)
coding_test(watson)


