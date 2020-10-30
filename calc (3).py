from tkinter import *
import tkinter.messagebox,math

total=0
current=''
ip_val=True
check_sum=False
op1=''
result=False
        
wn=Tk()
wn.title("Calculator")
wn.configure(background="green2")
wn.resizable(width=False,height=False)
wn.geometry("480x568")
calc=Frame(wn)
calc.grid(row=0,column=0)
    
def numberEnter(num):
        global result,ip_val,current
        result=False
        first_num=txtDisplay.get()
        second_num=str(num)
        if ip_val:
            current=second_num
            ip_val=False
        else:
            if second_num=='.':
                if second_num in first_num:
                    return
            current=first_num + second_num
        display(current)
    
def sum_of_total():
        global result,check_sum,current
        result=True
        current=float(current)
        print(current)
        if check_sum:
            valid_function()
        else:
            total=float(txtDisplay.get())
    
def valid_function():
        global check_sum,ip_val,op1,total
        if op1=='add':
            total += current
        elif op1=='sub':
            total -= current
        elif op1=='mul':
            total *= current
        elif op1=='div':
            total /= current
        elif op1=='^':
            total=math.pow(total,current) 
        ip_val=True
        check_sum=False
        display(total)

def operation(op):
        global check_sum,ip_val,total,current,result,op1
        current=float(current)
        if check_sum:
            valid_function()
        elif not result:
            total=current
            ip_val=True
        check_sum=True
        op1=op
        result=False

def display(value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)
    
def clear_entry():
        global current,result,ip_val
        result=False
        current='0'
        display(0)
        ip_val=True
    
def clear_all():
        global total
        clear_entry()
        total=0

def pi():
        global current,result
        result=False
        current=math.pi
        display(current)
    
def e():
        global current,result
        result=False
        current=math.e
        display(current)

def PM():
        global current,result
        result=False
        current=-(float(txtDisplay.get()))
        display(current)
    
def sq_rt():
        global current,result
        result=False
        current=math.sqrt(float(txtDisplay.get()))
        display(current)
    
def ln():
        global current,result
        result=False
        current=math.log(float(txtDisplay.get()))
        display(current)
    
def log():
        global current,result
        result=False
        current=math.log10(float(txtDisplay.get()))
        display(current)
    
def log2():
        global current,result
        result=False
        current=math.log2(float(txtDisplay.get()))
        display(current)
    
def exp():
        global current,result
        result=False
        current=math.exp(math.radians(float(txtDisplay.get())))
        display(current)
    
def sin():
        global current,result
        result=False
        current=math.sin(math.radians(float(txtDisplay.get())))
        display(current)
    
def cos():
        global current,result
        result=False
        current=math.cos(math.radians(float(txtDisplay.get())))
        display(current)
    
def tan():
        global current,result
        result=False
        current=math.tan(math.radians(float(txtDisplay.get())))
        display(current)
    
def sinh():
        global current,result
        result=False
        current=math.sinh(math.radians(float(txtDisplay.get())))
        display(current)
    
def cosh():
        global current,result
        result=False
        current=math.cosh(math.radians(float(txtDisplay.get())))
        display(current)
    
def tanh():
        global current,result
        result=False
        current=math.tanh(math.radians(float(txtDisplay.get())))
        display(current)
    
def degrees():
        global current,result
        result=False
        current=math.degrees(float(txtDisplay.get()))
        display(current)
    
def radians():
        global current,result
        result=False
        current=math.radians(float(txtDisplay.get()))
        display(current)

def Exit():
    if tkinter.messagebox.askyesno("Calculator","Confirm if you want to quit") >0 :
        wn.destroy()
        return

def Sci():
    wn.resizable(width=False,height=False)
    wn.geometry("835x568")

def Std():
    wn.resizable(width=False,height=False)
    wn.geometry("480x568")

txtDisplay=Entry(calc,font=('arial',20,'bold'),bd=30,bg='gray60',width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,'0')

numpad ='789456123'
i=0
btn=[]

for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=6,height=2,font=('arial',20,'bold'),bd=4,text=numpad[i],bg="orange"))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]['command']=lambda x=numpad[i]:numberEnter(x)
        i+=1

#Standard Calculator
Button(calc,text=chr(67),width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command=clear_entry).grid(row=1,column=0,pady=1)
Button(calc,text=chr(67)+chr(69),width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command=clear_all).grid(row=1,column=1,pady=1)
Button(calc,text=u'\u221A',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command=sq_rt).grid(row=1,column=2,pady=1)
Button(calc,text='+',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command=lambda: operation('add')).grid(row=1,column=3,pady=1)

Button(calc,text='-',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command=lambda: operation('sub')).grid(row=2,column=3,pady=1)
Button(calc,text='*',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command=lambda: operation('mul')).grid(row=3,column=3,pady=1)
Button(calc,text='/',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command=lambda: operation('div')).grid(row=4,column=3,pady=1)
Button(calc,text='=',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command=sum_of_total).grid(row=5,column=3,pady=1)

Button(calc,text='.',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command=lambda: numberEnter('.')).grid(row=5,column=0,pady=1)
Button(calc,text='0',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="orange",command=lambda: numberEnter(0)).grid(row=5,column=1,pady=1)
Button(calc,text=chr(177),width=6,height=2,font=('arial',20,'bold'),bd=4,bg="green",command=PM).grid(row=5,column=2,pady=1)

#Scientific
Button(calc,text=u'\u03C0',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=pi).grid(row=1,column=4,pady=1)
Button(calc,text='sin',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=sin).grid(row=2,column=4,pady=1)
Button(calc,text='cos',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=cos).grid(row=2,column=5,pady=1)
Button(calc,text='tan',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=tan).grid(row=2,column=6,pady=1)

Button(calc,text='log',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=log).grid(row=4,column=4,pady=1)
Button(calc,text='sinh',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=sinh).grid(row=3,column=4,pady=1)
Button(calc,text='cosh',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=cosh).grid(row=3,column=5,pady=1)
Button(calc,text='tanh',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=tanh).grid(row=3,column=6,pady=1)

Button(calc,text='ln',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=ln).grid(row=4,column=5,pady=1)
Button(calc,text='exp',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=exp).grid(row=1,column=6,pady=1)
Button(calc,text='^',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=lambda: operation('^')).grid(row=5,column=6,pady=1)
Button(calc,text='e',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=e).grid(row=1,column=5,pady=1)

Button(calc,text='log2',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=log2).grid(row=4,column=6,pady=1)
Button(calc,text='deg',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=degrees).grid(row=5,column=4,pady=1)
Button(calc,text='rad',width=6,height=2,font=('arial',20,'bold'),bd=4,bg="gold",command=radians).grid(row=5,column=5,pady=1)

#Display control
menubar=Menu(calc)
file_menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Standard",command=Std)
file_menu.add_command(label="Scientific",command=Sci)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=Exit)
wn.config(menu=menubar)
wn.mainloop()