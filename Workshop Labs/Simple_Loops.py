fruit = ['apples','oranges','bananas']
for item in fruit:
     print(f'The best fruit now is {item}')


numbers = [0,1,2,3,4,5,6,7,8,9,10]
for number in numbers:
     print(f'The next number is {number}')


#It would be tedious to write out a lot of numbers you want in a list, so we use the range() function:
for number in range(10):
     print(f'The next number is {number}')


#If you want to start at 1:
for number in range(1,10):
     print(f'The next number is {number}')


#If you want to increment the counter by more than the default value of 1, perhaps if you wanted only odd numbers or even numbers for example. 
#To do this you add a third parameter to the range() function as shown below:
for number in range(1,10,2):
     print(f'The next number is {number}')