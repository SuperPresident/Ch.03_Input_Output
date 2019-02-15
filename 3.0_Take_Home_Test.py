'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: _____Darius____



1. Write a line of code that will print your name.
'''
print('Darius')


2. Write a program that asks someone for their name and then prints their name to the screen?

name=input("whats your name\n")
print(name)
'''
3. Predict the output of the following lines of code and then test them? Write down your prediction and the output.
print (17/9)  1?   1.8888888
print (17//9) 1?    1
print (17%9) 2?    8  
'''


'''
4. Write a a program where a user enters a base and height and you print the area of a triangle.

'''
b=int(input("What's the  base?\n"))
h=int(input("What's the height?\n"))
print("The area is", (b*h)/2)

'''
5. Change this program so it works.
A=("May the Force be with you!")
print(a)
'''




'''
6. Write a line of code that will ask the user for the length of a square's
side and then print the area of the square
'''
s=int(input("What's the  length of a side?\n"))
print("The area is",s**2)

'''7. Ask a user for the length of radii of an ellipse and then print its area. 
Area=pi*a*b where a and b are the lengths of the major radii.
'''
import math
a=int(input("What's the  length of axis a?(larger)\n"))
b=int(input("What's the  length of a axis b?(smaller\n"))
print("The area is", (a*b*math.pi))

'''
8. Ask a user for moles, volume and temperature of a gas and print out the pressure. PV=nRT where n is the number of moles, T is the absolute temperature, V is the
volume, and R is the gas constant 8.3144.
'''
R=.08206
n=float(input("what is the moles\n"))
T=float(input("what is the temperature\n"))
V=float(input("what is the volume\n"))
P=( (n*R*abs(T))/V)
print("The pressure is",P)
'''
9. Ask a user for an integer and then print the square root.
'''a=int(input("What's number are you thinking about?)\n"))
import math
a=int(input("What's number are you thinking about?)\n"))
print("The square root is", math.sqrt(a))

'''
10. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. Ask the user for mass and acceleration
and then print out the Force on one line and "Get it?" on the next.
'''

m=float(input("what is the mass\n"))
a=float(input("what is the acceleration\n"))
print(m*a ,"\nGet it?")