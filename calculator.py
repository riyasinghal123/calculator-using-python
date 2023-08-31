from tkinter import *

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    
cal=Tk()
cal.title("Calculator")
operator=""

text_Input=StringVar()
txtdisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,bd=10,
                            bg='powder blue',fg='black',justify='right').grid(columnspan=4)
Addition=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",
            command=lambda:btnClick("+")).grid(row=3,column=3)
btn9=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=9,
            command=lambda:btnClick(9)).grid(row=3,column=2)
btn8=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=8,
            command=lambda:btnClick(8)).grid(row=3,column=1)
btn7=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=7,
            command=lambda:btnClick(7)).grid(row=3,column=0)

Substraction=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",
            command=lambda:btnClick("-")).grid(row=2,column=3)
btn6=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=6,
            command=lambda:btnClick(6)).grid(row=2,column=2)
btn5=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=5,
            command=lambda:btnClick(5)).grid(row=2,column=1)
btn4=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=4,
            command=lambda:btnClick(4)).grid(row=2,column=0)

Multiplication=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",
            command=lambda:btnClick("*")).grid(row=1,column=3)
btn3=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=3,
            command=lambda:btnClick(3)).grid(row=1,column=2)
btn2=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=2,
            command=lambda:btnClick(2)).grid(row=1,column=1)
btn1=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=1,
            command=lambda:btnClick(1)).grid(row=1,column=0)

Divison=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",
            command=lambda:btnClick("/")).grid(row=4,column=3)
Clear=Button(cal,padx=16,bd=8,fg="red",font=('arial',20,'bold'),text='C',
            command=lambda:btnClearDisplay()).grid(row=4,column=2)
btn0=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text=0,
            command=lambda:btnClick()).grid(row=4,column=1)
Equals=Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='=',
            command=lambda:btnEqualsInput()).grid(row=4,column=0)
