# Input a number and find whether its prime or not

number = int(input('Enter a number: '))
i = 2

# checking if the number has any factors between i and the number itself
while i < number:
    if number % i == 0:
        flag = False  #since the number has a factor we assigned a false value and broke the loop
        break   #breaking the loop once any factor is found for the number
    else:
        flag = True   #flag = true until any factor is found for the number
    i += 1
if flag == True:
    print(number, 'is a prime number')
else:
    print(number, 'is not a prime number')
