# ------ This is my first class -------

class Human:
    """
    -------- This is the documentation for the class --------------------
    -------- This is my first class. it's the most simple class ---------
    """
    pass


# --------- Creating an object named obj1 for Human class ----------
obj1 = Human()
# ----------- Assigning the values for obj1 object ----------------
obj1.name = 'Suman'
obj1.surname = 'Maiti'
obj1.age = 100

# --------- Creating an object named obj2 for Human class ----------
obj2 = Human()
# --------- Creating an object named obj2 for Human class ----------
obj3 = Human()
# ----------- Assigning the values for obj2 object ----------------
obj2.name = 'Sumana'
obj2.surname = 'Maiti'
obj2.age = 80

# ----------- printing the values for all the objects ----------------
print(f'My name is {obj1.name} {obj1.surname} and i am {obj1.age} years old')
print(obj1, type(obj1), id(obj1), obj1.__class__)
print(f'My name is {obj2.name} {obj2.surname} and i am {obj2.age} years old')
print(obj2, type(obj2), id(obj2))
print(obj3, type(obj3), id(obj3))
# ---------------- Below code will generate Attribute error -------------
print(obj3.name, obj3.surname, obj3.age)
