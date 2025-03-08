#calculator
# How this calculator works
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
# let user choose mode of the calculator
print('Please choose the mode you want to use!')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
# get the input from user
while True:
    choice = input('Enter choice 1/ 2/ 3/ 4: ')
    if choice in ('1', '2', '3', '4'):
        num1 = float(input('Enter your first number: '))
        num2 = float(input('Enter your second number: '))
        if choice == '1':
            print('Result: ', add(num1, num2))
        elif choice == '2':
            print('Result: ', sub(num1, num2))
        elif choice == '3':
            print('Result: ', mul(num1, num2))
        elif choice == '4':
            print('Result: ', div(num1, num2))
    ask = input('Do you want to continue calculating? answer y/n: ')
    if ask == 'n' or 'no':
        break
    elif ask == 'y' or 'yes':
        continue
    
