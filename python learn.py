# import tkinter 
# window = tkinter.Tk()
# window.title('calculator')
# #
# font = ('Arial', 14, 'bold')
# Title_label = tkinter.Label(window, text='Please choose the mode you want to use!', font=font, bg='darkred', fg='white')
# Title_label.grid(row=0, column=0)
# #
# plus_button = tkinter.Button(window, text='+', font=font)
# plus_button.grid(row=1, column=0)
# #
# minus_button = tkinter.Button(window, text='-', font=font)
# minus_button.grid(row=1, column=1)
# window.mainloop()

#
# x = int(input('Input a number: '))
# def RE(x):
#     if (x==1):
#         result = x
#     else:
#         result = x * RE(x-1)
#     return result
# print(RE(x))
#
# class Add():
#     fir = 0
#     sen = 0
#     ans = 0
#     def __init__(self, f, s):
#         self.fir = f
#         self.sen = s
#     def cal(self):
#         self.ans=self.fir+self.sen
#     def dis(self):
#         print(self.ans)
# obj = Add(1000, 2000)
# obj.cal()
# obj.dis()

#
# class Hello:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __str__(self):
#         return 'Hello (%c %c)' % (self.a, self.b)
#     def __add__(self, other):
#         return Hello(self.a + other.a, self.b + other.b)
# v1 = Hello(2, 10)
# v2 = Hello(5, -2)
# print(v1 + v2)

# a = 1.5
# print('%s' % a)

#
# def main(number):
#     if number == 0:
#         return 0
#     elif number == 1:
#         return 1
#     elif number > 1:
#         return(main(number-2) + main(number-1))
# number = int(input('enter an number: '))
# for n in range(0, number):
#     print(main)

# x =20
# y =3.1
# print("sum =" and +x + y)

#
# print(sum([ord(d)-ord('a')for d in "abcd"]))
#
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
    