'''
 Условия
'''
# if..else
num = int(input("How many times have you been to theHermitage? "))
if num > 0:
 print("Wonderful!")
 print("I hope you liked this museum!")
else:
 print("You should definitely visit theHermitage!")
# if..elif..else
course = int(input("What is your course number?"))
if course == 1:
 print("You are just at the beginning!")
elif course == 2:
 print("You learned many things, but not all ofthem!")
elif course == 3:
 print("The basic course is over, it's time forprofessional disciplines!")
else:
 print("Oh! You need to hurry! June is the monthof thesis defense")
x = 5
y = 12
if y % x > 0: print("%d cannot be evenly divided by%d" % (y,x))
z = 5
x = "{} is a divider of {}".format(z,y)
if y % z==0: print(x)
else:
 print("{} is not a divider of {}".format(z,y))

print("\n\n")