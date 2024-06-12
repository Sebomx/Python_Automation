'''
 Функции
'''
def condition(name, age):
 print(f"Hello {name}!")
 print(f"Your age is {age}!")
 print('-'*20)

condition("Anton", 25)

condition("Alex", 20)

#------------------------------------------------
def numbers_sum(num1, num2):
 return num1 + num2
 #print(num1 + num2)
 #print('-'*20)

print(numbers_sum(num1=2, num2=5))
result = numbers_sum(num1=25, num2=35)
print(result)
print('-' * 20)
print("\n")



def dictUpdate(a):
 a.update([("x",5)])
 print("dict in function: ",a)
 return
def dictNoUpdate(a):
 a = a.copy()
 a.update([("y",3)])
 print("dict in function: ",a)
 return
def returnFunc(a):
 def f1(a):
  print("returned f1(a): ",a)
 return f1
d= {"v":7}
dictUpdate(d)
print("dict out of function: ",d)
dictNoUpdate(d)
print("dict out of function: ",d)
f = returnFunc(d)
print("f: ", f)
f(2)
print("\n")
