import math

circleArea = math.pi*5**2
print("This is the area of a circle with radius 5:" , circleArea)

sphereVolume = (4/3)*math.pi*3**3
print("This is the volume of a sphere of radius 3:" , sphereVolume)

hypotenuseLength = 3**2+4**2
print("This is the length of the hypotenuse of a right triangle with side lengths 3 and 4:", hypotenuseLength)

myName = "Josef Corbin"
print("The numbers of letters in my name is:" ,len(myName))

#Demonstration concatenation of strings in python
myNameFirst = "Josef"
myNameLast = "Corbin"
print(myNameFirst , myNameLast)
#printing my name in upper case
print("This is what my name looks like on my Social Security Card:" , myName.upper())
#Printing my full name in lower case
print("And if I don't pay attention when I type:" , myName.lower())

myAgeYears = 24
myHeightFeet = 6.167
myHeightInches = 74
myWeightPounds = 150
BMI = (myWeightPounds/(myHeightInches*myHeightInches))*703

print("My BMI is:" , BMI)