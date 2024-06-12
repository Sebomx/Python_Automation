'''
 Циклы
'''
# while
print("Numbers < 10 (while):")
i = 1
while (i<10):
 print(i, end = " ") # print in one line
 i += 1
print("\n")

# for
print("Numbers < 10 (for):")
for i in range(0,10):
 print(i, end=" ")
else:
 print("\nThe next number is 10\n")

# break
sum = 0
for i in range(0,100):
  if i > 10:
   print("\nWe reached the end, final sum: ", sum)
   break
  sum += i

# continue
i = 0
while i<=15:
  if i % 3 == 0:
    i += 1
    continue
  print(i, end=" ")
  i += 1
print("\n")

# pass
print("Let's print numbers again!")
for i in range(0,10):
  pass
  print(i, end=" ")
print("\n\n")

'''
Вложенные циклы
'''
i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1