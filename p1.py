from tkinter import *
from tkinter import messagebox
import math

d={'a':"ln",'b':"log",'c':"sin",'d':"cos",'e':"tan",'f':"cosec",'g':"sec",'h':"cot"}
g={j:i for i,j in d.items()}
print(g)
Loo = ['a','b','c','d','e','f','g','h','^','!','/','*','+','-']

class Window(Frame):
    
                       
    def __init__(self, master=None):
        
        self.strin, self.LastEntries = '',[]
    
        Frame.__init__(self, master)
        self.master = master
# Creating result text field
        self.resultField = Text(master, bg="#FFFFFF", fg="#000000", height=2, width=34)
        self.resultField.insert(INSERT, "0")
        self.resultField.grid(row=0, columnspan=6)
            
            
        h,w = 3,7
        mybd=4
# Creating number and operation buttons
        b1 = Button(master, text="1", bd=mybd, bg="blue", fg="white", height=h, width=w, command=lambda: [self.notice(1),self.s('1')])
        b2 = Button(master, text="2", bd=mybd, bg="blue", fg="white", height=h, width=w, command=lambda: [self.notice(2),self.s('2')])
        b3 = Button(master, text="3", bd=mybd, bg="blue", fg="white", height=h, width=w, command=lambda: [self.notice(3),self.s('3')])
        bPlus = Button(master, text="+", bd=mybd, bg="black", fg="white", height=h, width=w, command=lambda: [self.notice("+"),self.s('+')])
        b4 = Button(master, text="4", bd=mybd, bg="blue", fg="white", height=h, width=w, command=lambda: [self.notice(4),self.s('4')])
        b5 = Button(master, text="5", bd=mybd, bg="blue", fg="white", height=h, width=w, command=lambda: [self.notice(5),self.s('5')])
        b6 = Button(master, text="6", bd=mybd, bg="blue", fg="white", height=h, width=w, command=lambda: [self.notice(6),self.s('6')])
        bMinus = Button(master, text="-", bd=mybd, bg="black", fg="white", height=h, width=w, command=lambda: [self.notice("-"),self.s('-')])
        b7 = Button(master, text="7", bd=mybd, bg="blue", fg="white", height=h, width=w, command=lambda: [self.notice(7),self.s('7')])
        b8 = Button(master, text="8", bd=mybd, bg="blue", fg="white", height=h, width=w, command=lambda: [self.notice(8),self.s('8')])
        b9 = Button(master, text="9", bd=mybd, bg="blue", fg="white", height=h, width=w, command=lambda: [self.notice(9),self.s('9')])
        bMultip = Button(master, text="*", bd=mybd, bg="black", fg="white", height=h, width=w, command=lambda: [self.notice("*"),self.s('*')])
        b0 = Button(master, text="0", bd=mybd, bg="blue", fg="white", height=h, width=w, command=lambda: [self.notice(0),self.s('0')])
        bLeft = Button(master, text="(", bd=mybd, bg="black", fg="white", height=h, width=w, command=lambda: [self.notice("("),self.s('(')])
        bRight = Button(master, text=")", bd=mybd, bg="black", fg="white", height=h, width=w, command=lambda: [self.notice(")"),self.s(')')])
        bDivide = Button(master, text="/", bd=mybd, bg="black", fg="white", height=h, width=w, command=lambda: [self.notice("/"),self.s('/')])
        bdot=Button(master, text=".", bd=mybd, bg="black", fg="white", height=h, width=w, command=lambda: [self.notice("."),self.s('.')])
        bfac=Button(master, text="!", bd=mybd, bg="black", fg="white", height=h, width=w, command=lambda: [self.notice("!"),self.s('!')])
        bln=Button(master, text="ln(", bd=mybd, bg="black", fg="white", height=h, width=w, command=lambda: [self.notice("ln("),self.s('a(')])
        blog=Button(master, text="log(", bd=mybd, bg="black", fg="white", height=h, width=w, command=lambda: [self.notice("log("),self.s('b(')])
        bsin=Button(master, text="sin(", bd=mybd, bg="turquoise4", fg="white", height=h, width=w, command=lambda: [self.notice("sin("),self.s('c(')])
        bcos=Button(master, text="cos(", bd=mybd, bg="turquoise4", fg="white", height=h, width=w, command=lambda: [self.notice("cos("),self.s('d(')])
        btan=Button(master, text="tan(", bd=mybd, bg="turquoise4", fg="white", height=h, width=w, command=lambda: [self.notice("tan("),self.s('e(')])
        bcosec=Button(master, text="cosec(", bd=mybd, bg="turquoise4", fg="white", height=h, width=w, command=lambda: [self.notice("cosec("),self.s('f(')])
        bsec=Button(master, text="sec(", bd=mybd, bg="turquoise4", fg="white", height=h, width=w, command=lambda: [self.notice("sec("),self.s('g(')])
        bcot=Button(master, text="cot(", bd=mybd, bg="turquoise4", fg="white", height=h, width=w, command=lambda: [self.notice("cot("),self.s('h(')])
        bpow=Button(master, text="^", bd=mybd, bg="black", fg="white", height=h, width=w, command=lambda: [self.notice("^"),self.s('^')])
        bBkSp=Button(master, text="<-", bd=mybd, bg="red", fg="white", height=h, width=w, command=lambda: self.BkS())
