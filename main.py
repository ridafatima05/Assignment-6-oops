# 1. Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


# 2. Using cls
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")


# 3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car started")


# 4. Class Variables and Class Methods
class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


# 5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


# 6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger initialized")

    def __del__(self):
        print("Logger destroyed")


# 7. Access Modifiers: Public, Protected, Private
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")


# 8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")


# 11. Class Methods
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


# 13. Composition
class Engine:
    def start(self):
        print("Engine started")

class CarWithEngine:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


# 14. Aggregation
class Department:
    def __init__(self, employee):
        self.employee = employee

class EmployeeAggr:
    def __init__(self, name):
        self.name = name


# 15. Method Resolution Order (MRO)
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass


# 16. Function Decorators
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")


# 17. Class Decorators
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class PersonWithGreet:
    pass


# 18. Property Decorators
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price


# 19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


# 20. Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18")
    print("Age is valid")


# 21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val


# Testing the classes and their methods
if __name__ == "__main__":
    # 1. Using self
    student = Student("Alice", 95)
    student.display()

    # 2. Using cls
    c1 = Counter()
    c2 = Counter()
    Counter.display_count()

    # 3. Public Variables and Methods
    car = Car("Honda")
    car.start()

    # 4. Class Variables and Class Methods
    print("Bank name:", Bank.bank_name)
    Bank.change_bank_name("XYZ Bank")
    print("New bank name:", Bank.bank_name)

    # 5. Static Methods
    print("Sum:", MathUtils.add(10, 20))

    # 6. Constructors and Destructors
    log = Logger()
    del log

    # 7. Access Modifiers
    emp = Employee("John", 50000, "123-45-6789")
    emp.show_info()

    # 8. The super() Function
    t = Teacher("Mr. Smith", "Math")
    print(f"Teacher: {t.name}, Subject: {t.subject}")

    # 9. Abstract Classes and Methods
    r = Rectangle(4, 5)
    print("Area of Rectangle:", r.area())

    # 10. Instance Methods
    dog = Dog("Buddy", "Labrador")
    dog.bark()

    # 11. Class Methods
    Book.increment_book_count()
    Book.increment_book_count()
    print("Total books:", Book.total_books)

    # 12. Static Methods
    print("Fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(0))

    # 13. Composition
    engine = Engine()
    car_with_engine = CarWithEngine(engine)
    car_with_engine.start()

    # 14. Aggregation
    emp_aggr = EmployeeAggr("Jane")
    dept = Department(emp_aggr)
    print("Employee in Department:", dept.employee.name)

    # 15. MRO
    d = D()
    d.show()

    # 16. Function Decorator
    say_hello()

    # 17. Class Decorator
    p = PersonWithGreet()
    print(p.greet())

    # 18. Property Decorators
    product = Product(150)
    print("Product Price:", product.price)
    product.price = 200
    print("Updated Price:", product.price)
    del product.price

    # 19. Callable Object
    multiplier = Multiplier(3)
    print("Is multiplier callable?", callable(multiplier))
    print("Multiplied result:", multiplier(5))

    # 20. Custom Exception
    try:
        check_age(16)
    except InvalidAgeError as e:
        print("Error:", e)

    # 21. Iterable Countdown
    print("Countdown:")
    for i in Countdown(3):
        print(i)
