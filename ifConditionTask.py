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

"""#8.check vowel and consonants

ch = input("Enter the Characters")

if ((ch == 'a') or (ch == 'e') or (ch == 'i') or  (ch == 'o')or  (ch == 'u')or (ch == 'A') or (ch == 'E') or (ch == 'I') or  (ch == 'O')or  (ch == 'U')):
    print ("The Given Character is Vowel")
elif (ch):
    print("The Given Character is consonants ")
"""

"""#9. Check the Given Textis upper or lower case

text = input("Enter the text")

if (text.isupper()):
    print("The Given Text is UpperCase")
elif(text.islower()):
    print("The Given Text is Lower Case")
else:
    print("Invalid Text ")"""

"""# 10.Print day name of Week

week = int(input("Enterr the Week Number"))

if (week == 1):
    print("Monday")
elif(week ==2):
    print("Tuesday")
elif(week ==3):
    print("Wednesday")
elif(week ==4):
    print("Thursday")
elif(week ==5):
    print("Friday")
elif(week ==6):
    print("Saturday")
elif(week ==7):
    print("Sunday")
else:
    print("Invalid Input")
"""

"""# 11 Find the Number days in Month
month = int(input("Enter the month Number(1-12)"))
if (month == 1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month == 12):
    print("This month Contain 31 days")
elif(month == 2):
    print("This month contain 28 /29 days")
elif(month == 4 or month == 6 or month == 9 or month == 11):
    print("This month contain 30 days")
else:
    print("Invalid Input")"""

"""# 12.countt total number of notes in given amount

amt =int(input("Enter the amount"))
fiveHundred = 0
hundredRupe =0
fiftyRupee = 0
twentyRupee = 0
tenRupee =  0
fiveRupee = 0
twoRupee = 0
oneRupeeCoin =0

if(amt>=500):
    fiveHundred = amt/500
    amt -= fiveHundred *500
    print(f"This Amount contain{amt} Note")
if(amt>=100):
    hundredRupe =amt/100
    amt-= hundredRupe*100
if(amt>=50):
    fiftyRupee =amt/50
    amt-= fiftyRupee*50
if(amt>=20):
    twentyRupee =amt/20
    amt-= twentyRupee*20
if(amt>=10):
    tenRupee =amt/10
    amt-= tenRupee*10
if(amt>=5):
    fiveRupee =amt/5
    amt-= fiveRupee*5
if(amt>=2):
    twoRupee=amt/2
    amt-= twoRupee*2
if(amt>=1):
    oneRupeeCoin =amt/1
    amt-= hundredRupe*1"""

"""# 13.Whether triangle is valid or not using angles

angle1 = int(input("Enter the 1st angle"))
angle2 = int(input("Enter the 2nd angle"))
angle3 = int(input("Enter the 3rd angle"))

sum = angle1 + angle2 + angle3
if (sum == 180  and angle1> 0 and angle2 > 0 and angle3>0):
    print("This Triangle is Valid")
else:
    print("This Triangle is invalid")"""

"""#14.whether triangle is valid or not using side of triangle

side1 = int(input("Enter the Side 1 for triangle"))
side2 = int(input("Enter the Side 2 for triangle"))
side3 = int(input("Enter the Side 3 for triangle"))

if((side1+side2)> side3):
    if((side2+side3)>side1):
        if ((side1+side3)>side2):
            print("This Triangle is Valid")

else:
    print("This Triangle is invalid")"""

"""#15. check the given triangle is equalateral or scalene or isosceles 

triSide1 = int(input("Enter the side 1"))
triSide2 = int(input("Enter the side 1"))
triSide3 = int(input("Enter the side 1"))

if(triSide1 == triSide2 and triSide2 == triSide3 and triSide1 == triSide3):
    print("This Triangle is Equalateral ")
elif(triSide1 == triSide2 or triSide2 == triSide3 or triSide1 == triSide3):
    print("This triangle is isosceles ")
else:
    print("This is Scalene Triangle")"""