# Aligning number and operation buttons
        b1.grid(row=1, column=1)
        b2.grid(row=1, column=2)
        b3.grid(row=1, column=3)
        bPlus.grid(row=6, column=4)
        b4.grid(row=2, column=1)
        b5.grid(row=2, column=2)
        b6.grid(row=2, column=3)
        bMinus.grid(row=5, column=4)
        b7.grid(row=3, column=1)
        b8.grid(row=3, column=2)
        b9.grid(row=3, column=3)
        bMultip.grid(row=3, column=4)
        b0.grid(row=4, column=2)
        bLeft.grid(row=4, column=1)
        bRight.grid(row=4, column=3)
        bDivide.grid(row=4, column=4)
        bfac.grid(row=5,column=2,columnspan=1)
        bdot.grid(row=5,column=3,columnspan=1)
        bpow.grid(row=6,column=3,columnspan=1)
        bBkSp.grid(row=1,column=4)
        bln.grid(row=5,column=1)
        blog.grid(row=6,column=1)
        bsin.grid(row=1,column=0)
        bcos.grid(row=2,column=0)
        btan.grid(row=3,column=0)
        bcosec.grid(row=4,column=0)
        bsec.grid(row=5,column=0)
        bcot.grid(row=6,column=0)
                
# Creating and aligning calculation buttons
        bCalculate = Button(master, text="=", bd=mybd, bg="green", fg="white", height=h, width=w, command=self.displayRes)              
        bClear = Button(master, text="Clear", bd=mybd, bg="red", fg="white", height=h, width=w, command=self.clear)
        bCalculate.grid(row=6, column=2, columnspan=1)
        bClear.grid(row=2, column=4)
                
    def notice(self, num):
        self.LastEntries.append(num)
        if self.resultField.get("0.0", END) == "0\n":
            self.resultField.delete("0.0", END)
        self.resultField.insert(INSERT, str(num))
               
    def clear(self):
        self.resultField.delete("0.0", END)
        self.resultField.insert(INSERT, "0")
        self.strin=""
        el=[]

                
    def displayRes(self):
        
        res = self.evaluate(self.Dig_Grouper(list(self.strin))) #self.resultField.get("0.0",END)[:-1]
        self.resultField.delete("0.0", END)
        self.resultField.insert(INSERT, str(res))
                
    def s(self, st):  self.strin+=st
    
    def BkS(self):
        print(self.LastEntries,self.strin)
        self.strin=self.strin[0:self.strin.rindex(str(self.LastEntries[-1]))]
        
        self.resultField.delete("0.0", END)
        self.resultField.insert(INSERT, str(self.strin))

    def Dig_Grouper(self, el):
 
        for i in range(len(el)) :
            if i>=len(el) : break
            if ord(el[i]) in range(48,58) :
                j=i+1
                while(j<len(el) and (el[j].isdigit() or el[j]=='.' )) :
                    el[i]+=el[j]
                    j+=1
        
                del el[i+1:j]
    
                el[i]=float(el[i])    
        return el

    def evaluate(self, el) : 

        for i in range(len(el)) : 
            if i>=len(el) : break
            if el[i]=='(':
                k,op,clo = i,1,0
                #try:
                while(op!=clo):
                    k+=1
                    if el[k]==')': clo+=1
                    if el[k]=='(': op+=1
            
        
         
                el[i]=self.evaluate(el[i+1:k])
      
                del el[i+1:k+1]
      
        for j in range(len(Loo)) :
    
            for i in range(len(el)) : 
      
                if i>=len(el) : break
      
                if el[i] == Loo[j] :
      
                    if el[i]=='a':   el[i]   = float(math.log(el[i+1]))
                    if el[i]=='b':   el[i]   = float(math.log(el[i+1],10))
                    if el[i]=='c':   el[i]   = float(math.sin(el[i+1]))
                    if el[i]=='d':   el[i]   = float(math.cos(el[i+1]))
                    if el[i]=='e':   el[i]   = float(math.tan(el[i+1]))
                    if el[i]=='f':   el[i]   = float(1/math.sin(el[i+1]))
                    if el[i]=='g':   el[i]   = float(1/math.cos(el[i+1]))
                    if el[i]=='h':   el[i]   = float(1/math.tan(el[i+1]))
                    if el[i]=='^':   el[i-1] = float(el[i-1] ** round(el[i+1],20))
                    if el[i]=='!':   el[i-1] = float(math.factorial(int(el[i-1]+0.5)))
                    if el[i]=='/':
                        try: el[i-1] = float(el[i-1] / el[i+1])
                        except: return "Division Error"
                    if el[i]=='*':  el[i-1] = float(el[i-1] * el[i+1])
                    if el[i]=='+':  el[i-1] = float(el[i-1] + el[i+1])
                    if el[i]=='-':  el[i-1] = float(el[i-1] - el[i+1])        
                    #if el[i]==14:  el[i-1] = float(el[i-1] - el[i+1])
                    
                    if j in range(8,14): del el[i:i+2]
                    elif j==9: del[i]
                    else: del el[i+1]
                    i-=1
                    print(i)
               
        return el[0]  


root = Tk()
app = Window(root)
root.wm_title("CALCULATOR")
root.mainloop()  
