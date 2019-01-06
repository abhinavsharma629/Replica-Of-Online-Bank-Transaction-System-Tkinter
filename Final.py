from tkinter import *
import tkinter.messagebox
import sqlite3
import smtplib

root=Tk()
root.title('SBI')

global named,name66
global col
global img19
col=0
img10=PhotoImage(file='maximax.gif')
img=PhotoImage(file='SBI.gif')


def sendmail(c5):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('abhinavsharma629@gmail.com','*****************************')
    msg="SUCCESSFULL TRANSACTION FROM YOUR ACCOUNT"
    server.sendmail('abhinavsharma629@gmail.com',c5,msg)
    server.quit()



def fun():
    frame=Toplevel(width=1000,height=1000)
    frame.config(background='light blue')
    head=Label(frame, text="FILL YOUR NECESSARY DETAILS",bd=5,font="Times 28",fg="white",bg="black").place(x=260,y=1)
    head1=Label(frame,image=img10).place(x=700,y=200)
    name=StringVar()
    passw=StringVar()
    cv=IntVar()
    ac=IntVar()
    address=StringVar()
    email=StringVar()
    phone=IntVar()
    phone1=IntVar()
    branch=StringVar()
    country=StringVar()
    gender=IntVar()

    #connecting DATABASE
    def database():
        global name3
        name3= name.get()
        global pas1
        pas1= passw.get()
        cvv=cv.get()
        ac1=ac.get()
        add = address.get()
        email1 = email.get()
        phone3 = phone.get()
        phone4 = phone1.get()
        branch1 = branch.get()
        coun = country.get()
        gend = gender.get()
        amou=10000
        conn = sqlite3.connect('ATM.db')
        with conn:
            cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Details1(Name TEXT,Password TEXT,Pin Number CANDIDATE KEY,Account_Num Number PRIMARY KEY,Address TEXT,Email TEXT,PhoneNumber TEXT,AlternatePhoneNumber TEXT,Branch TEXT,Country TEXT,Gender TEXT,Amount Number)')
        cursor.execute('INSERT INTO Details1(Name,Password,Pin,Account_Num,Address,Email,PhoneNumber,AlternatePhoneNumber,Branch,Country,Gender,Amount) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(name3,pas1,cvv,ac1,add,email1,phone3,phone4,branch1,coun,gend,amou))
        cursor.execute('CREATE TABLE IF NOT EXISTS Details3(Account_Num Number,Amount Number)')
        conn.commit()



    #CODE

    name54=Label(frame,text="Name",font="italic",bd=2).place(x=300,y=100)
    name14=Entry(frame,bd=4,textvar=name,font=17).place(x=502,y=102)
    pasw23=Label(frame,text="Password",font=("italic"),bd=2).place(x=300,y=150)
    pas2=Entry(frame,bd=4,textvar=passw,show='•',font=17).place(x=502,y=152)
    add=Label(frame,text="Address",font=("italic"),bd=2).place(x=300,y=200)
    add1=Entry(frame,bd=4,textvar=address,font=17).place(x=502,y=202)

    cv1=Label(frame,text="PIN",font=("italic"),bd=2).place(x=300,y=250)
    cv2=Entry(frame,bd=4,textvar=cv,show='•',font=17).place(x=502,y=252)

    accn=Label(frame,text="Account Number",font=("italic"),bd=2).place(x=300,y=300)
    accn2=Entry(frame,bd=4,textvar=ac,font=17).place(x=502,y=302)

    
    email43=Label(frame,text="Email Address",font=("italic"),bd=2).place(x=300,y=350)
    email543=Entry(frame,bd=4,textvar=email,font=17).place(x=502,y=352)
    phn=Label(frame,text="Phone Number",font=("italic"),bd=2).place(x=300,y=400)
    phon=Entry(frame,bd=4,textvar=phone,font=17).place(x=502,y=402)
    phn1=Label(frame,text="Alternate Phone Number",font=("italic"),bd=2).place(x=300,y=450)
    phn2=Entry(frame,bd=4,textvar=phone1,font=17).place(x=502,y=452)
    branch43=Label(frame,text="Branch",font=("italic"),bd=2).place(x=300,y=500)
    brn=Entry(frame,bd=4,textvar=branch,font=17).place(x=502,y=502)
    count= Label(frame, text="Country",bd=2,font="italic").place(x=300,y=550)
    list=["India","England","Australia","USA","Netherland"];
    dropList=OptionMenu(frame,country,*list)
    dropList.config(width=20)
    country.set('Select your country')
    dropList.place(x=502,y=552)
    gen=Label(frame,text="Gender",bd=2,font="italic").place(x=300,y=600)
    Radiobutton(frame,text="Male",padx=5,pady=5,variable=gender,value=1).place(x=495,y=600)
    Radiobutton(frame,text="Female",padx=5,pady=5,variable=gender,value=2).place(x=550,y=600)
    

    def fr():
        tkinter.messagebox.showinfo("Successful","SUCCESSFULLY SIGNED UP")

    def trigger():
        
        if(len(name.get())==0 or len(passw.get())==0 or len(address.get())==0 or len(cv.get())==0 or len(ac.get())==0 or len(email.get())==0 or len(phone.get())==0 or len(phone1.get())==0 or len(branch.get())==0
           or gen==0):
            tkinter.messagebox.showerror("Empty Entry","Fill Up All The Entries")
            frame.destroy()
            fun()
            
            

        else:
            database()
            fr()
        
        
    submit=Button(frame,text="Submit",fg="silver",bg="grey",font=("italic",17),command= trigger)
    submit.place(x=470,y=640)
    b1=Button(frame,text="GO BACK TO LOGIN PAGE",fg="blue",bg="yellow",font=("bold",15),command=login).place(x=700,y=600)

img1=PhotoImage(file='login.gif')


def login():
    
    img2=PhotoImage(file='login1.gif')
    ment= StringVar()
    men= StringVar()
    frame1=Toplevel(height=1000,width=1000)
    frame1.config(background='white')
    
    Label(frame1,image=img1).place(x=100,y=0)
    
    name54=Label(frame1,text="NAME",font="bold",bd=2).place(x=300,y=300)
    named=Entry(frame1,bd=4,textvariable=men,font=20).place(x=450,y=302)
    name76=Label(frame1,text="PASSWORD",font="italic",bd=2).place(x=300,y=350)
    nameg=Entry(frame1,bd=4,textvariable=ment,show='•',font=20).place(x=450,y=352)
    
   
    conn = sqlite3.connect('ATM.db')
    cursor = conn.cursor()
    cursor.execute('SELECT Password, Name from Details1;')
    data = cursor.fetchall()
    conn.commit()


    def fr():
        global col
        metext=men.get()
        mtext=ment.get()
        count=0
        v=0
        i=0
        for i in range (0,len(data)):       # condition to check if data is found in database and if not found displaying correct error and also asking user for new input
            if(data[i][1]==metext):
                if(data[i][0]==mtext):
                    tkinter.messagebox.showinfo("Logged In","LOGGED IN SUCCESSFULLY")
                    count=1
                    v=0
                    col=0
                    break
                else:
                    col=col+1
                    if(col==3):
                        tkinter.messagebox.showerror("SIGN UP!! Seems you don't have an account","Maximum Login Limit Reached")
                        count=2
                        v=0
                        col=0
                        break
                    else:
                        tkinter.messagebox.showerror("Type Again","Wrong Password")
                        col=0
                        v=0
                        count=5
                        v=0
                        login()
                        break
            else:
                v=1
            
        if(v==1 and col==0):
            tkinter.messagebox.showinfo("Wrong UserName!! TRY AGAIN ","No Such Account Exists")
            ask=tkinter.messagebox.askyesno("CREATE A NEW ACCOUNT","Create A New Account")
            if(ask==True):
                fun()
                
        elif(count==0):
            tkinter.messagebox.showinfo("TRY AGAIN ","No Such Account Exists")
            login()
            
        elif(count==2):
            frame1.destroy()
            fun()
            
        elif(count is not 5):
            fre=Toplevel(height=1000,width=1000)
            fre.config(background='light blue')
            c=IntVar()
            c1=IntVar()
            c2=StringVar()
            Label(fre,image=img2,font="Times 20",bg="blue",fg="red").place(x=100,y=0)
            accno=Label(fre,text="Account Number",font="italic",bd=2).place(x=300,y=300)
            acc=Entry(fre,textvariable=c,font=20,bd=4).place(x=502,y=302)
            pasw213=Label(fre,text="PIN",font=("italic"),bd=2).place(x=300,y=350)
            pas21=Entry(fre,textvariable=c1,show='•',font=20,bd=4).place(x=502,y=352)
            add=Label(fre,text="Email Address",font=("italic"),bd=2).place(x=300,y=400)
            add1=Entry(fre,bd=4,font=20,textvar=c2).place(x=502,y=402)
            cou=StringVar()
            count= Label(fre, text="Debit/Credit",bd=2,font="italic").place(x=300,y=450)
            
            
            list1=["DEBIT","CREDIT TO ANOTHER ACCOUNT"];
            cou.set('Select TYPE')
            dropList=OptionMenu(fre,cou,*list1)
            dropList.config(width=20)
            dropList.place(x=502,y=452)

            
            conn = sqlite3.connect('ATM.db')
            cursor = conn.cursor()
            cursor.execute('SELECT Account_Num,Pin from Details1;')
            data1 = cursor.fetchall()
            conn.commit()
            
            img3=PhotoImage(file='plat.gif')
            img4=PhotoImage(file='login1.gif')

            
            def fr1():
                con=1
                c3=c.get()
                c4=c1.get()
                c5=c2.get()
                conn = sqlite3.connect('ATM.db')
                cursor = conn.cursor()
                cursor.execute('SELECT Name from Details1 WHERE Pin=? and Account_Num=? and Email=?',(c4,c3,c5,))
                data156 = cursor.fetchall()
                conn.commit()
                
                if(len(data156)==0):
                    tkinter.messagebox.showwarning("NO SUCH ACCOUNT","TRY ANOTHER ACCOUNT OR CHECK THE PASSWORD")
                    fr()
                    
                else:
                    for i in range (0,len(data1)):       # condition to check if data is found in database and if not found displaying correct error and also asking user for new input
                        if(data1[i][0]==c3):
                            if(data1[i][1]==c4):
                                con=1
                                if(cou.get()=="DEBIT"):
                                    con=1
                                    ext=IntVar()
                                    to=Toplevel(width=1000,height=1000)
                                    to.config(background='light blue')
                                    head1=Label(to,image=img4,bd=2,font="italic").place(x=100,y=0)
                                    head=Label(to,image=img3,bd=2,font="italic").place(x=580,y=250)
                                    head22=Label(to,text="DEBIT AMOUNT",bd=2,font=("italic",20),bg='purple',fg='yellow').place(x=300,y=200)
                                    ty=Label(to,text="Amount",bd=2,font=("bold",15)).place(x=180,y=280)
                                    ty1=Entry(to,bd=4,textvariable=ext,font=20).place(x=300,y=280)
                                    
                                    

                                    
                                    def fr3():
                                        conn = sqlite3.connect('ATM.db')
                                        cursor = conn.cursor()
                                        cursor.execute('SELECT Amount from Details1 WHERE Account_Num=?',(c3,))
                                        data2=cursor.fetchall()
                                        conn.commit()
                                        dah=data2[0][0]
                                        dah=dah-ext.get()
                                        
                                        if(dah<0):
                                            tkinter.messagebox.showwarning("UNSUCCESSFUL TRANSACTION","INSUFFICIENT MONEY IN ACCOUNT")
                                            
                                        else:
                                        
                                            cursor.execute('INSERT INTO Details3(Account_Num,Amount) VALUES(?,?)',(c3,dah))
                                            cursor.execute('UPDATE Details1 SET Amount=? WHERE Account_Num=?',(dah,c3))
                                            conn.commit()
                                            
                                            #sendmail(c5)
                                            msg=tkinter.messagebox.askyesno("Successfull Transaction","To see MINI STATEMENT PRESS YES else NO")
                                            

                                            
                                            def passbook():
                                                img19=PhotoImage(file='State12.gif')
                                                conn = sqlite3.connect('ATM.db')
                                                cursor = conn.cursor()
                                                cursor.execute('SELECT Account_Num,Amount from Details3 WHERE Account_Num=?',(c3,))
                                                daf=cursor.fetchall()
                                                conn.commit
                                                
                                                y1=200
                                                i=0
                                                b=1
                                                to1=Toplevel(height=1000,width=1000)
                                                to1.config(background='light blue')
                                                Label(to1,image=img19).place(x=100,y=0)
                                                if(len(daf)<10):
                                                    for i in range(0,len(daf)):
                                                        Label(to1,text=('Amount: {} = {}'.format(b,daf[i][1])),bd=1,font="italic").place(x=300,y=(0+y1))
                                                        Label(to1,text='----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------',bd=1,font="italic").place(x=0,y=(y1+20))
                                                        y1=y1+40
                                                        b=b+1
                                                else:
                                                    for i in range((len(daf)-10),len(daf)):
                                                        Label(to1,text=('Amount: {} = {}'.format(b,daf[i][1])),bd=1,font="italic").place(x=300,y=(0+y1))
                                                        Label(to1,text='----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------',bd=1,font="italic").place(x=0,y=(y1+20))
                                                        y1=y1+40
                                                        b=b+1
                                        
                                            if(msg==True):
                                                passbook()
                
                                    
                                    submit=Button(to,text="Submit",fg="silver",bg="grey",font=("italic",12),command=fr3).place(x=290,y=330)

                                
                                elif(cou.get()=="CREDIT TO ANOTHER ACCOUNT"):        #CREDIT MONEY TO ANOTHER ACCOUNT
                                    img6=PhotoImage(file='login1.gif')
                                    def credit():
                                        name=StringVar()
                                        accnum=IntVar()
                                        amcr=StringVar()

                                        img7=PhotoImage(file='plat.gif')
                                        img8=PhotoImage(file='login1.gif')

                                    
                                        def frk():
                                            cna=name.get()
                                            accnm=accnum.get()
                                            amcr1=amcr.get()
                                            conn = sqlite3.connect('ATM.db')
                                            cursor = conn.cursor()
                                            cursor.execute('SELECT Name,Account_Num,Branch from Details1 WHERE Name=? and Account_Num=? and Branch=?',(cna,accnm,amcr1))
                                            data25=cursor.fetchall()

                                            if(len(data25)==0):
                                                tkinter.messagebox.showwarning("No Such Account Exists","Try The Right Account")
                                                msg=tkinter.messagebox.askyesno("Want to Continue?","Try The Right Account Again")
                                                if(msg==True):
                                                    credit()
                                                
                                                else:
                                                    exit()
                                                
                                            else:
                                            
                                                con=1
                                                ext=IntVar()
                                                to16=Toplevel(width=1000,height=1000)
                                                to16.config(background='white')
                                                head1=Label(to16,image=img7).place(x=670,y=250)
                                                head12=Label(to16,image=img8).place(x=100,y=0)
                                                head=Label(to16,text="CREDIT AMOUNT",bd=2,font=("italic",20),bg='light blue',fg='blue').place(x=300,y=200)
                                                ty=Label(to16,text="Amount",bd=2,font=("italic",15)).place(x=260,y=280)
                                                ty1=Entry(to16,bd=4,textvariable=ext,font=20).place(x=350,y=280)
                                            
                                                img5=PhotoImage(file='State.gif')

                                            
                                                def fr3():
                                                
                                                    conn = sqlite3.connect('ATM.db')
                                                    cursor = conn.cursor()
                                                    cursor.execute('SELECT Amount from Details1 WHERE Account_Num=?',(accnm,))
                                                    data2=cursor.fetchall()
                                                    cursor.execute('SELECT Amount from Details1 WHERE Account_Num=?',(c3,))
                                                    data3=cursor.fetchall()
                                                    conn.commit()
                                                    
                                                    dah=data2[0][0]
                                                    dah1=data3[0][0]
                                                    dah=dah+ext.get()
                                                    dah1=dah1-ext.get()
                                                
                                                    if(dah1<0):
                                                        tkinter.messagebox.showwarning("UNSUCCESSFUL TRANSACTION","INSUFFICIENT MONEY IN ACCOUNT")
                                                        exit()
                                                    
                                                    else:
                                        
                                                        cursor.execute('INSERT INTO Details3(Account_Num,Amount) VALUES(?,?)',(accnm,dah))
                                                        cursor.execute('UPDATE Details1 SET Amount=? WHERE Account_Num=?',(dah,accnm))
                                                        cursor.execute('INSERT INTO Details3(Account_Num,Amount) VALUES(?,?)',(c3,dah1))
                                                        cursor.execute('UPDATE Details1 SET Amount=? WHERE Account_Num=?',(dah1,c3))
                                                        conn.commit()

                                                        #sendmail(c5)

                                                        msg=tkinter.messagebox.askyesno("Successfull Transaction","To see MINI STATEMENT PRESS YES else NO")

                                                    
                                                        def passbook1():
                                                            conn = sqlite3.connect('ATM.db')
                                                            cursor = conn.cursor()
                                                            cursor.execute('SELECT Account_Num,Amount from Details3 WHERE Account_Num=?',(c3,))
                                                            daf=cursor.fetchall()
                                                            conn.commit()
                                                        
                                                            y1=200
                                                            i=0
                                                            b=1
                                                            to12=Toplevel(height=1000,width=1000)
                                                            to12.config(background='light blue')
                                                            Label(to12,image=img5).place(x=100,y=0)
                                                            if(len(daf)<10):
                                                                for i in range(0,len(daf)):
                                                                    Label(to12,text=('Amount: {} = {}'.format(b,daf[i][1])),bd=2,font="italic").place(x=300,y=(0+y1))
                                                                    Label(to12,text='----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------',bd=1,font="italic").place(x=0,y=(y1+20))
                                                                    y1=y1+40
                                                                    b=b+1
                                                            else:
                                                                for i in range((len(daf)-10),len(daf)):
                                                                    Label(to12,text=('Amount: {} = {}'.format(b,daf[i][1])),bd=2,font="italic").place(x=300,y=(0+y1))
                                                                    Label(to12,text='----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------',bd=1,font="italic").place(x=0,y=(y1+20))
                                                                    y1=y1+40
                                                                    b=b+1
                                        
                                                        if(msg==True):
                                                            passbook1()
                
                                    
                                                submit=Button(to16,text="Submit",fg="silver",bg="grey",font=("italic",15),command=fr3).place(x=300,y=330)



                                        to67=Toplevel(height=1000,width=1000)
                                        to67.config(background='light blue')
                                        he=Label(to67,image=img6).place(x=100,y=0)
                                        he1=Label(to67,text="THE ACCOUNT YOU WANT TO CREDIT IN ",font=("bold",20),bd=4,bg='yellow',fg='red').place(x=250,y=300)
                                        he1=Label(to67,text="Name",font=("italic",12),bd=2).place(x=300,y=400)
                                        he2=Entry(to67,bd=4,textvar=name,font=20).place(x=502,y=402)
                                        he3=Label(to67,text="Account Number",font=("italic",12),bd=2).place(x=300,y=450)
                                        he4=Entry(to67,bd=4,textvar=accnum,font=20).place(x=502,y=452)
                                        he5=Label(to67,text="Branch",font=("italic",12),bd=2).place(x=300,y=500)
                                        he6=Entry(to67,bd=4,textvar=amcr,font=20).place(x=502,y=502)
                                
                                        submit=Button(to67,text="Submit",fg="silver",bg="grey",font=("italic",14),command= frk)
                                        submit.place(x=502,y=552)
                                    credit()
                            
                if(con==0):
                    tkinter.messagebox.showerror('Error', 'No Such Account Exists')
                    

            submit=Button(fre,text="Submit",fg="white",bg="grey",font=("italic",15),command=fr1).place(x=340,y=520)
            b1=Button(fre,text="CREATE A NEW ACCOUNT",fg="yellow",bg="blue",font=("bold",15),command=login).place(x=310,y=580)
                   
    submit=Button(frame1,text="Submit",fg="white",bg="grey",font=('Arial',15),command=fr).place(x=400,y=420)
    b1=Button(frame1,text="CREATE A NEW ACCOUNT",fg="yellow",bg="blue",font=('Arial',15),command=fun).place(x=320,y=470)    

imj=PhotoImage(file="about.gif")
def seedetails():
    frame2=Toplevel(height=1000,width=1000)
    frame2.config(background="white")
    Label(frame2,image=imj).place(x=0,y=0)


def main():
    root.geometry("1000x1000")
    root.config(background='light blue')
    fr1=Frame(root,width=1000,height=1000).place(x=1000,y=1000)
    
    Label(fr1,text="WELCOME TO SBI SERVICES",font="Times 30",bg="blue",fg="yellow").place(x=220,y=0)
    Label(fr1,image=img).place(x=200,y=100)
    Button(fr1,text="SIGN UP",command=fun,fg="blue",bg="yellow",font=('Arial',15)).place(x=250,y=450)
    Button(fr1,text="SEE DETAILS",command=seedetails,fg="blue",bg="yellow",font=('Arial',15)).place(x=590,y=450)
    Button(fr1,text="SIGN IN",command=login,fg="blue",bg="yellow",font=('Arial',17)).place(x=430,y=520)
    root.mainloop()
    
main()
