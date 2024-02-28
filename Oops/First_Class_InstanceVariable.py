# --------------- This python file creates constructors for a simple class ------------------
# --------------- we have passed object as parameter in Class. By default, all the class derives from object class.
# --------------- This is called inheritance which we will discuss later ------------------ 
class Human(object):
    # -------- This is a Class Variable . Its value will be same for all the objects created for this class -----------
    scientific_name = 'Homo Sapience'

    # ------- We are creating a constructor here. Constructor By Default returns NONE , hence -->None is written -----
    # ----------- without [-->None] also the code wil run as it is -------------------
    # ----------- Here we are controlling what type of data to be entertained in __init__ ---------------
    def __init__(self, name: str, surname: str, age: int) -> None:
        # ---------- Here we are doing some validations on the parameters --------
        try:
            assert len(name) >= 3, f'{name} should be at least 3 character long'
            assert len(surname) >= 3, f'{surname} should be at least 3 character long'
            assert age > 0, f'{age} should be greater than Zero'

            self.name = name
            self.surname = surname
            self.age = age

            print(f'My name is {self.name} {self.surname} and i am {self.age} years old.')

        except Exception as e:
            print(e)

        # -------------- Creating objects references of the above class ---------------


human1 = Human('Suman', 'Maiti', 33)
human2 = Human('Sumana', 'Maiti', 29)
human3 = Human('ab', 'Maiti', 10)  # ------------ This will raise exception -------------
human4 = Human('abc', 'de', 10)  # ------------ This will raise exception -------------
human5 = Human('abc', 'def', 0)  # ------------ This will raise exception -------------
