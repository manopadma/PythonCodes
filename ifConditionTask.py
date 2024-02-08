"""#3.check given number is +ve orr -ve
a =  float (input("Enter the Number"))
if a>0:
    print("The Given Value is +ve")
elif a<0:
    print("The Given Value is -ve")
else:
    print("The Given Value is Zero")"""


""" #4.check given number is divisible by 5 and 11

b = int (input("Enter the Number"))
if ((b%5 == 0) and (b%11 == 0)):
       print("The Given Number is Divisble by 5 and 11")
else:
      print("The Given number is not Divisble by 5 and 11")"""

"""#5.Check given number is odd or even

c = int (input("Enter the Number"))
if (c % 2==0):
    print("The Given Number is even Number")
else:
    print("The  Given Number is Odd Number")"""

"""#6.Check the leap and Non Leap Year

year = int(input("Enter The Year"))

if ((year % 4 == 0) and (year% 100 !=0) or (year % 400 == 0)):
    print("The given year is leap year")
else:
    print("The Given year is Non Leap Year")"""

"""#7.Check whether  a character is alphapet or not


alpha = str(input("Enter the Value"))

if (alpha.isalpha()):
    print("The Given Value is Alphapet")
else:
    print("The Given Value is not Alphapet")"""

#8.check vowel and consonants

ch = input("Enter the Characters")

if ((ch == 'a') or (ch == 'e') or (ch == 'i') or  (ch == 'o')or  (ch == 'u')or (ch == 'A') or (ch == 'E') or (ch == 'I') or  (ch == 'O')or  (ch == 'U')):
    print ("The Given Character is Vowel")
elif (ch):
    print("The Given Character is consonants ")
