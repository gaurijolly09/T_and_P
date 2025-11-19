"""

            Name: GAURI JOLLY
            Enrollno : 0157AL231080
            Batch : MTF
            Batch Time : 10:30



                """

# Basic if else

# 1 WAP to check positive negative or zero
num = int(input("Enter number : "))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

# 2 WAP to check weather num is even or odd
num = int(input("Enter number : "))
if num % 2 == 0:
    print("Even")
else:
    print("odd")

# 3 WAP to check leap year
year = int(input("Enter the year : "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# 4 WAP to find greatst of two numbers
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if num1 > num2:
    print(num1, " is greater")
else:
    print(num2, " is greater")

# 5 WAP to check weather a person is eligible for voting
age = int(input("Enter age : "))
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# 6 WAP to check weather a character is vowel or consonent
vowel = ['a', 'e', 'i', 'o', 'u']
char = input("Enter character : ")
if char in vowel:
    print("vowel")
else:
    print("consonant")

# 7 WAP to check weather a number is divisible by 5
num = int(input("Enter a number : "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible")

# 8 check a number single , double or more than 2 digit
num = int(input("Enter number : "))
if num < 10:
    print("Single digit")
elif num >= 10 and num <= 99:
    print("Double digit")
else:
    print("More than 2 digit")

# 9 Student pass or fail
marks = float(input("Enter marks : "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# 10 WAP to check num is multiple of 3 and 7
num = int(input("Enter a number : "))
if num % 3 == 0 and num % 7 == 0:
    print("Yes it is a multiple")
else:
    print("Not a multiple of 3 and 7")

    # ladder if

# 1 WAP to find greatest of 3 numbers
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))
if num1 > num2:
    if num1 > num3:
        print(num1, " is greatest")
    else:
        print(num3, " is greatest")
else:
    if num2 > num3:
        print(num2, " is greatest")
    else:
        print(num3, " is greatest")

# 2 WAP to classify perso based on age
age = int(input("Enter age : "))
if age < 13:
    print("Child")
elif age <= 13 and age < 19:
    print("Teenager")
elif age >= 19 and age <= 59:
    print("Adult")
else:
    print("Senior")

# 3 WAP to assign grades
marks = int(input("Enter marks : "))
if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 75 and marks <= 89:
    print("B")
elif marks >= 50 and marks <= 74:
    print("C")
elif marks >= 35 and marks <= 49:
    print("D")
elif marks < 35:
    print("Fail")

# 4 classify the triangles
s1 = int(input("Enter first side : "))
s2 = int(input("Enter second side : "))
s3 = int(input("Enter third side : "))
if s1 == s2:
    if s1 == s3:
        print("Equilateral")
    else:
        print("Isosceles")
elif s1 == s3:
    if s1 == s2:
        print("Equilateral")
    else:
        print("Isosceles")
elif s2 == s3:
    if s2 == s1:
        print("Equilateral")
    else:
        print("Isosceles")
else:
    print("Scalene")

# 5 to check upercase lowercase digit or special character
ch = input("Enter character : ")
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

# 6 WAP to cal electricity bill
unit = int(input("Enter units : "))
total = 0
remain = unit
if remain <= 100:
    total = remain * 5

else:
    total += 100 * 5
    remain -= 100
    if remain > 0 and remain <= 100:
        total += remain * 7
    elif remain > 100:
        total += 100 * 7
        remain -= 100
        if remain > 0:
            total += remain * 10
print(total)

# 7 WAP to find largest of 4 numbers
n1 = int(input("Enter first num : "))
n2 = int(input("Enter second num : "))
n3 = int(input("Enter third num : "))
n4 = int(input("Enter fourth num : "))
if n1 > n2:
    if n1 > n3:
        if n1 > n4:
            print(n1, " is Greatest")
        else:
            print(n4, " is Greatest")
    else:
        if n3 > n4:
            print(n3, " is Greatest")
        else:
            print(n4, " is Greatest")
else:
    if n2 > n3:
        if n2 > n4:
            print(n2, " is Greatest")
        else:
            print(n4, " is Greatest")
    else:
        if n3 > n4:
            print(n3, " is Greatest")
        else:
            print(n4, " is Greatest")

# 8 WAP to check a century and leap year
year = int(input("Enter year : "))
if year % 100 == 0 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
    print("Century and Leap year")
else:
    print("NO")

# 9 WAP to classify BMI value
bmi = float(input("Enter bmi : "))
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal")
elif bmi >= 25 and bmi <= 29.9:
    print("Overweight")

# 10 WAP to find smallest number amog three
n1 = int(input("Enter num1 : "))
n2 = int(input("Enter num2 : "))
n3 = int(input("Enter num3 : "))
if n1 < n2:
    if n1 < n3:
        print(n1, " is smallest")
    else:
        print(n3, " is smallest")
else:
    if n2 < n3:
        print(n2, " is smallest")
    else:
        print(n3, " is smallest")

        # for loop

# 1 WAP to check armstrong number
##armstrong numbers
for i in range(100, 999):
    num_str = str(i)
    k = 0
    for num in num_str:
        f = ((int(num)) ** 3) + k
        k = f
    if f == i:
        print(f"this is armstrong {i}")

# 2 WAP to display first n prime number
n = int(input("Enter how many prime numbers to print: "))
count = 0  # Number of primes found
for num in range(2, 10000):  # A large enough range to find n primes
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
        count += 1
        if count == n:
            break

# 3 num divisible by 3 , sum of digits <=10
for i in range(1, 501):
    if i % 3 == 0:
        s = 0
        n = i
        while n > 0:
            s += n % 10
            n //= 10
        if s <= 10:
            print(i)

# 4 pyramid pattern
n = int(input("Enter n : "))
for i in range(0, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# 5 WAP to check panagram string
s = input("Enter string : ")
alphabets = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabets:
    if i not in s:
        print("Not panagram")
        break

else:
    print("Yes panagram")

# 6 WAP to print twin prime numbers
for num in range(2, 100):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    flag2 = True
    for j in range(2, num + 2):
        if (num + 2) % j == 0:
            flag = False
            break
    if flag and flag2 and num + 2 <= 100:
        print((num, num + 2))

# 7 WAP to check harshad number

num = int(input("Enter a number : "))
s_num = str(num)

s = 0
for i in s_num:
    digit = int(i)
    s += digit

if num % s == 0:
    print("Harshad number")
else:
    print("Not harshad")

# 8 PASCAL'S TRIANGLE
num = int(input("Enter the number : "))
l = []
for i in range(num):
    temp = []
    for j in range(i + 1):
        if j == 0 or j == i:
            temp.append(1)
        else:
            temp.append(l[i - 1][j - 1] + l[i - 1][j])
    l.append(temp)

for i in range(num):
    for j in range(num - i + 1):
        print(" ", end="")
    for k in range(i + 1):
        print(l[i][k], end=" ")
    print()

# 9 WAP to display sum of square series
n = int(input("Enter number : "))
s = 0
for i in range(1, n + 1):
    s += i ** 2
    print(i ** 2, " + ", end="")
print("\nTotal sum = ", s)

# 10 WAP to check for a strong number
num = int(input("Enter number : "))
s = 0
fact = 1
s_num = str(num)
for i in s_num:
    for j in range(1, int(i) + 1):
        fact *= j
    s += fact
    fact = 1
print(s)
if s == num:
    print("Strong number")
else:
    print("Not strong number")

    # While loop

# 11 WAP to reverse a number and check if it is a prime
num = int(input("Enter number : "))
new_num = 0
while (num > 0):
    digit = num % 10
    new_num = new_num * 10 + digit
    num //= 10

print(f"Reverse number : {new_num}")

if new_num < 2:
    print("Not prime")

else:
    flag = True
    for j in range(2, int(new_num ** 0.5) + 1):
        if new_num % j == 0:
            flag = False
            break

    if flag:
        print("Prime")
    else:
        print("Not prime")

# 12 continously take input number until all digits's sum is : sum>100
s = 0
while s <= 100:
    num = int(input("Enter number : "))
    while num > 0:
        digit = num % 10
        s += digit
        num //= 10

print("Sum crossed 100 , sum : ", s)

# 13 WAP to check a number is a Duck number
num = int(input("Enter a number : "))
s_num = str(num)
if s_num[0] == 0:
    print("Non Duck number")
else:
    i = 0
    while i < len(s_num):
        if s_num[i] == '0':
            print("Duck number")
            break
        else:
            i += 1
    else:
        print("Not a Duck number")

# 14 WAP to check  happy number
num = int(input("Enter a number : "))
visited = set()

while num != 1 and num not in visited:
    visited.add(num)
    s = 0
    while num > 0:
        digit = num % 10
        s += digit ** 2
        num //= 10
    num = s

if num == 1:
    print("Happy number")
else:
    print("Not a happy number")

# 15 WAP to find largest prime factor of given number
num = int(input("Enter number : "))
largest = 1
i = 2
while i <= num:
    if num % i == 0:
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            largest = i

    i += 1
print(largest, " is the largest prime factor")

# 16 WAP to repeatedly take input a string till we get palindrome string
s = input("Enter a string : ")
rev = s[::-1]
while s != rev:
    s = input("Enter a string : ")
    rev = s[::-1]

print("Palindrome string found : ", s)

# 17 WAP to find sum of digits till we get a single digit
num = int(input("Enter a number : "))
while num >= 10:
    s = 0
    while num > 0:
        digit = num % 10
        s += digit
        num //= 10
    num = s
print("Single value : ", num)

# 18 WAP to generate collartz sequence
num = int(input("Enter a number : "))
while num != 1:
    if num % 2 == 0:
        num = int(num / 2)
        print(num, end=" ")
    else:
        num = int((3 * num) + 1)
        print(num, end=" ")

# 19 WAP to check keprekar number
num = int(input("Enter a number : "))
if num == 1:
    print("Kaprekar number")

else:
    sq = num ** 2
    str_sq = str(sq)
    mid = len(str_sq) // 2

    l = str_sq[:mid]
    r = str_sq[mid:len(str_sq)]

    if int(l) + int(r) == num:
        print("Kaprekar number")
    else:
        print("Not a Kaprekar number")

# 20 ATM machine user stimulation

print("1. Check balance")
print("2. Deposit money")
print("3. Withdraw money")
print("4. Exit")

balance = int(input("Enter balance : "))

choice = input("Enter choice :")
while choice != '4':
    if choice == '1':
        print("Your balance : ", balance)

    elif choice == '2':
        depo = int(input("Enter amount to deposit : "))
        balance += depo
        print("Your balance : ", balance)

    elif choice == '3':
        amt = int(input("Enter amount to withdraw : "))
        if amt > balance:
            print("Not enough amount")
        else:
            balance -= amt
            print("Your balance : ", balance)
    else:
        print("Enter from 1 to 4 only")
    choice = input("Enter choice :")
else:
    print("Thank you ! ")









































