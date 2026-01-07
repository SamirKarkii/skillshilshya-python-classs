# Assigment 6 OOPS
# Task 1: The "Digital Wallet" (Basic Encapsulation)

class Wallet:
    def __init__(self, ownerName= "Samir"):
        self.__ownerName = ownerName
        self.__balance = 0  
        
    def deposit(self, amount):
        if amount>0:
            self.__balance+=amount
            return self.__balance
        else:
            print("Invalide deposite amount ")
    
    def withdraw(self, amounts):
        if self.__balance>=amounts:
            self.__balance-=amounts
            return self.__balance
     
        else:
            print("Insufficient  funds ")

    def getBalance(self):
        return self.__balance


w = Wallet("Alice")
print(w.deposit(100))
print(w.withdraw(50))
print(w.getBalance()) 

# Task 2: The "Smart Light Bulb" (State Management)
# Goal: Understand how methods change the "internal state" of an object without the user touching variables directly.
# The Problem:Create a class called SmartBulb.
# Private Attributes: brightness (Integer) and isOn (Boolean).
# The Logic:
# Constructor: The bulb should start "Off" (false) and brightness at 0.
# turnOn(): Sets isOn to true and sets brightness to 100.
# turnOff(): Sets isOn to false and sets brightness to 0.
# dim(value): * If the bulb is Off, print: "Cannot dim a bulb that is off!"
# If the bulb is On, decrease the brightness by the value, but don't let it go below 0.
# getStatus(): Print whether the bulb is on/off and its current brightness level.
# class SmartBulb:
#     def __init__(self):
#         self.__internal_state = False
#         self.__brightness = 0
    
#     def turnon(self):
#        self.__brightness=100
#        self.__internal_state = True
    
#     def turnoff(self):
#         self.__brightness = 0
#         self.__internal_state = False
    
#     def dim(self,value):
#         if not self.turnon:
#             print("Cannot dim a bulb that is off ")
#         else:
#             self.__brightness -= value
#             if self.__brightness<=0:
#                 self.__brightness=0
#     def get_status(self):
#         state = "On " if self.__internal_state else "off"
#         print(f'bulb is {state},brightness :{self.__brightness}')

# bulb = SmartBulb()

# print(bulb.get_status())
        


# Task 3: The "Car Fuel System" (Validation Logic)
# Goal: Practice using "Setters" to validate data before saving it to an object.
# The Problem:Create a class called Car.
# Private Attributes: modelName (String) and fuelLevel (Integer).
# The Logic:
# Constructor: Set the modelName and set fuelLevel to 50 (percent).
# drive(): Each time this is called, decrease fuelLevel by 10.
# If fuelLevel reaches 0, print: "Out of fuel! Cannot drive."
# refuel(amount):
# If amount + fuelLevel is more than 100, print: "Tank is overflowing! Setting fuel to 100%." and set it to 100.
# Otherwise, add the amount to the current fuel.
# displayFuel(): Show the remaining percentage of fuel.
# class Car:
#     def __init__(self,modelName):
#         self.__modelname=modelName
#         self.__fuellevel=50
#     def drive(self):
#         if self.__fuellevel==0:
#             return "out of fuel"
#         else:
#             self.__fuellevel-=10
#             if self.__fuellevel<0:
#                 self.__fuellevel=0
#             return self.__fuellevel
#     def refuel(self, amount):
        
#         if self.__fuellevel + amount > 100:
#             print("Tank is overflowing!")
#             self.__fuellevel = 100
#         else:
#             self.__fuellevel += amount

#     def displayFuel(self): 
#         return f"remaining fuel is {self.__fuellevel}"


#Create a temperature converter class that can convert temperatures
#betweem Celsius, Fahrenheit, and Kelvin
#The class should have methods to set the termperature in one unit.
#and get the temperature in another unit .
#Use encapsulation to hide the internal methods for conversion.

class Temperatue:
    def __init__(self):
        self.Celsius = 11
        self.Fahrenheit= 11
        self.Kelvin = 11
    
    def Cel(self,ticks):
        if (ticks=="f"):
            return (self.Fahrenheit*9/5)+32
        if (ticks== "k"):
            return (self.Fahrenheit+275.15)
     
    def Kel(self,ticks):
        if (ticks=="f"):
            return (self.Kelvin*9/5)+32
        if (ticks== "c"):
            return (self.Kelvin+275.15)
     
    def Fahr(self,ticks):
        if (ticks=="c"):
            return (self.Fahrenheit*9/5)+32
        if (ticks== "k"):
            return (self.Fahrenheit+275.15)
    
    
a = Temperatue()
print(a.Cel("k"))
print(a.Fahr("c"))
print(a.Kel("c"))





    
