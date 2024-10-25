# Task 1: Kvadratning perimetri 
a = int(input("Kvadrat tomonini kiriting: "))
P = 4 * a
print("Kvadratning perimetri: ", P)

# Task 2: Kvadratning yuzi 
S = a ** 2
print("Kvadratning yuzi: ", S)

# Task 3: To'g'ri to'rtburchakning perimetri va yuzi 
a = int(input("To'g'ri to'rtburchakning tomoni a ni kiriting: "))
b = int(input("To'g'ri to'rtburchakning tomoni b ni kiriting: "))
S = a * b
P = 2 * (a + b)
print("To'g'ri to'rtburchakning yuzi: ", S)
print("To'g'ri to'rtburchakning perimetri: ", P)

# Task 4: Aylananing uzunligi 
d = int(input("Aylananing diametri d ni kiriting: "))
pi = 3.14
L = pi * d
print("Aylananing uzunligi: ", L)

# Task 5: Kubning hajmi va to'la yuzi 
a = int(input("Kubning tomoni a ni kiriting: "))
V = a ** 3
S = 6 * a ** 2
print("Kubning hajmi: ", V)
print("Kubning to'la yuzi: ", S)

# Task 6: Parallelepipedning hajmi va to'la yuzi 
a = int(input("Parallelepipedning tomoni a ni kiriting: "))
b = int(input("Parallelepipedning tomoni b ni kiriting: "))
c = int(input("Parallelepipedning tomoni c ni kiriting: "))
V = a * b * c
S = 2 * (a * b + b * c + a * c)
print("Parallelepipedning hajmi: ", V)
print("Parallelepipedning to'la yuzi: ", S)

# Task 7: Doiraning radiusi va yuzasi 
R = int(input("Doiraning radiusi R ni kiriting: "))
L = 2 * pi * R
S = pi * R ** 2
print("Doiraning uzunligi: ", L)
print("Doiraning yuzi: ", S)

# Task 8: Ikkita sonning o'rta arifmetigi 
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
mean = (a + b) / 2
print("O'rta arifmetigi: ", mean)

# Task 9: Ikkita sonning o'rta geometrigi 
geo_mean = (a * b) ** 0.5
print("O'rta geometrigi: ", geo_mean)

# Task 10: Ikki sonning yig'indisi, ko'paytmasi va kvadrati 
sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2
print("Yig'indisi: ", sum_ab)
print("Ko'paytmasi: ", product_ab)
print("a ning kvadrati: ", square_a)
print("b ning kvadrati: ", square_b)

# Task 11: Ikki sonning yig'indisi, ko'paytmasi va modul qiymatlari 
modulus_a = abs(a)
modulus_b = abs(b)
print("a ning moduli: ", modulus_a)
print("b ning moduli: ", modulus_b)

# Task 12: To'g'ri uchburchakning gipotenuzasi va perimetri 
a = int(input("To'g'ri uchburchakning tomoni a ni kiriting: "))
b = int(input("To'g'ri uchburchakning tomoni b ni kiriting: "))
hypotenuse = (a ** 2 + b ** 2) ** 0.5
perimeter = a + b + hypotenuse
print("To'g'ri uchburchakning gipotenuzasi: ", hypotenuse)
print("To'g'ri uchburchakning perimetri: ", perimeter)

# Task 13: Ikki aylananing yuzalari va ularning ayirmasi 
R1 = int(input("Birinchi aylananing radiusi R1 ni kiriting: "))
R2 = int(input("Ikkinchi aylananing radiusi R2 ni kiriting: "))
S1 = pi * R1 ** 2
S2 = pi * R2 ** 2
S3 = S1 - S2
print("Birinchi aylananing yuzi: ", S1)
print("Ikkinchi aylananing yuzi: ", S2)
print("Yuzalarning ayirmasi: ", S3)

# Task 14: Aylananing uzunligi 
L = 2 * pi * R1
print("Aylananing uzunligi (R1 bilan): ", L)

# Task 15: Aylananing yuzi 
d = int(input("Aylananing diametri d ni kiriting: "))
R = d / 2
S = pi * R ** 2
print("Aylananing yuzi (d bilan): ", S)

# 16-task: Sonlar o'qida ikkita nuqta orasidagi masofa
z1 = int(input("Birinchi nuqta z1 ni kiriting: "))
z2 = int(input("Ikkinchi nuqta z2 ni kiriting: "))
distance = abs(z2 - z1)
print("Nuqtalar orasidagi masofa: ", distance)

