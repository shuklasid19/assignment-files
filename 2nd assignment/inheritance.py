#first base class
class linkinpark:
    def __init__(self, name, records, role):
        self.name = name
        self.records = records
        self.role = role
    
    def info(self):
        return f"the name is {self.name} records_sold is {self.records} and role is {self.role}"

#2nd base class
class cal1:
    def mul(self, a, b):
        return f"the multiplicatin is {a*b}"
    
    def add(self, a, b):
        return f"the addition is {a + b}"

#class inherited both 2 class 
class derived(linkinpark, cal1):
    pass
    

#calling our derived class which inherited all 2 base classes
#and passing values as our derived class doesnt take any
#creating the object of derived class
al = derived("chester bennigton", 23423, "leadsinger")

#mul method is no defined in derived class but it inherited from base class
print(al.mul(32, 34))
#and we are able to call it from derived class because of inheritance

print(al.add(23,34))

#same here 
print(al.info())