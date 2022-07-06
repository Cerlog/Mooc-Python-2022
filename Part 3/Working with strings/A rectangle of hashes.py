"""Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

Sample output
Width: 10
Height: 3
##########
##########
##########"""
w = int(input("Width"))
h = int(input("Height"))
row = "#" * w
while h > 0:
    print(row)
    h -=1
