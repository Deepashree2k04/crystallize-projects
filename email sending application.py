from tkinter import *
import smtplib
from PIL import ImageTk,Image


def button1():
        #going to page 2
        def nextpage():
                #sending process
                def sending():
                        
                        sender_email="shushilaliki@gmail.com"
                        sender_password="fhwe fawn axaq nakw"
                        server=smtplib.SMTP("smtp.gmail.com",587)
                        server.starttls()
                        server.login(sender_email,sender_password)
                        print("login successful !!")
                        to_email=to_email1.get()
                        #subject=subject1.get()
                        text=text1.get()
                        server.sendmail(sender_email, to_email, text)
                        print("message is sent")
                        #to_email2.delete(0,END)
                       #text2.delete(0,END)
                        

                # start_button.destroy()
                # title.destroy()
                # in_title.destroy()
                page.destroy()
                page2=Tk()
                page2.title("EMAIL SENDER")
                page2.geometry("400x280")

                to_email1=StringVar()
                subject1=StringVar()
                text1=StringVar()
                title1=Label(page2,text="Email Sending Application",font=("times new romen",10,"bold"),pady=2,bd=12,bg="#FFDEAD",fg="black",relief=GROOVE)
                title1.pack(fill=X)

                to_email=Label(page2,text="enter the reciver email address:",font=('times new romen',8,'bold'),fg="black",relief=GROOVE)
                to_email.place(x=50,y=50)

                to_email2=Entry(page2,textvariable=to_email1,width=35,font=("times new romen",8,"bold"),bg="light gray",relief=GROOVE)
                to_email2.place(x=50,y=80)

                subject=Label(page2,text="subject",font=('times new romen',8,'bold'),fg="black",relief=GROOVE)
                subject.place(x=50,y=110)

                subject2=Entry(page2,textvariable=subject1,width=35,font=("times new romen",8,"bold"),bg="light gray",relief=GROOVE)
                subject2.place(x=50,y=140)

                text=Label(page2,text="text",font=('times new romen',8,'bold'),fg="black",relief=GROOVE)
                text.place(x=50,y=170)

                text2=Entry(page2,textvariable=text1,font=("times new romen",8,"bold"),bg="light gray",relief=GROOVE)
                text2.place(x=50,y=200,width=310)

                start_button=Button(page2,text="send",bg="grey",command=sending)
                start_button.place(x=312,y=250,width=70)

        #second page        
        page=Tk()
        page.title("EMAIL SENDER")
        page.resizable(0, 0)
        page.geometry("550x300")
        page.configure(bg="#1874CD")        
        title=Label(page,text="Email Sending",font=("Goudy Old Style",39,"bold"),bg="#1874CD",fg="white")
        title.place(x=20,y=20)
        title=Label(page,text="Application",font=("Goudy Old Style",39,"bold"),bg="#1874CD",fg="white")
        title.place(x=40,y=90)
        emailImage=ImageTk.PhotoImage(Image.open("143.png"))
        emailImag=Label(page,image=emailImage,background="#1874CD")
        emailImag.place(x=375,y=60)
        in_title=Label(page,text="click here",font=("times new romen",9,"bold"),bg="white",fg="black")
        in_title.place(x=400,y=150)
        in_title=Label(page,text="to start",font=("times new romen",9,"bold"),bg="white",fg="black")
        in_title.place(x=400,y=170)

        start_button=Button(page,text="start",command=nextpage,bg="#1874CD",fg="white")
        start_button.place(x=412,y=200)               
 
        page.mainloop()
object=button1() 