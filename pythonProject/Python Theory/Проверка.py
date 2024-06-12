marks_auto = ["Opel", "Volvo", "BMW"]
print(marks_auto[-1])
marks_auto.append("Toyota")
print(marks_auto)
marks_v2=marks_auto.pop(1)
print(marks_v2)
print(marks_auto)



marks_auto_color = {"Opel":"Черный", "Volvo":"Белый", "BMW":"Красный"}
print(marks_auto_color["Volvo"])
marks_auto_color["Volvo"] = "Синий"
print(marks_auto_color)
print("\n")

'''
Если мы перечислим все натуральные числа до 10, кратные 3 или 5, мы получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Завершите решение так, чтобы оно вернуло сумму всех чисел, кратных 3 или 5, для числа 1000.
'''
#number % 2 == 0
def solution(number):
    d = 0
    for i in range(number):
        #print(i)
        if i % 3 == 0:
            #print("3-", i)
            d += i
        elif i % 5 == 0:
            #print("5-", i)
            d += i
    print(d)

solution(1000)


#-----------------------------------------------------------------

def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]
abbrevName("Sam Harris")



def fake_bin(x):
    d = 0
    for i in range(x):
        if i < 5 == 0:
            d+=i
        elif i > 5 == 1:
            d+=i
    print(d)
    pass

fake_bin(["4,5"])