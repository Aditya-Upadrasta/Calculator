# Taking the input from the user!
num1 = input('Enter your 1st number: ')
num2 = input('Enter your 2nd number: ')

prob = input('What do you want to do??: (+)\t (-)\t (*)\t (/)\n \t  \t \t \t \t \t:-  ')


sum = float(num1) + float(num2)
sub = float(num1) - float(num2)
div = float(num1) / float(num2)
multiply = float(num1) * float(num2)

if prob == '+':
    print('The sum of {0} and {1} is {2}' .format(num1,num2,sum))    
    
elif prob == '-':
    print('The subtraction of {0} and {1} is {2}' .format(num1,num2,sub))
    
elif prob == '*':
    print('The multiply of {0} and {1} is {2}' .format(num1,num2,multiply))

else:
    print('The division of {0} and {1} is {2}' .format(num1,num2,div))
