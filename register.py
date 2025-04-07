from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

class RegisterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        # Variables for registration fields
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        
        # Background image
        self.bg = ImageTk.PhotoImage(file="images/employee_img2.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Left image
        # Left image
        img = Image.open("images/register_image.jpg")
        img = img.resize((470, 550), Image.Resampling.LANCZOS)  # Resize to match the frame dimensions
        self.bg1 = ImageTk.PhotoImage(img)
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)
        
        # Registration frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)
        
        register_lbl = Label(frame, text="REGISTER HERE", font=("Times New Roman", 20, "bold"),
                             fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)
        
        # First Name
        fname_lbl = Label(frame, text="First Name", font=("Times New Roman", 15, "bold"), bg="white")
        fname_lbl.place(x=50, y=100)
        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("Times New Roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)
        
        # Last Name
        lname_lbl = Label(frame, text="Last Name", font=("Times New Roman", 15, "bold"), bg="white", fg="black")
        lname_lbl.place(x=370, y=100)
        self.lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("Times New Roman", 15, "bold"))
        self.lname_entry.place(x=370, y=130, width=250)
        
        # Contact
        contact_lbl = Label(frame, text="Contact No", font=("Times New Roman", 15, "bold"), bg="white", fg="black")
        contact_lbl.place(x=50, y=170)
        self.contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("Times New Roman", 15, "bold"))
        self.contact_entry.place(x=50, y=200, width=250)
        
        # Email
        email_lbl = Label(frame, text="Email", font=("Times New Roman", 15, "bold"), bg="white", fg="black")
        email_lbl.place(x=370, y=170)
        self.email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("Times New Roman", 15, "bold"))
        self.email_entry.place(x=370, y=200, width=250)
        
        # Security Question
        securityQ_lbl = Label(frame, text="Select Security Question", font=("Times New Roman", 15, "bold"),
                              bg="white", fg="black")
        securityQ_lbl.place(x=50, y=240)
        self.combo_securityQ = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("Times New Roman", 15, "bold"), state="readonly")
        self.combo_securityQ["values"] = ("Select", "Your Birth Place", "Your Nick name", "Your Blood Group")
        self.combo_securityQ.place(x=50, y=270, width=250)
        self.combo_securityQ.current(0)
        
        # Security Answer
        securityA_lbl = Label(frame, text="Security Answer", font=("Times New Roman", 15, "bold"),
                              bg="white", fg="black")
        securityA_lbl.place(x=370, y=240)
        self.securityA_entry = ttk.Entry(frame, textvariable=self.var_SecurityA, font=("Times New Roman", 15, "bold"))
        self.securityA_entry.place(x=370, y=270, width=250)
        
        # Password
        pswd_lbl = Label(frame, text="Password", font=("Times New Roman", 15, "bold"),
                         bg="white", fg="black")
        pswd_lbl.place(x=50, y=310)
        self.pswd_entry = ttk.Entry(frame, textvariable=self.var_pass, font=("Times New Roman", 15, "bold"))
        self.pswd_entry.place(x=50, y=340, width=250)
        
        # Confirm Password
        confpswd_lbl = Label(frame, text="Confirm Password", font=("Times New Roman", 15, "bold"),
                             bg="white", fg="black")
        confpswd_lbl.place(x=370, y=310)
        self.confpswd_entry = ttk.Entry(frame, textvariable=self.var_confpass, font=("Times New Roman", 15, "bold"))
        self.confpswd_entry.place(x=370, y=340, width=250)
        
        # Terms and Conditions
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions",
                                    bg="white", font=("Times New Roman", 12, "bold"), onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=380)
        
        # Register and Login Buttons
        img_register = Image.open("images/register-now-button1.jpg")
        img_register = img_register.resize((200, 55), Image.Resampling.LANCZOS)  # Changed from ANTIALIAS
        self.photo_img_register = ImageTk.PhotoImage(img_register)
        btn_register = Button(frame, image=self.photo_img_register, command=self.register_data,
                              borderwidth=0, cursor="hand2", font=("Times New Roman", 15, "bold"), fg="white")
        btn_register.place(x=10, y=420, width=200)
        
        img_login = Image.open("images/loginpng.png")
        img_login = img_login.resize((200, 45), Image.Resampling.LANCZOS)  # Changed from ANTIALIAS
        self.photo_img_login = ImageTk.PhotoImage(img_login)
        btn_login = Button(frame, image=self.photo_img_login, command=self.return_login,
                           borderwidth=0, cursor="hand2", font=("Times New Roman", 15, "bold"), fg="white")
        btn_login.place(x=330, y=420, width=200)
    
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydata")
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email", parent=self.root)
                else:
                    insert_query = "INSERT INTO register VALUES(%s, %s, %s, %s, %s, %s, %s)"
                    my_cursor.execute(insert_query, (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_SecurityA.get(),
                        self.var_pass.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Success", "Registered Successfully", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)
    
    def return_login(self):
        self.root.destroy()