# 17-task: AC va BC kesmalari uzunliklari yig'indisi
A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))
C = int(input("C ni kiriting: "))
AC = abs(C - A)
BC = abs(C - B)
sum_AC_BC = AC + BC
print("AC va BC segmentlari yig'indisi: ", sum_AC_BC)

# 18-task: AC va BC segmentlarining ko'paytmasi
product_AC_BC = AC * BC
print("AC va BC segmentlarining ko'paytmasi: ", product_AC_BC)

# 19-task: To'g'ri to'rtburchakning perimetri va yuzi
x1 = int(input("To'g'ri to'rtburchakning birinchi koordinatasi (x1): "))
y1 = int(input("Birinchi koordinataning y1 qiymati: "))
x2 = int(input("Ikkinchi koordinata (x2): "))
y2 = int(input("Ikkinchi koordinataning y2 qiymati: "))
length = abs(x2 - x1)
width = abs(y2 - y1)
perimeter = 2 * (length + width)
area = length * width
print("To'g'ri to'rtburchakning perimetri: ", perimeter)
print("To'g'ri to'rtburchakning yuzi: ", area)

# 20-task: Tekislikdagi ikkita nuqta orasidagi masofa
x1 = int(input("Birinchi nuqta x1 ni kiriting: "))
y1 = int(input("Birinchi nuqta y1 ni kiriting: "))
x2 = int(input("Ikkinchi nuqta x2 ni kiriting: "))
y2 = int(input("Ikkinchi nuqta y2 ni kiriting: "))
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Nuqtalar orasidagi masofa: ", distance)

# 21-task: Uchburchakning yuzi va perimetri
x1 = int(input("Birinchi uch nuqta (x1, y1) uchun x1 ni kiriting: "))
y1 = int(input("y1 ni kiriting: "))
x2 = int(input("Ikkinchi nuqta (x2, y2) uchun x2 ni kiriting: "))
y2 = int(input("y2 ni kiriting: "))
x3 = int(input("Uchinchi nuqta (x3, y3) uchun x3 ni kiriting: "))
y3 = int(input("y3 ni kiriting: "))

# Tomonlarning uzunligini hisoblash
a = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
b = ((x3 - x2)**2 + (y3 - y2)**2) ** 0.5
c = ((x3 - x1)**2 + (y3 - y1)**2) ** 0.5

# Perimetr
p = (a + b + c)/2


# Yuzi (Geron formulasi orqali)
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print("Uchburchakning perimetri: ", perimeter)
print("Uchburchakning yuzi: ", area)

# 22-task: A va B sonlarini almashtirish
A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))
A, B = B, A
print("A ning yangi qiymati: ", A)
print("B ning yangi qiymati: ", B)

# 23-task: A, B, C sonlarini almashtirish (A -> B, B -> C, C -> A)
A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))
C = int(input("C ni kiriting: "))
A, B, C = B, C, A
print("A ning yangi qiymati: ", A)
print("B ning yangi qiymati: ", B)
print("C ning yangi qiymati: ", C)

# 24-task: A, B, C sonlarini almashtirish (A -> C, B -> A, C -> B)
A = int(input("A ni kiriting: "))
B = int(input("B ni kiriting: "))
C = int(input("C ni kiriting: "))
A, B, C = C, A, B
print("A ning yangi qiymati: ", A)
print("B ning yangi qiymati: ", B)
print("C ning yangi qiymati: ", C)

# 25-task: y = 3x^6 - 6x^2 - 7 funksiyaning qiymati
x = int(input("x ni kiriting: "))
y = 3 * x**6 - 6 * x**2 - 7
print("Funksiya qiymati: ", y)

# 26-task: y = 4(x-3)^6 - 7(x-3)^3 + 2 funksiyaning qiymati
x = int(input("x ni kiriting: "))
y = 4 * (x - 3)**6 - 7 * (x - 3)**3 + 2
print("Funksiya qiymati: ", y)

# 31-masala: Farengeytdan Selsiyga o'tkazish
TF = float(input("Farengeytda temperaturani kiriting: "))
TC = (TF - 32) * 5 / 9
print("Temperatura Selsiyda: ", TC)

# 32-masala: Selsiydan Farengeytda o'tkazish
TC = float(input("Selsiyda temperaturani kiriting: "))
TF = (TC * 9 / 5) + 32
print("Temperatura Farengeytda: ", TF)

