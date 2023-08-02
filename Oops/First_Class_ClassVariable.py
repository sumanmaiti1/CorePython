#--------------- This python file creates constructors for a simpoe class ------------------
#--------------- we have passed object as parameter in Class. By default all the class derives from object class.
#--------------- This is called inheritance which we will discuss later ------------------ 
class Human(object):
    #----------------- This is a Class Varriable . Its value wiil be same for all the objects created for thi sclass -----------
    scientific_name='Homo Sapience'
    #----------- We are creating a constructor here. Constructor By Default returns NONE , hence -->None is written -------------
    #----------- without [-->None] also the code wil run as it is -------------------
    def __init__(self,name,surname,age)-> None:
        #----------------- This is an instance Varriable . Its value wiil be different for each of the objects created for thi sclass -----------
        self.name=name
        self.surname=surname
        self.age=age

#-------------- Creating objects references of the above class ---------------
Human.scientific_name='Hibiscus Rosacynensis'

human1=Human('Suman','Maiti',33)
human2=Human('Sumana','Maiti',29)

#---------------- Here we are accessing / changing the Class variables using WITH and WITHOUT object refference, i.e, outside of class --------------
human1.scientific_name='Gallas Domesticus' # ------This is just an Instance Varriable --------
print(human1.scientific_name)
print(human2.scientific_name)
print(Human.scientific_name,'\n')

human2.scientific_name='Panthera Tigris'# ------This is just an Instance Varriable --------
print(human1.scientific_name)
print(human2.scientific_name)
print(Human.scientific_name,'\n')

Human.scientific_name='Homo Sapience'
print(human1.scientific_name)
print(human2.scientific_name)
print(Human.scientific_name,'\n')

#-------------- Creating another object reference of Human class ---------------

human3=Human('Sri Krishna','Sanatan',1)
print(human1.scientific_name)
print(human2.scientific_name)
print(human3.scientific_name)
print(Human.scientific_name,'\n')