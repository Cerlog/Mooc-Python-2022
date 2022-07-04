"""
Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

You may assume the letters will be either all uppercase, or all lowercase.

Some examples of expected behaviour:

Sample output
1st letter: x
2nd letter: c
3rd letter: p
The letter in the middle is p

Sample output
1st letter: C
2nd letter: B
3rd letter: A
The letter in the middle is B



"""

a = input("1st letter")
b = input("2nd letter")
c = input("3rd letter")

if a.isupper() == True and b.isupper() == True and c.isupper() == True:
    if a < b < c:
        print(f"1The letter in the middle is {b}")
    elif a < c < b:
        print(f"2The letter in the middle is {c}")
    elif a < c and b < c:
        print(f"3The letter in the middle is {a}")
    elif a < b and b > c:
        print(f"4The letter in the middle is {a}")
    elif a > b and b < c < a:
        print(f"5The letter in the middle is {c}")
    elif a > b > c:
        print(f"6The letter in the middle is {b}")

elif a.isupper() == False and b.isupper() == False and c.isupper() == False:
    if a < b < c:
        print(f"The letter in the middle is {b}")
    elif a < b and b > c:
        print(f"The letter in the middle is {c}")
    elif a < b and b > c:
        print(f"The letter in the middle is {a}")
    elif a < b and b > c:
        print(f"The letter in the middle is {a}")
    elif a > b and b < c < a:
        print(f"5The letter in the middle is {c}")
    elif a > b > c:
        print(f"The letter in the middle is {b}")
