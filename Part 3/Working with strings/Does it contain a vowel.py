"""
Please write a program which asks the user to input a string.
The program then prints out different messages if the string contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below.

Sample output
Please type in a string: hello there
a not found
e found
o found

Sample output
Please type in a string: hiya
a found
e not found
o not found
"""
string = input("Please type in a string: ")
vowels = "aeo"
index = 0

while index < len(vowels):
    vowel = vowels[index]
    if vowel in string:
        print(vowel, "found")
    else:
        print(vowel, "not found")
    index +=1