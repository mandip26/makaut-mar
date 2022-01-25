# Input three numbers and find the largest and smallest number.

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
smallest = 0
largest = 0

#finding out the smallest among the three
if a < b and a < c:
    smallest = a
if b < a and b < c:
    smallest = b
if c < a and c < b:
    smallest = c

#finding out the largest among the three
if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c
    
# printing the smallest and largest numbers
print('Smallest among the three: ', smallest)
print('Largest among the three: ', largest)
