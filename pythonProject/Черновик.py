a = [1,2,3,4,5]
a.append(10)
a.extend([15,16,17])
a.insert (1,23)
a.remove(3)
#el=a.pop()
print(a)
print ("\n")



people = ["Tom", "Sam", "Bob"]
i = 0
while i < len(people):
    print(people[i])    # применяем индекс для получения элемента
    i += 1
print("-"*20)



def condition(name, age):
 print(f"Hello {name}!")
 print(f"Your age is {age}!")
condition("Anton", 25)
print("\n")
print("-"*20)

print("Numbers (for):")
for i in range(0, 10):
    print(i, end="")
print("\n")
print("-"*20)

print("Numbers (while):")
i = 0
while (i < 10):
    print(i, end="")
    i += 1