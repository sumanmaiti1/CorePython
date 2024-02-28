#Write a Python program to create a person class. Include attributes like name, country and date of birth. 
#Implement a method to determine the person's age.
import datetime

class Person():
    '''
    This is person class. It has attributes as name, country and date of birth(DD-MM-YYYY).
    '''

    #------------------------- This is class constructor ------------------------
    def __init__(self,name='Default Name',country='India',dob='01-01-2000')->None:
        try:
            self.__name = name
            self.__country=country
            self.__dob=dob
            self.__dobdate=''
            try:
                self.__dobdate=datetime.datetime.strptime(self.__dob,'%d-%m-%Y')
            except ValueError as e:
                print(f'Please provide valid Date of Birth in DD-MM-YYYY format and try again.\nError generated:-{e}')
                exit()
        except Exception as err:
            print(f'Runtime error occurred while trying to instanciate Person. Error Generated:-{err}')
            exit()

    def __str__(self):
        return(f'Person({self.__name,self.__country,self.__dob})')
    
    def give_person_details(self):
        return(f'Person Name :- {self.__name}\n Person country :- {self.__country}\n Persion DOB :- {self.__dob}\n difference :- {self.__calculate_age()}')

    def __calculate_age(self):
        __todaysdate=datetime.datetime.now()
        __datediff=__todaysdate-self.__dobdate
        print(__datediff)
    

p1=Person('Suman Maiti','India','20-05-1990')
p1.give_person_details()