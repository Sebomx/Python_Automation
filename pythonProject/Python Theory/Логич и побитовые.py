'''
Логические операции
'''
f = True
g = False
print("f: ", f)
print("g: ", g)
print("not f: ", f)
print("f and g: ", f and g)
print("f or g: ", f or g)
print("f == g: ", f == g)
print("f != g", f != g)
print("\n")
h = 3
i = 5
print("h = ", h)
print("i = ", i)
print("h > i: ", h > i)
print("h < i: ", h < i)
print("h >= i: ", h >= i)
print("0 < h < i: ", 0 < h < i)
print("\n\n")
'''
Побитовые операции
'''
j = 7
k = 20
print("j = %d; j in binary format: %s" % (j, bin(j)))
print("k = %d; k in binary format: %s" % (k, bin(k)) )
print("j & k: %d; binary: %s" % (j & k, bin(j & k)) ) # побитовое AND
print("j | k: %d; binary: %s" % (j | k, bin(j | k)) ) # побитовое OR
print("j ^ k: %d; binary: %s" % (j ^ k, bin(j ^ k)) ) # побитовое XOR
print("~k: %d; binary: %s" % (~k, bin(~k)) ) # инверсия двоичного числа
print("k>>1: %d; binary: %s" % (k>>1, bin(k>>1)) ) # сдвиг на один бит вправо
print("k<<1: %d; binary: %s" % (k<<1, bin(k<<1)) ) # сдвиг на один бит влево
print("\n\n")