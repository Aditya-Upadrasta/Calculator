# Taking the input from the user!
num1 = input('Enter your 1st number: ')
num2 = input('Enter your 2nd number: ')

prob = input('What do you want to do??:  \n add\n subtract\n multiply\n divide\n : ')


sum = float(num1) + float(num2)
sub = float(num1) - float(num2)
product = float(num1) * float(num2)
div = float(num1) / float(num2)

if prob == 'add':
    print('The sum of {0} and {1} is {2}' .format(num1,num2,sum))    
    
elif prob == 'subtract':
    print('The subtraction of {0} and {1} is {2}' .format(num1,num2,sub))
    
elif prob == 'product':
    print('The product of {0} and {1} is {2}' .format(num1,num2,product))

else:
    print('The division of {0} and {1} is {2}' .format(num1,num2,div))
