from tkinter import *
from tkinter import ttk, messagebox
from time import strftime
import datetime
import mysql.connector
from book_management import BookManagement
class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        
        # Variables for membership and book details
        self.member_var = StringVar()
        self.ref_var = StringVar()
        self.title_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook = StringVar()
        self.lateratefine_var = StringVar()
        self.dateoverdue = StringVar()
        self.finallprice = StringVar()
        
        # Title label with clock
        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="white", fg="crimson",
                         bd=20, relief=RIDGE, font=("Times New Roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)
        
        def update_time():
            current_time = strftime('%I:%M:%S %p')
            clock_lbl.config(text=current_time)
            clock_lbl.after(1000, update_time)
        
        clock_lbl = Label(lbltitle, font=('Times New Roman', 15, 'bold'), background='purple', foreground='white')
        clock_lbl.place(x=0, y=0, width=150)
        update_time()
        
        # Data Frame
        data_frame = Frame(self.root, bd=20, padx=20, relief=RIDGE)
        data_frame.place(x=0, y=130, width=1530, height=400)
        
        # Left Frame for Membership Information
        data_frame_left = LabelFrame(data_frame, bd=12, padx=20, relief=RIDGE, fg="darkgreen",
                                     font=("Arial", 12, "bold"), text="Library Membership Information")
        data_frame_left.place(x=0, y=5, width=900, height=350)
        
        # Right Frame for Book Details
        data_frame_right = LabelFrame(data_frame, bd=12, padx=20, relief=RIDGE, fg="darkgreen",
                                      font=("Arial", 12, "bold"), text="Book Details")
        data_frame_right.place(x=910, y=5, width=540, height=350)
        
        # Button Frame
        button_frame = Frame(self.root, bd=20, padx=20, relief=RIDGE)
        button_frame.place(x=0, y=530, width=1530, height=70)
        
        btnAddData = Button(button_frame, command=self.add_data, text="ADD DATA", font=("Arial", 12, "bold"),
                            width=19, bg="crimson", fg="white")
        btnAddData.grid(row=0, column=0)
        
        btnShowData = Button(button_frame, command=self.showData, text="SHOW DATA", font=("Arial", 12, "bold"),
                             width=19, bg="crimson", fg="white")
        btnShowData.grid(row=0, column=1)
        
        btnUpdate = Button(button_frame, command=self.update_data, text="UPDATE", font=("Arial", 12, "bold"),
                           width=19, bg="crimson", fg="white")
        btnUpdate.grid(row=0, column=2)
        
        btnDelete = Button(button_frame, command=self.mDelete, text="DELETE", font=("Arial", 12, "bold"),
                           width=19, bg="crimson", fg="white")
        btnDelete.grid(row=0, column=3)
        
        btnReset = Button(button_frame, command=self.reset, text="RESET", font=("Arial", 12, "bold"),
                          width=19, bg="crimson", fg="white")
        btnReset.grid(row=0, column=4)
        
        # Add Manage Books button
        btnManageBooks = Button(button_frame, command=self.open_book_management, text="MANAGE BOOKS", 
                               font=("Arial", 12, "bold"), width=19, bg="crimson", fg="white")
        btnManageBooks.grid(row=0, column=5)
        
        btnExit = Button(button_frame, command=self.iExit, text="EXIT", font=("Arial", 12, "bold"),
                         width=19, bg="crimson", fg="white")
        btnExit.grid(row=0, column=6)
        
        # Details Frame (for displaying table records)
        details_frame = Frame(self.root, bd=20, padx=20, relief=RIDGE)
        details_frame.place(x=0, y=600, width=1530, height=195)
        
        # Left Frame Widgets (Membership Information)
        lblMember = Label(data_frame_left, font=("Arial", 12, "bold"), text="Member Type", padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)
        comMember = ttk.Combobox(data_frame_left, textvariable=self.member_var, state="readonly",
                                 font=("Arial", 12, "bold"), width=27)
        comMember['value'] = ("Admin Staff", "Lecturer", "Student")
        comMember.current(0)
        comMember.grid(row=0, column=1)
        
        lblRef = Label(data_frame_left, font=("Arial", 12, "bold"), text="Reference(PRN No):", padx=2)
        lblRef.grid(row=1, column=0, sticky=W)
        txtRef = Entry(data_frame_left, font=("Arial", 13, "bold"), textvariable=self.ref_var, width=29)
        txtRef.grid(row=1, column=1)
        
        lblTitle = Label(data_frame_left, font=("Arial", 12, "bold"), text="ID No:", padx=2, pady=4)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(data_frame_left, font=("Arial", 13, "bold"), textvariable=self.title_var, width=29)
        txtTitle.grid(row=2, column=1)
        
        lblFirstName = Label(data_frame_left, font=("Arial", 12, "bold"), text="First Name:", padx=2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(data_frame_left, font=("Arial", 13, "bold"), textvariable=self.firstname_var, width=29)
        txtFirstName.grid(row=3, column=1)
        
        lblLastName = Label(data_frame_left, font=("Arial", 12, "bold"), text="Surname:", padx=2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(data_frame_left, font=("Arial", 13, "bold"), textvariable=self.lastname_var, width=29)
        txtLastName.grid(row=4, column=1)
        
        lblAddress1 = Label(data_frame_left, font=("Arial", 12, "bold"), text="Address1:", padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(data_frame_left, font=("Arial", 13, "bold"), textvariable=self.address1_var, width=29)
        txtAddress1.grid(row=5, column=1)
        
        lblAddress2 = Label(data_frame_left, font=("Arial", 12, "bold"), text="Address2:", padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(data_frame_left, font=("Arial", 13, "bold"), textvariable=self.address2_var, width=29)
        txtAddress2.grid(row=6, column=1)
        
        lblPostCode = Label(data_frame_left, font=("Arial", 12, "bold"), text="Post Code:", padx=2, pady=4)
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(data_frame_left, font=("Arial", 13, "bold"), textvariable=self.postcode_var, width=29)
        txtPostCode.grid(row=7, column=1)
        
        lblMobile = Label(data_frame_left, font=("Arial", 12, "bold"), text="Mobile Number:", padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(data_frame_left, font=("Arial", 13, "bold"), textvariable=self.mobile_var, width=29)
        txtMobile.grid(row=8, column=1)
        
        # Book Details in Membership Information
        lblBookId = Label(data_frame_left, font=("Arial", 12, "bold"), text="Book ID:", padx=2)
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(data_frame_left, font=("Arial", 12, "bold"), textvariable=self.bookid_var, width=29)
        txtBookId.grid(row=0, column=3)
        
        lblBookTitle = Label(data_frame_left, font=("Arial", 12, "bold"), text="Book Title:", padx=2, pady=6)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(data_frame_left, font=("Arial", 12, "bold"), textvariable=self.booktitle_var, width=29)
        txtBookTitle.grid(row=1, column=3)
        
        lblAuther = Label(data_frame_left, font=("Arial", 12, "bold"), text="Auther Name:", padx=2, pady=6)
        lblAuther.grid(row=2, column=2, sticky=W)
        txtAuther = Entry(data_frame_left, font=("Arial", 12, "bold"), textvariable=self.auther_var, width=29)
        txtAuther.grid(row=2, column=3)
        
        lblDateBorrowed = Label(data_frame_left, font=("Arial", 12, "bold"), text="Date Borrowed:", padx=2, pady=6)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(data_frame_left, font=("Arial", 12, "bold"), textvariable=self.dateborrowed_var, width=29)
        txtDateBorrowed.grid(row=3, column=3, sticky=W)
        
        lblDateDue = Label(data_frame_left, font=("Arial", 12, "bold"), text="Date Due:", padx=2, pady=6)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(data_frame_left, font=("Arial", 12, "bold"), textvariable=self.datedue_var, width=29)
        txtDateDue.grid(row=4, column=3)
        
        lblDaysOnBook = Label(data_frame_left, font=("Arial", 12, "bold"), text="Days On Book:", padx=2, pady=6)
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(data_frame_left, font=("Arial", 12, "bold"), textvariable=self.daysonbook, width=29)
        txtDaysOnBook.grid(row=5, column=3)
        
        lblLateReturnFine = Label(data_frame_left, font=("Arial", 12, "bold"), text="Late Return Fine:", padx=2, pady=6)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(data_frame_left, font=("Arial", 12, "bold"), textvariable=self.lateratefine_var, width=29)
        txtLateReturnFine.grid(row=6, column=3)
        
        lblDateOverdue = Label(data_frame_left, font=("Arial", 12, "bold"), text="Date Over Due:", padx=2, pady=6)
        lblDateOverdue.grid(row=7, column=2, sticky=W)
        txtDateOverdue = Entry(data_frame_left, font=("Arial", 12, "bold"), textvariable=self.dateoverdue, width=29)
        txtDateOverdue.grid(row=7, column=3)
        
        lblFinalPrice = Label(data_frame_left, font=("Arial", 12, "bold"), text="Final Price:", padx=2, pady=6)
        lblFinalPrice.grid(row=8, column=2, sticky=W)
        txtFinalPrice = Entry(data_frame_left, font=("Arial", 12, "bold"), textvariable=self.finallprice, width=29)
        txtFinalPrice.grid(row=8, column=3)
        
        # Right Frame: Book List and Details TextBox
        self.txtBox = Text(data_frame_right, font=("Arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)
        
        listScrollbar = Scrollbar(data_frame_right)
        listScrollbar.grid(row=0, column=1, sticky="ns")
        
        # Create the book list widget
        self.bookList = Listbox(data_frame_right, font=("Arial", 12, "bold"), width=20, height=16)
        self.bookList.bind('<<ListboxSelect>>', self.select_book)
        self.bookList.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=self.bookList.yview)
        
        # Fetch books from database instead of hardcoded list
        self.fetch_books()
        
        # Table Frame for showing records
        table_frame = Frame(details_frame, bd=6, relief=RIDGE)
        table_frame.place(x=0, y=1, width=1460, height=150)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.library_table = ttk.Treeview(table_frame, column=("member", "ref", "title", "firtname",
                                                               "lastname", "adress1", "adress2", "postid",
                                                               "mobile", "bookid", "booktitle", "auther",
                                                               "dateborrowed", "datedue", "days", "latereturnfine",
                                                               "dateoverdue", "finalprice"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.library_table.xview)
        scroll_y.config(command=self.library_table.yview)
        
        headings = [
            ("member", "Member Type"), ("ref", "Reference No."), ("title", "Title"),
            ("firtname", "First Name"), ("lastname", "Last Name"), ("adress1", "Address1"),
            ("adress2", "Address2"), ("postid", "Post ID"), ("mobile", "Mobile Number"),
            ("bookid", "Book ID"), ("booktitle", "Book Title"), ("auther", "Auther"),
            ("dateborrowed", "Date Of Borrowed"), ("datedue", "Date Due"), ("days", "DaysOnBook"),
            ("latereturnfine", "LateReturnFine"), ("dateoverdue", "DateOverDue"),
            ("finalprice", "Final Price")
        ]
        
        for col, heading in headings:
            self.library_table.heading(col, text=heading)
            self.library_table.column(col, width=100)
        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)
        
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
    
    # Database operations
    def add_data(self):
        if self.member_var.get() == "" or self.postcode_var.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                conn =conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydata")
                my_cursor = conn.cursor()
                insert_query = """INSERT INTO library 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                values = (
                    self.member_var.get(),
                    self.ref_var.get(),
                    self.title_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address1_var.get(),
                    self.address2_var.get(),
                    self.postcode_var.get(),
                    self.mobile_var.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.auther_var.get(),
                    self.dateborrowed_var.get(),
                    self.datedue_var.get(),
                    self.daysonbook.get(),
                    self.lateratefine_var.get(),
                    self.dateoverdue.get(),
                    self.finallprice.get()
                )
                my_cursor.execute(insert_query, values)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Member has been inserted", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)
    
    def update_data(self):
        if self.ref_var.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", 
                                               password="root", database="mydata")
                my_cursor = conn.cursor()
                update_query = """UPDATE library SET 
                    Member_type=%s, ID_No=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, 
                    PostCode=%s, Mobile=%s, Bookid=%s, Booktitle=%s, Auther=%s, DateBorrowed=%s, 
                    DateDue=%s, DaysOfBook=%s, LateReturnFine=%s, DateOverDue=%s, FinalPrice=%s 
                    WHERE PRN_No=%s"""
                values = (
                    self.member_var.get(),
                    self.title_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address1_var.get(),
                    self.address2_var.get(),
                    self.postcode_var.get(),
                    self.mobile_var.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.auther_var.get(),
                    self.dateborrowed_var.get(),
                    self.datedue_var.get(),
                    self.daysonbook.get(),
                    self.lateratefine_var.get(),
                    self.dateoverdue.get(),
                    self.finallprice.get(),
                    self.ref_var.get()
                )
                my_cursor.execute(update_query, values)
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()
                messagebox.showinfo("Update", "Record has been updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)
    
    # Add this import at the top of the file
    from book_management import BookManagement
    
    # Add this method to the LibraryManagementSystem class
    def open_book_management(self):
        self.new_window = Toplevel(self.root)
        self.book_app = BookManagement(self.new_window, self)
        # self.
    
    # Method to handle book selection
    def select_book(self, event=""):
        try:
            index = self.bookList.curselection()[0]
            selected = self.bookList.get(index)
            
            # Get book details from database
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM books WHERE title = %s", (selected,))
            book_data = my_cursor.fetchone()
            
            if book_data:
                self.bookid_var.set(book_data[0])  # Assuming book_id is first column
                self.booktitle_var.set(book_data[1])  # Assuming title is second column
                self.auther_var.set(book_data[2])  # Assuming author is third column
                
                # Set standard borrowing details
                d1 = datetime.date.today()
                d3 = d1 + datetime.timedelta(days=15)
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set("15")
                self.lateratefine_var.set("Rs.25")
                self.dateoverdue.set("NO")
                
                # Set price if available in database, otherwise use default
                if len(book_data) > 3 and book_data[3]:
                    self.finallprice.set(f"Rs.{book_data[3]}")
                else:
                    self.finallprice.set("Rs.500")
                    
            conn.close()
        except Exception as es:
            pass  # Handle silently or show error message
    
    # Method to fetch books from database
    def fetch_books(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT title FROM books")
            books = my_cursor.fetchall()
            
            # Clear the existing list
            self.bookList.delete(0, END)
            
            # Add books from database to the list
            for book in books:
                self.bookList.insert(END, book[0])  # book[0] is the title
            
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error fetching books: {str(es)}", parent=self.root)
    
    # Modify the fetch_data method to also fetch books
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM library")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.library_table.delete(*self.library_table.get_children())
                for row in rows:
                    self.library_table.insert("", END, values=row)
                conn.commit()
            conn.close()
            
            # Also refresh the book list
            self.fetch_books()
        except Exception as es:
            messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)
    
    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content["values"]
        if row:
            self.member_var.set(row[0])
            self.ref_var.set(row[1])
            self.title_var.set(row[2])
            self.firstname_var.set(row[3])
            self.lastname_var.set(row[4])
            self.address1_var.set(row[5])
            self.address2_var.set(row[6])
            self.postcode_var.set(row[7])
            self.mobile_var.set(row[8])
            self.bookid_var.set(row[9])
            self.booktitle_var.set(row[10])
            self.auther_var.set(row[11])
            self.dateborrowed_var.set(row[12])
            self.datedue_var.set(row[13])
            self.daysonbook.set(row[14])
            self.lateratefine_var.set(row[15])
            self.dateoverdue.set(row[16])
            self.finallprice.set(row[17])
    
    def mDelete(self):
        if self.ref_var.get() == "":
            messagebox.showinfo("Error", "First select the member!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", 
                                               password="root", database="mydata")
                my_cursor = conn.cursor()
                delete_query = "DELETE FROM library WHERE PRN_No=%s"
                value = (self.ref_var.get(),)
                my_cursor.execute(delete_query, value)
                conn.commit()
                conn.close()
                self.fetch_data()
                self.reset()
                messagebox.showinfo("Delete", "Member has been deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)
    
    def iExit(self):
        exit_confirm = messagebox.askyesno("Library Management System", "Confirm if you want to exit", parent=self.root)
        if exit_confirm:
            self.root.destroy()
    
    def reset(self):
        self.member_var.set("")
        self.ref_var.set("")
        self.title_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.auther_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook.set("")
        self.lateratefine_var.set("")
        self.dateoverdue.set("")
        self.finallprice.set("")
        self.txtBox.delete("1.0", END)
    
    def showData(self):
        self.txtBox.delete("1.0", END)
        self.txtBox.insert(END, f"Member Type:\t\t{self.member_var.get()}\n")
        self.txtBox.insert(END, f"Reference(PRN No):\t\t{self.ref_var.get()}\n")
        self.txtBox.insert(END, f"ID No:\t\t{self.title_var.get()}\n")
        self.txtBox.insert(END, f"First Name:\t\t{self.firstname_var.get()}\n")
        self.txtBox.insert(END, f"Last Name:\t\t{self.lastname_var.get()}\n")
        self.txtBox.insert(END, f"Address1:\t\t{self.address1_var.get()}\n")
        self.txtBox.insert(END, f"Address2:\t\t{self.address2_var.get()}\n")
        self.txtBox.insert(END, f"Post Code:\t\t{self.postcode_var.get()}\n")
        self.txtBox.insert(END, f"Mobile No:\t\t{self.mobile_var.get()}\n")
        self.txtBox.insert(END, f"Book ID:\t\t{self.bookid_var.get()}\n")
        self.txtBox.insert(END, f"Book Title:\t\t{self.booktitle_var.get()}\n")
        self.txtBox.insert(END, f"Auther:\t\t{self.auther_var.get()}\n")
        self.txtBox.insert(END, f"Date Borrowed:\t\t{self.dateborrowed_var.get()}\n")
        self.txtBox.insert(END, f"Date Due:\t\t{self.datedue_var.get()}\n")
        self.txtBox.insert(END, f"Days On Book:\t\t{self.daysonbook.get()}\n")
        self.txtBox.insert(END, f"Late Return Fine:\t\t{self.lateratefine_var.get()}\n")
        self.txtBox.insert(END, f"Date Over Due:\t\t{self.dateoverdue.get()}\n")
        self.txtBox.insert(END, f"Final Price:\t\t{self.finallprice.get()}\n")
