#Write a Python program to create a class representing a Circle. 
#Include methods to calculate its area and perimeter.
import math

class Circle():
    '''
    This class will deal with Circle type shape. 
    To create an instance :- Circle(radious)
    '''
    #------------------- Constructor of Circle class -----------------
    def __init__(self,radious) -> None:
        self.__radious=radious
    
    #------------------ Representation of Circle class ----------------
    def __str__(self) -> str:
        return(f'Circle({self.__radious})')

    #------------------- Getter method of Circle class -----------------
    def get_radious(self):
        '''
        This is public method and it return the radious of the circle instance
        '''
        return (self.__radious)
    
    #------------------- Setter method of Circle class -----------------
    def set_redious(self,new_radious):
        '''
        This is a public method and it will set update the radious of a circle
        '''
        self.__radious=new_radious
        print(f'Radious of the Circle is updated succerssfully. New Radious {self.__radious}')
    
    #------------------- Method of calculate perimeter of Circle class -----------------
    def perimeter(self):
        '''
        This is a public method . It will calculate and return perimeter of a circle
        '''
        return(2*math.pi*self.__radious)
    
        #------------------- Method of calculate perimeter of Circle class -----------------
    def area(self):
        '''
        This is a public method . It will calculate and return area of a circle
        '''
        return(math.pi*pow(self.__radious,2))
    

c1=Circle(3)
print(c1.get_radious())
c1.__radious=4
print(c1.get_radious())
print(c1.perimeter())
print(c1.area())
c1.set_redious(5)
print(c1.get_radious())
c1.__radious=6
print(c1.get_radious())
print(c1.__radious)
print(c1.area())
print(c1.perimeter())
print(c1)