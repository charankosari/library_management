from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from register import RegisterWindow
from library_management import LibraryManagementSystem

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1550x800+0+0")
        
        # Background image
        img_bg = Image.open("images/Library_Image.png")
        img_bg = img_bg.resize((1530, 800), Image.Resampling.LANCZOS)  # Changed from ANTIALIAS
        self.photo_img_bg = ImageTk.PhotoImage(img_bg)
        bg_lbl = Label(self.root, image=self.photo_img_bg)
        bg_lbl.place(x=0, y=0, width=1530, height=800)
        
        # Title
        title = Label(bg_lbl, text="Library Management System", font=("Times New Roman", 42, "bold"),
                      bg="orange", fg="red")
        title.place(x=0, y=0, width=1550, height=70)
        
        # Login frame
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=200, width=340, height=430)
        
        # Icon in the login window
        img_icon = Image.open("images/LoginIconAppl.png")
        img_icon = img_icon.resize((90, 90), Image.Resampling.LANCZOS)  # Changed from ANTIALIAS
        self.photo_img_icon = ImageTk.PhotoImage(img_icon)
        lbl_img_icon = Label(self.root, image=self.photo_img_icon, bg="black", borderwidth=0)
        lbl_img_icon.place(x=730, y=200, width=90, height=90)
        
        # Login header
        get_str = Label(frame, text="Admin Login", font=("Times New Roman", 20, "bold"),
                        fg="white", bg="black")
        get_str.place(x=95, y=85)
        
        # Variables for username and password
        self.txtuser = StringVar()
        self.txtpass = StringVar()
        
        # Username
        username_lbl = Label(frame, text="Email", font=("Times New Roman", 12, "bold"),
                             fg="white", bg="black")
        username_lbl.place(x=70, y=125)
        txtuser_entry = ttk.Entry(frame, textvariable=self.txtuser, font=("Times New Roman", 15, "bold"))
        txtuser_entry.place(x=40, y=150, width=270)
        
        # Password
        password_lbl = Label(frame, text="Password", font=("Times New Roman", 12, "bold"),
                             fg="white", bg="black")
        password_lbl.place(x=70, y=195)
        txtpass_entry = ttk.Entry(frame, textvariable=self.txtpass, font=("Times New Roman", 15, "bold"), show="*")
        txtpass_entry.place(x=40, y=220, width=270)
        
        # Additional icons (optional)
        img_user_icon = Image.open("images/LoginIconAppl.png")
        img_user_icon = img_user_icon.resize((25, 25), Image.Resampling.LANCZOS)  # Changed from ANTIALIAS
        self.photo_img_user_icon = ImageTk.PhotoImage(img_user_icon)
        lbl_user_icon = Label(self.root, image=self.photo_img_user_icon, bg="black", borderwidth=0)
        lbl_user_icon.place(x=650, y=323, width=25, height=25)
        
        img_lock_icon = Image.open("images/lock-512.png")
        img_lock_icon = img_lock_icon.resize((25, 25), Image.Resampling.LANCZOS)  # Changed from ANTIALIAS
        self.photo_img_lock_icon = ImageTk.PhotoImage(img_lock_icon)
        lbl_lock_icon = Label(self.root, image=self.photo_img_lock_icon, bg="black", borderwidth=0)
        lbl_lock_icon.place(x=650, y=395, width=25, height=25)
        
        # Login button
        btn_login = Button(frame, text="Login", borderwidth=3, relief=RAISED,
                           command=self.login, cursor="hand2",
                           font=("Times New Roman", 16, "bold"), fg="white", bg="red",
                           activebackground="#B00857")
        btn_login.place(x=110, y=270, width=120, height=35)
        
        # Register and Forgot Password buttons
        registerbtn = Button(frame, text="New User Register", command=self.register_window,
                             font=("Times New Roman", 10, "bold"), borderwidth=0,
                             fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=320, width=160)
        
        forgetbtn = Button(frame, text="Forget Password", command=self.forgot_password_window,
                           font=("Times New Roman", 10, "bold"), borderwidth=0,
                           fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetbtn.place(x=10, y=340, width=160)
        
    def register_window(self):
        self.new_window = Toplevel(self.root)
        RegisterWindow(self.new_window)
    
    def login(self):
        # Hardcoded admin login for testing
        if self.txtuser.get() == "Pratik" and self.txtpass.get() == "Ketan":
            messagebox.showinfo("Success", "Welcome to Library Management System...")
            self.new_window = Toplevel(self.root)
            LibraryManagementSystem(self.new_window)
        elif self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", 
                                               password="root", database="mydata")
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s AND password=%s"
                value = (self.txtuser.get(), self.txtpass.get())
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Emaik & Password")
                else:
                    open_main = messagebox.askyesno("YesNo", "Enter Library Management System")
                    if open_main:
                        self.new_window = Toplevel(self.root)
                        LibraryManagementSystem(self.new_window)
                    else:
                        return
                conn.commit()
                self.clear()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
    
    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")
    
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset password")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root",
                                               password="root", database="mydata")
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.txtuser.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please enter a valid username")
                else:
                    conn.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("340x450+610+200")
                    self.root2.configure(bg="white")
                    
                    lbl = Label(self.root2, text="Forget Password", font=("Times New Roman", 20, "bold"),
                                fg="red", bg="white")
                    lbl.place(x=0, y=10, relwidth=1)
                    
                    security_Q = Label(self.root2, text="Select Security Question", 
                                       font=("Times New Roman", 15, "bold"), bg="white", fg="black")
                    security_Q.place(x=50, y=80)
                    
                    self.combo_securiy_Q = ttk.Combobox(self.root2, font=("Times New Roman", 15, "bold"), state="readonly")
                    self.combo_securiy_Q["values"] = ("Select", "Your Birth Place", "Your Nick name", "Your Pet Name")
                    self.combo_securiy_Q.place(x=50, y=110, width=250)
                    self.combo_securiy_Q.current(0)
                    
                    security_A = Label(self.root2, text="Security Answer", font=("Times New Roman", 15, "bold"),
                                       bg="white", fg="black")
                    security_A.place(x=50, y=150)
                    self.txt_security = ttk.Entry(self.root2, font=("Times New Roman", 15, "bold"))
                    self.txt_security.place(x=50, y=180, width=250)
                    
                    new_password = Label(self.root2, text="New Password", font=("Times New Roman", 15, "bold"),
                                         bg="white", fg="black")
                    new_password.place(x=50, y=220)
                    self.txt_newpass = ttk.Entry(self.root2, font=("Times New Roman", 15, "bold"))
                    self.txt_newpass.place(x=50, y=250, width=250)
                    
                    btn_reset = Button(self.root2, text="Reset", command=self.reset_pass,
                                       font=("Times New Roman", 15, "bold"), fg="white", bg="green")
                    btn_reset.place(x=120, y=290, width=100)
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
    
    def reset_pass(self):
        # Reset password functionality
        if (self.combo_securiy_Q.get() == "Select" or self.txt_security.get() == "" or
                self.txt_newpass.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root",
                                               password="root", database="mydata")
                cur = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
                value = (self.txtuser.get(), self.combo_securiy_Q.get(), self.txt_security.get())
                cur.execute(query, value)
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please select the correct security question/enter answer", parent=self.root2)
                else:
                    query = "UPDATE register SET password=%s WHERE email=%s"
                    value = (self.txt_newpass.get(), self.txtuser.get())
                    cur.execute(query, value)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Your password has been reset. Please login with new password", parent=self.root2)
                    self.root2.destroy()
                    self.txtuser.focus()
            except Exception as es:
                messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root2)
