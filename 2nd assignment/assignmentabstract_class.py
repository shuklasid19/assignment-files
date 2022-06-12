#abstract class is a class that cannot be instantiated.
#python has module for defining an abstract class and abstract method
#abstract class to create a blueprint for other classes
from abc import ABC , abstractmethod
#defining abstract class with passing ABC
#the decorator is used to define an abstractmethod 

#this is an abstract class ABC defines 
class album(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        

       
    def band_member(self):
        return self.first_name + self.last_name
    

    #its an abstractmethod decorator defines it @abstractmethid
    #the derived class must have this method
    @abstractmethod
    def records_sold(self):
        pass
    

#derived class
#new_album class inherit from an abstract class
class new_album(album):
    #constructor and were inheriting the album properties
    def __init__(self, first_name, last_name, records):
        super().__init__(first_name, last_name)
        self.records = records
    

    def records_sold(self):
        return self.records

first_album  = new_album("chester", "bennigton", 34231)

print(first_album.records_sold())

print(first_album.band_member())

#we have to define this records_sold method otherwise itll throw an error
#when we instantiate objects