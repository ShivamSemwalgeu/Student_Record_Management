from tkinter import *    #for creating graphical user interface
from PIL import ImageTk   #pillow library  bcuz we cant use image directly (jpg)
                           #for png ,no need for importing this    
from tkinter import messagebox                         
def login():
        if usernameEntry.get()=='' or PasswordEntry.get()=='':
            messagebox.showerror('Error','fields cannot be empty')   
        elif  usernameEntry.get()=='shivam' and PasswordEntry.get()=='123':
            messagebox.showinfo('Success','Welcome')
            window.destroy()
            import sms     
        else: messagebox.showerror('Error','Please enter correct details')      
window=Tk()          #class from tkinter to create gui     
                       #window is object of tk class
   
window.geometry('1280x700+0+0')  #height and width maximise
window.title('Login System of Student Management System')
window.resizable(False,False)   #not to resize the window
backgroundImage=ImageTk.PhotoImage(file='bg1.jpg')   #object of image
bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)
loginFrame=Frame(window,bg='white')   #frame object
loginFrame.place(x=400,y=150)
logoImage=PhotoImage(file='logo.png')  #import logo og png type
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)  #to display logo

usernameLabel=Label(loginFrame,text='username',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')  #created label 
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='black')    #textfield
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

PasswordLabel=Label(loginFrame,text='Password',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')  #created label 
PasswordLabel.grid(row=2,column=0,pady=10,padx=20)

PasswordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='black')    #textfield
PasswordEntry.grid(row=2,column=1,pady=10,padx=20)


loginButton=Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15
                   ,fg='white',bg='cornflowerblue',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)



window.mainloop()     #to keep our window on loop so we can see it continuously
 
