#--------------- This python file creates constructors for a simpoe class ------------------
#--------------- we have passed object as parameter in Class. By default all the class derives from object class.
#--------------- This is called inheritance which we will discuss later ------------------ 
class Human(object):
    #----------- We are creating a constructor here. Constructor By Default returns NONE , hence -->None is written -------------
    #----------- without [-->None] also the code wil run as it is -------------------
    def __init__(self,name,surname,age)-> None:
        #----------------- This is an instance Varriable . Its value wiil be different for each of the objects created for thi sclass -----------
        self.name=name
        self.surname=surname
        self.age=age
        print(f'My name is {self.name} {self.surname} and i am {self.age} years old. Currently i am inside Class Constructor.')

#-------------- Creating objects references of the above class ---------------

human1=Human('Suman','Maiti',33)
human2=Human('Sumana','Maiti',29)

#---------------- Here we are accessing  the instance variables using object refference --------------
print('\n')
print(f'My name is {human1.name} {human1.surname} and i am {human1.age} years old. Currently i am accessing instance variables using Objects of Human Class.')
print(f'My name is {human2.name} {human2.surname} and i am {human2.age} years old. Currently i am accessing instance variables using Objects of Human Class.\n')

#---------------- Here we are changing the instance variables using object refference, i.e, outside of class --------------

human1.age = 100
human2.name = "Beauty"

#---------------- Here we are accessing  the instance variables using object refference --------------
print(f'My name is {human1.name} {human1.surname} and i am {human1.age} years old. Currently i am accessing instance variables using Objects of Human Class.')
print(f'My name is {human2.name} {human2.surname} and i am {human2.age} years old. Currently i am accessing instance variables using Objects of Human Class.')
