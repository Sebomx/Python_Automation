'''
 Строки
'''
group = input("What is your group number? ")
print("Your group is ",group)
print("\nString:")
# получение символов строки в цикле (1)
for i in range(0,len(group)):
 print(group[i], end=" ")
print("\nString:")
# получение символов строки в цикле (2)
for elem in group:
 print(elem, end=" ")
print("\n")
s = "Hello, World!"
print(s)
num = s.count('o')    #подсчет количества повторов символа "о" в строке
print("Count 'o': ",num)
ind = s.find("world")  #возвращает номер позиции в строке (в данном случае -1 т.к world в нижнем регистре
print("Find 'world' (by find()): ",ind)
ind = s.find("World")
print("Find 'World' (by find()): ",ind)
ind = s.index("World")
print("Find 'World' (by index()): ",ind)
print("Find 'World' (by in operation): ", "World" in s)
print("\nReplace substring:")
s1 = s.replace("Hello", "hello")
print(" Old: {} \n New: {} ".format(s, s1))
l1 = s.split(",")
print("List l1 (splitted): ",l1)
l2 = s.partition(",")
print("List l2 (partitioned): ",l2)
s2 = s
print("Copy s in s2; s2: ",s2)
sep = "|"
l = ["h","e","l","l","o"]
s = sep.join(l)
print(s)
print("\n")
st = "Привет, мир!"
st1 = st.encode("utf-8")
print("Encoding utf-8:\n",st1)
st2 = st.encode("cp1251")
print("Encoding cp1251:\n",st2)
st3 = st2.decode("cp1251")
print("Decoding cp1251:\n",st3)