

# Revision


# print('Syed Muhammad Umer')
#
# a = input('Enter your name = ')
#
# print(a)



# a = int(input('Enter number 1 = '))
# b = int(input('Enter number 2 = '))
#
# print('Addition = ',a+b)
# print('Subtraction = ',a-b)
# print('Multiplication = ',a*b)
# print('Division = ',a/b)
# print('Square = ',a**2)






# Conditions

# a = 11
# b = 13
# c = 10
#
# if a>b:
#     print('a is greater than b')
# elif a>c:
#     print('a is greater than c')
# else:
#     print('b is greater than a')



# Loop

# num = 5
# for i in range(1,11):
#     print(num,'x',i,'=',num*i)


# a = 6
#
# while a>=1:
#     print(a)
#     a = a-1





# Functions

# def add(num1, num2):
#     sum = num1+num2
#     print(sum)
#
#
#
# add(12,23)
# add(7,13)
# add(2,5)
# add(10,8)
# add(1,3)
# add(2,2)



# Lambda Function


# add = lambda x,y: x+y
#
# print(add(5,3))




# Libraries

# GUI    Tkinter   and   PyQt5

# Tkinter

# from tkinter import *
#
# root = Tk()
#
#
# # Function
# def myclick():
#     hello = 'Hello ' + e.get()
#     my_label = Label(root,text=hello)
#     my_label.pack()
#
# # Add a label in our program
# my_label = Label(root,text='Hello! Please Write your name')
# # To show label on the screen
# my_label.pack()
#
# # Input Field
# e = Entry(root, width=100)
# e.pack()
#
#
# # Add button
# my_button = Button(root,text='Click me',command=myclick,padx=20,pady=20,fg='Red',bg='Yellow')
# # To show button on the screen
# my_button.pack()
#
# root.mainloop()







# GUI based Calculator

from tkinter import *

root = Tk()
root.title('Calculator')

# Add Entry Box

my_entry = Entry(root,width=50,borderwidth=10)
# my_entry.pack()
my_entry.grid(row=0,column=1,columnspan=3,padx=10,pady=20)

def button_click(number):
    current = my_entry.get()
    my_entry.delete(0,END)
    my_entry.insert(0,current+str(number))

def button_add():
    first_number = my_entry.get()
    global f_num
    global math
    math = 'Addition'
    f_num = int(first_number)
    my_entry.delete(0,END)

def button_sub():
    first_number = my_entry.get()
    global f_num
    global math
    math = 'Subtraction'
    f_num = int(first_number)
    my_entry.delete(0,END)

def button_mul():
    first_number = my_entry.get()
    global f_num
    global math
    math = 'Multiplication'
    f_num = int(first_number)
    my_entry.delete(0,END)

def button_div():
    first_number = my_entry.get()
    global f_num
    global math
    math = 'Division'
    f_num = int(first_number)
    my_entry.delete(0,END)

def button_equal():
    second_number = my_entry.get()
    s_num = int(second_number)
    my_entry.delete(0,END)
    if math == 'Addition':
        my_entry.insert(0,f_num+s_num)
    if math == 'Subtraction':
        my_entry.insert(0,f_num-s_num)
    if math == 'Multiplication':
        my_entry.insert(0,f_num*s_num)
    if math == 'Division':
        my_entry.insert(0,f_num/s_num)


# Create Buttons
my_button1 = Button(root,text='1',padx=40,pady=30,command=lambda: button_click(1))
my_button2 = Button(root,text='2',padx=40,pady=30,command=lambda: button_click(2))
my_button3 = Button(root,text='3',padx=40,pady=30,command=lambda: button_click(3))
my_button4 = Button(root,text='4',padx=40,pady=30,command=lambda: button_click(4))
my_button5 = Button(root,text='5',padx=40,pady=30,command=lambda: button_click(5))
my_button6 = Button(root,text='6',padx=40,pady=30,command=lambda: button_click(6))
my_button7 = Button(root,text='7',padx=40,pady=30,command=lambda: button_click(7))
my_button8 = Button(root,text='8',padx=40,pady=30,command=lambda: button_click(8))
my_button9 = Button(root,text='9',padx=40,pady=30,command=lambda: button_click(9))
my_button0 = Button(root,text='0',padx=40,pady=30,command=lambda: button_click(0))
my_button_add = Button(root,text='+',padx=40,pady=30,command=button_add)
my_button_Sub = Button(root,text='-',padx=40,pady=30,command=button_sub)
my_button_Mul = Button(root,text='*',padx=40,pady=30,command=button_mul)
my_button_Div = Button(root,text='/',padx=40,pady=30,command=button_div)
my_button_Clear = Button(root,text='C',padx=40,pady=30,command=lambda: my_entry.delete(0,END))
my_button_Equal = Button(root,text='=',padx=40,pady=30,command=button_equal)


# Button Positioning
my_button7.grid(row=1,column=0)
my_button8.grid(row=1,column=1)
my_button9.grid(row=1,column=2)

my_button4.grid(row=2,column=0)
my_button5.grid(row=2,column=1)
my_button6.grid(row=2,column=2)

my_button1.grid(row=3,column=0)
my_button2.grid(row=3,column=1)
my_button3.grid(row=3,column=2)

my_button0.grid(row=4,column=1)

my_button_add.grid(row=1,column=3)
my_button_Sub.grid(row=2,column=3)
my_button_Mul.grid(row=3,column=3)
my_button_Div.grid(row=4,column=3)

my_button_Clear.grid(row=4,column=0)
my_button_Equal.grid(row=4,column=2)




root.mainloop()





















