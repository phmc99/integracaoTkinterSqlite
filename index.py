#===============LIBS===============#
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import dataBaser

#===============JANELA===============#
janela = Tk()
janela.title('Access Panel')
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width=False, height=False)
janela.attributes("-alpha", 0.9) 
janela.iconbitmap(default="images/logo.ico")

#===============FUNÇOES===============#
def Register():
    loginButton.place(x="5000")
    registerButton.place(x="5000")
    
    nameLabel = Label(rightFrame, text="Name:", font=("Arial", 20), bg="midnightblue", fg="white")
    nameLabel.place(x="10", y="0")

    nameEntry = ttk.Entry(rightFrame, width="30")
    nameEntry.place(x="150", y="10")

    emailLabel = Label(rightFrame, text="E-mail:", font=("Arial", 20), bg="midnightblue", fg="white")
    emailLabel.place(x="10", y="50")

    emailEntry = ttk.Entry(rightFrame, width="30")
    emailEntry.place(x="150", y="60")

    def RegisterToDataBase():
        Name = nameEntry.get()
        Email = emailEntry.get()
        User = userEntry.get()
        Password = passEntry.get()

        if (Name == "" or Email == "" or User == "" or Password == ""):
            messagebox.showerror(title="Access Panel", message="Fill in all required fields!")
        else:
            dataBaser.cursor.execute("""
            INSERT INTO User(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Password))
            dataBaser.conn.commit()
            messagebox.showinfo(title="Access Panel", message="Account successfully created!")

    register = ttk.Button(rightFrame, text="Register", width="20", command=RegisterToDataBase)
    register.place(x="175", y="200")

    def backLogin():
        register.place(x="5000")
        nameLabel.place(x="5000")
        nameEntry.place(x="5000")
        emailLabel.place(x="5000")
        emailEntry.place(x="5000")
        backButton.place(x="5000")
        loginButton.place(x="175")
        registerButton.place(x="175")
        
    backButton = ttk.Button(rightFrame, text="Back", width="20", command=backLogin)
    backButton.place(x="175", y="230")

def loginAccess():
    userLogin = userEntry.get()
    passLogin = passEntry.get()
    dataBaser.cursor.execute("""
    SELECT * FROM User
    WHERE User = ? AND Password = ?
    """, (userLogin, passLogin))
    verify = dataBaser.cursor.fetchone()
    try:
        if(userLogin in verify and passLogin in verify):
            messagebox.showinfo(title="Access Panel", message="You are Logged in, welcome!")
        else:
            pass
    except:
        messagebox.showerror(title="Access Panel", message="Wrong e-mail or password.")


#===============CARREGANDO IMAGENS===============#
logo = PhotoImage(file="images/logo.png") 

#===============WIDGETS===============#
leftFrame = Frame(janela, width="200", height="300", bg="MIDNIGHTBLUE", relief="raise")
leftFrame.pack(side="left")

rightFrame = Frame(janela, width="398", height="300", bg="MIDNIGHTBLUE", relief="raise")
rightFrame.pack(side="right")

logoLabel = Label(leftFrame, image=logo, bg="midnightblue")
logoLabel.place(x="25", y="75")

userLabel = Label(rightFrame, text="Username:", font=("Arial", 20), bg="midnightblue", fg="white")
userLabel.place(x="10", y="100")

userEntry = ttk.Entry(rightFrame, width="30")
userEntry.place(x="150", y="110")

passLabel = Label(rightFrame, text="Password:", font=("Arial", 20), bg="midnightblue", fg="white")
passLabel.place(x="10", y="150")

passEntry = ttk.Entry(rightFrame, width="30", show="•")
passEntry.place(x="150", y="160")

#===============BOTOES===============#
loginButton = ttk.Button(rightFrame, text="Login", width="20", command=loginAccess)
loginButton.place(x="175", y="200")

registerButton = ttk.Button(rightFrame, text="Register", width="20", command=Register)
registerButton.place(x="175", y="230")


janela.mainloop()