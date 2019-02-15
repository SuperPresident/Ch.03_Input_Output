'''
Grading PROGRAM
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''



grade=float(input("What's the grade \n"))
test=float(input("What's your test score\n"))
worth=float(input("What's the worth?\n"))

worth=worth/100

overall=grade*(1-worth)+test*worth

print ("your overall grade is",letter,"%")

if overall>=100 and worth==0:
    letter="A+"
elif overall>=100:
    letter="you are a lucky Guessere"
elif overall>=90:
    letter="A"
elif overall>=80:
    letter="B"