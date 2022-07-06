"""Please write a program which asks the user to type in a limit.
The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...)
until the sum is at least equal to the limit set by the user. The program should function as follows:

Sample output
Limit: 2
3

Sample output
Limit: 10
10

Sample output
Limit: 18
21

If you have trouble understanding how the desired output is calculated,
the sample outputs in the next exercise may help. You may assume the number
typed in by the user is always equal to 2 or higher."""

limit = int(input("Limit:"))

base = 0
num = 1

# Each time base is less than limit, add base by num (At the first iteration num is 1), and add num by 1
while base < limit:
    base += num
    num += 1
print(base)