# 33-masala: X kg konfet narxi
A = float(input("1 kg konfetning narxi (so'm): "))
Y = float(input("Konfet miqdori Y kg: "))
cost_candy = A * Y
print("Konfetning narxi: ", cost_candy)

# 34-masala: Shokolad va konfet narxi
A = float(input("1 kg shokolad narxi (so'm): "))
B = float(input("1 kg konfet narxi (so'm): "))
X = float(input("Shokolad miqdori X kg: "))
Y = float(input("Konfet miqdori Y kg: "))
total_cost = A * X + B * Y
print("Shokolad va konfetning umumiy narxi: ", total_cost)

# 35-masala: Qayiqning daryo oqimi bo'yicha va oqimga qarshi yurishi
V = float(input("Qayiqning tezligi (km/soat): "))
U = float(input("Daryo oqimining tezligi (km/soat): "))
S = float(input("Yurgan masofa (km): "))

# Oqim bo'yicha vaqt
if V > U:
    T1 = S / (V + U)
    # Oqimga qarshi vaqt
    T2 = S / (V - U)
    print("Oqim bo'yicha yurish vaqti: ", T1)
    print("Oqimga qarshi yurish vaqti: ", T2)
else:
    print("Qayiqning tezligi daryo oqimidan katta bo'lishi kerak!")

# 36-masala: Ikkita avtomobilning qarama-qarshi yo'nalishdagi harakati
V1 = float(input("Birinchi avtomobilning tezligi (km/soat): "))
V2 = float(input("Ikkinchi avtomobilning tezligi (km/soat): "))
T = float(input("Ularning harakatlanish vaqti (soat): "))
S = (V1 + V2) * T
print("Ular orasidagi masofa: ", S)

# 37-masala: Ikkita avtomobilning bir-biriga qarab harakati
V1 = float(input("Birinchi avtomobilning tezligi (km/soat): "))
V2 = float(input("Ikkinchi avtomobilning tezligi (km/soat): "))
T = float(input("Ularning harakatlanish vaqti (soat): "))
S = abs((V1 - V2) * T)
print("Ular bir-biriga yaqinlashgandagi masofa: ", S)

# 38-masala: Chiziqli tenglamaning yechimi (Ax + B = 0)
A = float(input("Tenglamaning A koeffitsientini kiriting: "))
B = float(input("Tenglamaning B koeffitsientini kiriting: "))
if A != 0:
    x = -B / A
    print("Chiziqli tenglamaning yechimi: x =", x)
else:
    print("A qiymati 0 bo'la olmaydi!")

# 39-masala: Kvadrat tenglamaning diskriminanti va yechimlari
A = float(input("Kvadrat tenglamaning A koeffitsientini kiriting: "))
B = float(input("Kvadrat tenglamaning B koeffitsientini kiriting: "))
C = float(input("Kvadrat tenglamaning C koeffitsientini kiriting: "))

D = B**2 - 4 * A * C
if A != 0:
    if D > 0:
        x1 = (-B + D**0.5) / (2 * A)
        x2 = (-B - D**0.5) / (2 * A)
        print("Tenglamaning ikkita yechimi bor: x1 =", x1, ", x2 =", x2)
    elif D == 0:
        x = -B / (2 * A)
        print("Tenglamaning bitta yechimi bor: x =", x)
    else:
        print("Tenglamaning haqiqiy yechimi yo'q.")
else:
    print("A qiymati 0 bo'la olmaydi!")

# 40-masala: Chiziqli tenglamalar sistemasi (Cramer qoidasi)
A1 = float(input("Birinchi tenglama uchun A1 ni kiriting: "))
B1 = float(input("Birinchi tenglama uchun B1 ni kiriting: "))
C1 = float(input("Birinchi tenglama uchun C1 ni kiriting: "))
A2 = float(input("Ikkinchi tenglama uchun A2 ni kiriting: "))
B2 = float(input("Ikkinchi tenglama uchun B2 ni kiriting: "))
C2 = float(input("Ikkinchi tenglama uchun C2 ni kiriting: "))

D = A1 * B2 - A2 * B1
if D != 0:
    x = (C1 * B2 - C2 * B1) / D
    y = (A1 * C2 - A2 * C1) / D
    print("Tizimning yechimlari: x =", x, ", y =", y)
else:
    print("Tizimning yechimi yo'q (D = 0).")


