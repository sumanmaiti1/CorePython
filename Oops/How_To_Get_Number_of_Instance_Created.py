# --------------- This code is to determine How many instance is created for a class----------------
# --------------- This code will also tell the object is Nth instance of class ----------------

class TestClass(object):
    # --------- Static Variable-----------
    no_of_instance = 0
    total_no_of_instance = 0

    # ----------- Constructor of the class ---------------
    def __init__(self) -> None:
        TestClass.no_of_instance += 1
        TestClass.total_no_of_instance += 1
        # self.no_of_instance=TestClass.no_of_instance

        print(f'Alive instance created for TestClass :- {TestClass.no_of_instance}')
        print(f'Total instance created for TestClass :- {TestClass.total_no_of_instance}')
        print(f'This object is [{TestClass.no_of_instance}] instance of {type(self).__name__} \n')

    def __del__(self) -> None:
        TestClass.no_of_instance -= 1
        print(f'This object is getting Deleted')
        print(f'Total instance alive for TestClass :- {TestClass.no_of_instance} \n')
    # ---------------- creating object reference here ---------------------


obj1 = TestClass()
obj2 = TestClass()
obj3 = TestClass()
obj4 = TestClass()
del obj1
del obj3
obj3 = TestClass()
obj1 = TestClass()
print('suman')
