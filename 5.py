from tkinter import *
root = Tk()
root.geometry("268x288")
root.title("Калькулятор")
root.resizable(0,0)
numbers=['0','1','2','3','4','5','6','7','8','9', '.']
operators=['+','-','*','/']

def  button_clear():
    global f_num, math, math_op, sum
    input_field.delete(0, END)
def  button_click(number):
    global f_num, math, math_op,sum
    def button_add(f_num,math):
        sum = float(f_num) + math
        input_field.insert(END, sum)
    def button_subtract(f_num,math):
        sum = math - float(f_num)
        input_field.insert(END, sum)
    def button_multiply(f_num,math):
        sum = float(f_num) * math
        input_field.insert(END, sum)
    def button_divide(f_num,math):
        sum = math/float(f_num)
        input_field.insert(END, sum)
    def button_equal(math_op):
        if math_op == '+':
            button_add(f_num, math)
        if math_op == '-':
            button_subtract(f_num, math)
        if math_op == '/':
            button_divide(f_num, math)
        if math_op == '*':
            button_multiply(f_num, math)
    if number in numbers:
        f_num = f_num + number
        input_field.insert(END, number)
    if number in operators and f_num!='':
        math_op = number
        math = float(f_num)
        f_num = ''
        button_clear()
    if number=='-' and f_num=='' and math_op!='-':
        f_num ='-'
        input_field.insert(END, '-')
    if number=='-' and f_num=='' and math_op=='-':
        f_num =''
        input_field.insert(END, '-')
    if number=='=':
        button_clear()
        button_equal(math_op)
        f_num = ''
        math_op = ''
        math = 0

frame_input = Frame(root)
frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew")
input_field = Entry(frame_input, font='Arial 15 bold', width=24)
input_field.pack(fill=BOTH)
buttons = (('7', '8', '9', '/','4'),
           ('4', '5', '6', '*','4'),
           ('1', '2', '3', '-','4'),
           ('0', '.', '=', '+','4'))
f_num = ''
math = 0
math_op=''
sum = 0
button = Button(root, text='Очистить', command = lambda: button_clear())
button.grid(row=1, column=3, sticky="nsew")
for row in range(4):
    for col in range(4):
        Button(root, width=2, height=3, text=buttons[row][col],
               command=lambda row=row, col=col: button_click(buttons[row][col])).grid(row=row + 2, column=col, sticky="nsew", padx=1, pady=1)
root.mainloop()