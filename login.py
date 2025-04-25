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
        frame = Frame(self.root, bg="#181818")  # Darker background for modern look
        frame.place(x=550, y=170, width=450, height=500)
        
        # Icon in the login window (centered above the form)
        img_icon = Image.open("images/LoginIconAppl.png")
        img_icon = img_icon.resize((80, 80), Image.Resampling.LANCZOS)
        self.photo_img_icon = ImageTk.PhotoImage(img_icon)
        lbl_img_icon = Label(frame, image=self.photo_img_icon, bg="#181818", borderwidth=0)
        lbl_img_icon.place(x=185, y=20, width=80, height=80)
        
        # Login header
        get_str = Label(frame, text="Admin Login", font=("Times New Roman", 26, "bold"),
                        fg="#fff", bg="#181818")
        get_str.place(x=120, y=110)
        
        # Variables for username and password
        self.txtuser = StringVar()
        self.txtpass = StringVar()
        
        # Load icons once
        img_user_icon = Image.open("images/LoginIconAppl.png")
        img_user_icon = img_user_icon.resize((22, 22), Image.Resampling.LANCZOS)
        self.photo_img_user_icon = ImageTk.PhotoImage(img_user_icon)
        
        img_lock_icon = Image.open("images/lock-512.png")
        img_lock_icon = img_lock_icon.resize((22, 22), Image.Resampling.LANCZOS)
        self.photo_img_lock_icon = ImageTk.PhotoImage(img_lock_icon)
        
        # Email label and entry with icon
        username_lbl = Label(frame, text="Email", font=("Segoe UI", 13, "bold"),
                             fg="#fff", bg="#181818")
        username_lbl.place(x=60, y=160)
        user_entry_bg = Frame(frame, bg="#fff", bd=1, relief=SOLID)
        user_entry_bg.place(x=60, y=190, width=330, height=36)
        lbl_user_icon = Label(user_entry_bg, image=self.photo_img_user_icon, bg="#fff")
        lbl_user_icon.place(x=5, y=5)
        txtuser_entry = ttk.Entry(user_entry_bg, textvariable=self.txtuser, font=("Segoe UI", 12), width=26)
        txtuser_entry.place(x=35, y=2, height=30)
        
        # Password label and entry with icon
        password_lbl = Label(frame, text="Password", font=("Segoe UI", 13, "bold"),
                             fg="#fff", bg="#181818")
        password_lbl.place(x=60, y=240)
        pass_entry_bg = Frame(frame, bg="#fff", bd=1, relief=SOLID)
        pass_entry_bg.place(x=60, y=270, width=330, height=36)
        lbl_lock_icon = Label(pass_entry_bg, image=self.photo_img_lock_icon, bg="#fff")
        lbl_lock_icon.place(x=5, y=5)
        txtpass_entry = ttk.Entry(pass_entry_bg, textvariable=self.txtpass, font=("Segoe UI", 12), width=26, show="*")
        txtpass_entry.place(x=35, y=2, height=30)
        
        # Login button - centered and styled
        btn_login = Button(frame, text="Login", borderwidth=0, relief=RAISED,
                           command=self.login, cursor="hand2",
                           font=("Segoe UI", 15, "bold"), fg="#fff", bg="#e74c3c",
                           activebackground="#c0392b", activeforeground="#fff")
        btn_login.place(x=140, y=330, width=170, height=45)
        
        # Register and Forgot Password buttons - styled as links
        registerbtn = Button(frame, text="New User Register", command=self.register_window,
                             font=("Segoe UI", 11, "underline"), borderwidth=0,
                             fg="#3498db", bg="#181818", activeforeground="#2980b9", activebackground="#181818", cursor="hand2")
        registerbtn.place(x=140, y=390, width=170)

        forgetbtn = Button(frame, text="Forgot Password", command=self.forgot_password_window,
                           font=("Segoe UI", 11, "underline"), borderwidth=0,
                           fg="#3498db", bg="#181818", activeforeground="#2980b9", activebackground="#181818", cursor="hand2")
        forgetbtn.place(x=140, y=420, width=170)
        
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
