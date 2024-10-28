#1

num = float(input("Enter a float number: "))
rounded_num = round(num, 2)
print(f"Rounded number: {rounded_num}")


#2
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

l= max([a,b,c])
m= min([a,b,c])

print("The largest :", l, "The lowest : ", m)


#3


km= float(input("Enter the distance in kilometers: "))

m= (km)*1000
cm=(km)*100000

print(m,"meters",cm,"centimeters")


#4

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

divison=a//b
remainder= a%b

print("divison :", divison, "remainder",remainder)

#5

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(celsius,"°C is equal to ",fahrenheit,"°F")


#6

number = int(input("Enter a number: "))
last_digit = number % 10
print("The last digit is ",last_digit)


#7 


number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number," is even")
else:
    print(number," is odd")




#8

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

a, b = b, a

print("Fiirst number is" ,a ,"Second one is", b)

print("__________________________________________________________________________________________________")


# String Data Type
#1

sentence = input("Enter a sentence: ")
sentence = sentence.title()
print(f"Capitalized sentence: {sentence}")


#2
vowels = "aeiouAEIOU"
string = input("Enter a string: ")

translation_table = str.maketrans('', '', vowels)
no_vowels = string.translate(translation_table)

print(f"String without vowels: {no_vowels}")


#3
string = input("Enter a string: ")
reversed_string = string[::-1]
print(f"Reversed string: {reversed_string}")




#4

string = input("Enter a string: ")
modified_string = string.replace(" ", "_")
print(f"No space string: {modified_string}")


#5
word=input('Entet a word like "Aziza"')

if word == word[::-1]:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")


#6
string = input("Enter a string: ")
modified_string = string.replace("a", "o")
print(modified_string)


#7


email = input("Enter email : ")
username = email.split('@')[0]
print(f"Username: {username}")

#8

string = input("Enter a string: ")
title_case_string = string.title()
print(title_case_string)

#9

a = input("Enter a string: ")
b = a[1:-1]
print(f"Original string (a): {a}")
print(f"Chanfed string (b): {b}")

#10
x = input("Enter a sentence: ")
word = input("Enter a word to check: ")

if word in x:
    print(f"'{word}' is present in the sentence.")
else:
    print(f"'{word}' is not present in the sentence.")


#11

x = input("Enter string: ")
char = input("Enter a character to find: ")

position = x.find(char)

if position != -1:
    print(f"The first occurrence of '{char}' is at index {position}.")
else:
    print(f"The character '{char}' is not found in the string")


#12
a = input("Enter a string: ")
b = a[-3:]
print(f"Last 3 characters: {b}")


#13

a = input("Enter a string: ")
n = int(input("Enter a number of times to repeat: "))
b = a * n
print(f"Repeated string: {b}")



#14
a = input("Enter a sentence: ")
for word in a.split():
    print(word)


#15
a = input("Enter a string: ")
b = a[1::2]
print(f"Letters at even positions: {b}")



#16
a = input("Enter a string: ")
print("Title: ",a )


#17
a = input("Enter a sentence: ")
b = ' '.join(a.split()[::-1])
print(f"Reversed: {b}")

#18


a = input("Enter the first string: ")
b = input("Enter the second string: ")

length_difference = abs(len(a) - len(b))

print(f"The difference between two strings is: {length_difference}")


print("__________________________________________________________________________________________________")


#Boolean Data Type 
#1

username = input("Enter username: ")
password = input("Enter password: ")

if bool(username) and bool(password):
    print("Both are provided.")
else:
    print("Either username or password is missing.")



#2

a = float(input("enter the first number: "))
b = float(input("enter the second number: "))

if a == b:
    print("equal")
else:
    print("not equal")



#3

a = int(input("Enter a number: "))

if a > 0:
    if a % 2 == 0:
        print(f"The number {a} is positive and even.")
    else:
        print(f"The number {a} is positive but not even.")
else:
    print(f"The number {a} is not positive.")




#4

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a != b and b != c and a != c:
    print("All numbers are different")
else:
    print("Two are same")


#5

a = input("Enter the first string: ")
b = input("Enter the second string: ")

if len(a) == len(b):
    print("same length")
else:
    print("different lengths")

#6
a = int(input("Enter a number: "))

if a % 3 == 0 and a % 5 == 0:
    print(a,"is divisible by 3 and 5")
else:
    print(a,"is not divisible by 3 and 5")

#7


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a + b > 50:
    print("bigger thn 50 ")
else:
    print("less than 50")



#8

a = float(input("Enter a number: "))

if 10 <= a <= 20:
    print("between 10 and 20")
else:
    print("not between 10 and 20")