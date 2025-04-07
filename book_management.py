from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import datetime

class BookManagement:
    def __init__(self, root, library_system=None):
        self.root = root
        self.root.title("Book Management System")
        self.root.geometry("1200x700+0+0")
        self.library_system = library_system
        
        # Variables
        self.book_id_var = StringVar()
        self.book_title_var = StringVar()
        self.author_var = StringVar()
        self.publisher_var = StringVar()
        self.year_var = StringVar()
        self.isbn_var = StringVar()
        self.category_var = StringVar()
        self.price_var = StringVar()
        self.quantity_var = StringVar()
        
        # Title
        lbltitle = Label(self.root, text="BOOK MANAGEMENT SYSTEM", bg="white", fg="crimson",
                         bd=20, relief=RIDGE, font=("Times New Roman", 40, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)
        
        # Main Frame
        main_frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="white")
        main_frame.place(x=0, y=130, width=1200, height=400)
        
        # Left Frame for Book Information
        left_frame = LabelFrame(main_frame, text="Book Information", bd=12, relief=RIDGE,
                               font=("Arial", 12, "bold"), fg="darkgreen", bg="white")
        left_frame.place(x=10, y=10, width=400, height=350)
        
        # Book ID
        lbl_book_id = Label(left_frame, text="Book ID:", font=("Arial", 12, "bold"), bg="white")
        lbl_book_id.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        txt_book_id = Entry(left_frame, textvariable=self.book_id_var, font=("Arial", 12))
        txt_book_id.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        
        # Book Title
        lbl_title = Label(left_frame, text="Title:", font=("Arial", 12, "bold"), bg="white")
        lbl_title.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        txt_title = Entry(left_frame, textvariable=self.book_title_var, font=("Arial", 12))
        txt_title.grid(row=1, column=1, sticky=W, padx=5, pady=5)
        
        # Author
        lbl_author = Label(left_frame, text="Author:", font=("Arial", 12, "bold"), bg="white")
        lbl_author.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        txt_author = Entry(left_frame, textvariable=self.author_var, font=("Arial", 12))
        txt_author.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        
        # Publisher
        lbl_publisher = Label(left_frame, text="Publisher:", font=("Arial", 12, "bold"), bg="white")
        lbl_publisher.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        txt_publisher = Entry(left_frame, textvariable=self.publisher_var, font=("Arial", 12))
        txt_publisher.grid(row=3, column=1, sticky=W, padx=5, pady=5)
        
        # Year
        lbl_year = Label(left_frame, text="Year:", font=("Arial", 12, "bold"), bg="white")
        lbl_year.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        txt_year = Entry(left_frame, textvariable=self.year_var, font=("Arial", 12))
        txt_year.grid(row=4, column=1, sticky=W, padx=5, pady=5)
        
        # ISBN
        lbl_isbn = Label(left_frame, text="ISBN:", font=("Arial", 12, "bold"), bg="white")
        lbl_isbn.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        txt_isbn = Entry(left_frame, textvariable=self.isbn_var, font=("Arial", 12))
        txt_isbn.grid(row=5, column=1, sticky=W, padx=5, pady=5)
        
        # Category
        lbl_category = Label(left_frame, text="Category:", font=("Arial", 12, "bold"), bg="white")
        lbl_category.grid(row=6, column=0, sticky=W, padx=5, pady=5)
        combo_category = ttk.Combobox(left_frame, textvariable=self.category_var, font=("Arial", 12),
                                     state="readonly", width=18)
        combo_category["values"] = ("Fiction", "Non-Fiction", "Science", "History", "Technology", 
                                   "Mathematics", "Biography", "Self-Help", "Reference", "Other")
        combo_category.grid(row=6, column=1, sticky=W, padx=5, pady=5)
        
        # Price
        lbl_price = Label(left_frame, text="Price:", font=("Arial", 12, "bold"), bg="white")
        lbl_price.grid(row=7, column=0, sticky=W, padx=5, pady=5)
        txt_price = Entry(left_frame, textvariable=self.price_var, font=("Arial", 12))
        txt_price.grid(row=7, column=1, sticky=W, padx=5, pady=5)
        
        # Quantity
        lbl_quantity = Label(left_frame, text="Quantity:", font=("Arial", 12, "bold"), bg="white")
        lbl_quantity.grid(row=8, column=0, sticky=W, padx=5, pady=5)
        txt_quantity = Entry(left_frame, textvariable=self.quantity_var, font=("Arial", 12))
        txt_quantity.grid(row=8, column=1, sticky=W, padx=5, pady=5)
        
        # Right Frame for Book List
        right_frame = LabelFrame(main_frame, text="Book List", bd=12, relief=RIDGE,
                                font=("Arial", 12, "bold"), fg="darkgreen", bg="white")
        right_frame.place(x=420, y=10, width=730, height=350)
        
        # Table Frame
        table_frame = Frame(right_frame, bd=6, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=10, width=690, height=300)
        
        # Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        # Book Table
        self.book_table = ttk.Treeview(table_frame, columns=("id", "title", "author", "publisher", 
                                                           "year", "isbn", "category", "price", "quantity"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.book_table.xview)
        scroll_y.config(command=self.book_table.yview)
        
        # Define columns
        self.book_table.heading("id", text="Book ID")
        self.book_table.heading("title", text="Title")
        self.book_table.heading("author", text="Author")
        self.book_table.heading("publisher", text="Publisher")
        self.book_table.heading("year", text="Year")
        self.book_table.heading("isbn", text="ISBN")
        self.book_table.heading("category", text="Category")
        self.book_table.heading("price", text="Price")
        self.book_table.heading("quantity", text="Quantity")
        
        self.book_table["show"] = "headings"
        
        # Set column widths
        self.book_table.column("id", width=70)
        self.book_table.column("title", width=150)
        self.book_table.column("author", width=120)
        self.book_table.column("publisher", width=120)
        self.book_table.column("year", width=70)
        self.book_table.column("isbn", width=100)
        self.book_table.column("category", width=100)
        self.book_table.column("price", width=70)
        self.book_table.column("quantity", width=70)
        
        self.book_table.pack(fill=BOTH, expand=1)
        self.book_table.bind("<ButtonRelease-1>", self.get_cursor)
        
        # Button Frame
        button_frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="white")
        button_frame.place(x=0, y=530, width=1200, height=70)
        
        # Buttons
        btn_add = Button(button_frame, text="Add Book", command=self.add_book, 
                        font=("Arial", 12, "bold"), width=15, bg="crimson", fg="white")
        btn_add.grid(row=0, column=0, padx=10)
        
        btn_update = Button(button_frame, text="Update Book", command=self.update_book, 
                           font=("Arial", 12, "bold"), width=15, bg="crimson", fg="white")
        btn_update.grid(row=0, column=1, padx=10)
        
        btn_delete = Button(button_frame, text="Delete Book", command=self.delete_book, 
                           font=("Arial", 12, "bold"), width=15, bg="crimson", fg="white")
        btn_delete.grid(row=0, column=2, padx=10)
        
        btn_clear = Button(button_frame, text="Clear Fields", command=self.clear_fields, 
                          font=("Arial", 12, "bold"), width=15, bg="crimson", fg="white")
        btn_clear.grid(row=0, column=3, padx=10)
        
        btn_refresh = Button(button_frame, text="Refresh List", command=self.fetch_data, 
                            font=("Arial", 12, "bold"), width=15, bg="crimson", fg="white")
        btn_refresh.grid(row=0, column=4, padx=10)
        
        # Load data
        self.fetch_data()
    
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", 
                                          password="root", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM books")
            rows = my_cursor.fetchall()
            
            if len(rows) != 0:
                self.book_table.delete(*self.book_table.get_children())
                for row in rows:
                    self.book_table.insert("", END, values=row)
                conn.commit()
            conn.close()
            
            # Update the book list in the main library system if it exists
            if self.library_system:
                self.library_system.fetch_books()
                
        except Exception as es:
            messagebox.showerror("Error", f"Error fetching data: {str(es)}", parent=self.root)
    
    def add_book(self):
        if (self.book_id_var.get() == "" or self.book_title_var.get() == "" or 
            self.author_var.get() == "" or self.category_var.get() == ""):
            messagebox.showerror("Error", "Book ID, Title, Author and Category are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", 
                                              password="root", database="mydata")
                my_cursor = conn.cursor()
                
                # Check if book ID already exists
                my_cursor.execute("SELECT * FROM books WHERE id=%s", (self.book_id_var.get(),))
                row = my_cursor.fetchone()
                
                if row:
                    messagebox.showerror("Error", "Book ID already exists", parent=self.root)
                else:
                    my_cursor.execute("INSERT INTO books VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                    (self.book_id_var.get(),
                                     self.book_title_var.get(),
                                     self.author_var.get(),
                                     self.publisher_var.get(),
                                     self.year_var.get(),
                                     self.isbn_var.get(),
                                     self.category_var.get(),
                                     self.price_var.get(),
                                     self.quantity_var.get()))
                    conn.commit()
                    self.fetch_data()
                    self.clear_fields()
                    conn.close()
                    messagebox.showinfo("Success", "Book added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error adding book: {str(es)}", parent=self.root)
    
    def update_book(self):
        if self.book_id_var.get() == "":
            messagebox.showerror("Error", "Book ID is required for updating", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", 
                                              password="root", database="mydata")
                my_cursor = conn.cursor()
                
                my_cursor.execute("UPDATE books SET title=%s, author=%s, publisher=%s, year=%s, "
                                "isbn=%s, category=%s, price=%s, quantity=%s WHERE id=%s",
                                (self.book_title_var.get(),
                                 self.author_var.get(),
                                 self.publisher_var.get(),
                                 self.year_var.get(),
                                 self.isbn_var.get(),
                                 self.category_var.get(),
                                 self.price_var.get(),
                                 self.quantity_var.get(),
                                 self.book_id_var.get()))
                conn.commit()
                self.fetch_data()
                self.clear_fields()
                conn.close()
                messagebox.showinfo("Success", "Book updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error updating book: {str(es)}", parent=self.root)
    
    def delete_book(self):
        if self.book_id_var.get() == "":
            messagebox.showerror("Error", "Book ID is required for deletion", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", 
                                              password="root", database="mydata")
                my_cursor = conn.cursor()
                
                delete_confirm = messagebox.askyesno("Delete Book", "Are you sure you want to delete this book?", 
                                                   parent=self.root)
                if delete_confirm:
                    my_cursor.execute("DELETE FROM books WHERE id=%s", (self.book_id_var.get(),))
                    conn.commit()
                    self.fetch_data()
                    self.clear_fields()
                    conn.close()
                    messagebox.showinfo("Success", "Book deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error deleting book: {str(es)}", parent=self.root)
    
    def clear_fields(self):
        self.book_id_var.set("")
        self.book_title_var.set("")
        self.author_var.set("")
        self.publisher_var.set("")
        self.year_var.set("")
        self.isbn_var.set("")
        self.category_var.set("")
        self.price_var.set("")
        self.quantity_var.set("")
    
    def get_cursor(self, event=""):
        cursor_row = self.book_table.focus()
        content = self.book_table.item(cursor_row)
        row = content["values"]
        
        if row:
            self.book_id_var.set(row[0])
            self.book_title_var.set(row[1])
            self.author_var.set(row[2])
            self.publisher_var.set(row[3])
            self.year_var.set(row[4])
            self.isbn_var.set(row[5])
            self.category_var.set(row[6])
            self.price_var.set(row[7])
            self.quantity_var.set(row[8])

class BookManagement:
    def __init__(self, root, library_instance):
        self.root = root
        self.root.title("Book Management")
        self.root.geometry("800x600+350+100")
        self.library_instance = library_instance
        
        # Variables for book details
        self.book_id_var = StringVar()
        self.title_var = StringVar()
        self.author_var = StringVar()
        self.publisher_var = StringVar()
        self.year_var = StringVar()
        self.isbn_var = StringVar()
        self.category_var = StringVar()
        self.price_var = StringVar()
        self.quantity_var = StringVar()
        
        # Title label
        lbltitle = Label(self.root, text="BOOK MANAGEMENT", bg="white", fg="darkgreen",
                         bd=20, relief=RIDGE, font=("Times New Roman", 30, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)
        
        # Main Frame
        main_frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, pady=20, bg="white")
        main_frame.place(x=0, y=100, width=800, height=500)
        
        # Book Entry Frame
        book_frame = LabelFrame(main_frame, text="Book Details", bd=12, relief=RIDGE, 
                               font=("Arial", 12, "bold"), bg="white", fg="darkgreen")
        book_frame.place(x=10, y=10, width=760, height=300)
        
        # Book ID
        lbl_book_id = Label(book_frame, text="Book ID:", font=("Arial", 12, "bold"), bg="white")
        lbl_book_id.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        txt_book_id = Entry(book_frame, textvariable=self.book_id_var, font=("Arial", 12), width=20)
        txt_book_id.grid(row=0, column=1, padx=5, pady=5)
        
        # Title
        lbl_title = Label(book_frame, text="Title:", font=("Arial", 12, "bold"), bg="white")
        lbl_title.grid(row=0, column=2, sticky=W, padx=5, pady=5)
        txt_title = Entry(book_frame, textvariable=self.title_var, font=("Arial", 12), width=20)
        txt_title.grid(row=0, column=3, padx=5, pady=5)
        
        # Author
        lbl_author = Label(book_frame, text="Author:", font=("Arial", 12, "bold"), bg="white")
        lbl_author.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        txt_author = Entry(book_frame, textvariable=self.author_var, font=("Arial", 12), width=20)
        txt_author.grid(row=1, column=1, padx=5, pady=5)
        
        # Publisher
        lbl_publisher = Label(book_frame, text="Publisher:", font=("Arial", 12, "bold"), bg="white")
        lbl_publisher.grid(row=1, column=2, sticky=W, padx=5, pady=5)
        txt_publisher = Entry(book_frame, textvariable=self.publisher_var, font=("Arial", 12), width=20)
        txt_publisher.grid(row=1, column=3, padx=5, pady=5)
        
        # Year
        lbl_year = Label(book_frame, text="Year:", font=("Arial", 12, "bold"), bg="white")
        lbl_year.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        txt_year = Entry(book_frame, textvariable=self.year_var, font=("Arial", 12), width=20)
        txt_year.grid(row=2, column=1, padx=5, pady=5)
        
        # ISBN
        lbl_isbn = Label(book_frame, text="ISBN:", font=("Arial", 12, "bold"), bg="white")
        lbl_isbn.grid(row=2, column=2, sticky=W, padx=5, pady=5)
        txt_isbn = Entry(book_frame, textvariable=self.isbn_var, font=("Arial", 12), width=20)
        txt_isbn.grid(row=2, column=3, padx=5, pady=5)
        
        # Category
        lbl_category = Label(book_frame, text="Category:", font=("Arial", 12, "bold"), bg="white")
        lbl_category.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        txt_category = Entry(book_frame, textvariable=self.category_var, font=("Arial", 12), width=20)
        txt_category.grid(row=3, column=1, padx=5, pady=5)
        
        # Price
        lbl_price = Label(book_frame, text="Price:", font=("Arial", 12, "bold"), bg="white")
        lbl_price.grid(row=3, column=2, sticky=W, padx=5, pady=5)
        txt_price = Entry(book_frame, textvariable=self.price_var, font=("Arial", 12), width=20)
        txt_price.grid(row=3, column=3, padx=5, pady=5)
        
        # Quantity
        lbl_quantity = Label(book_frame, text="Quantity:", font=("Arial", 12, "bold"), bg="white")
        lbl_quantity.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        txt_quantity = Entry(book_frame, textvariable=self.quantity_var, font=("Arial", 12), width=20)
        txt_quantity.grid(row=4, column=1, padx=5, pady=5)
        
        # Button Frame
        button_frame = Frame(main_frame, bd=12, relief=RIDGE, bg="white")
        button_frame.place(x=10, y=320, width=760, height=70)
        
        # Add Book Button
        btn_add = Button(button_frame, text="Add Book", command=self.add_book, 
                         font=("Arial", 12, "bold"), bg="darkgreen", fg="white", width=15)
        btn_add.grid(row=0, column=0, padx=10, pady=10)
        
        # Clear Button
        btn_clear = Button(button_frame, text="Clear", command=self.clear_fields, 
                          font=("Arial", 12, "bold"), bg="darkgreen", fg="white", width=15)
        btn_clear.grid(row=0, column=1, padx=10, pady=10)
        
        # Exit Button
        btn_exit = Button(button_frame, text="Exit", command=self.exit_window, 
                         font=("Arial", 12, "bold"), bg="darkgreen", fg="white", width=15)
        btn_exit.grid(row=0, column=2, padx=10, pady=10)
        
        # Book List Frame
        list_frame = Frame(main_frame, bd=12, relief=RIDGE, bg="white")
        list_frame.place(x=10, y=400, width=760, height=80)
        
        # Status Label
        self.status_label = Label(list_frame, text="Ready to add books", 
                                 font=("Arial", 12), bg="white", fg="darkgreen")
        self.status_label.pack(pady=20)
    
    def add_book(self):
        if (self.book_id_var.get() == "" or self.title_var.get() == "" or 
            self.author_var.get() == "" or self.price_var.get() == ""):
            messagebox.showerror("Error", "Book ID, Title, Author and Price are required fields", parent=self.root)
            return
        
        try:
            # Connect to database
            conn = mysql.connector.connect(host="localhost", user="root", 
                                          password="root", database="mydata")
            my_cursor = conn.cursor()
            
            # Check if book ID already exists
            my_cursor.execute("SELECT * FROM books WHERE id = %s", (self.book_id_var.get(),))
            existing_book = my_cursor.fetchone()
            
            if existing_book:
                update_confirm = messagebox.askyesno("Confirm", 
                                                    f"Book ID {self.book_id_var.get()} already exists. Update it?", 
                                                    parent=self.root)
                if update_confirm:
                    # Update existing book
                    update_query = """UPDATE books SET 
                        title = %s, author = %s, publisher = %s, year = %s, 
                        isbn = %s, category = %s, price = %s, quantity = %s 
                        WHERE id = %s"""
                    values = (
                        self.title_var.get(),
                        self.author_var.get(),
                        self.publisher_var.get(),
                        self.year_var.get(),
                        self.isbn_var.get(),
                        self.category_var.get(),
                        self.price_var.get(),
                        self.quantity_var.get() or "1",  # Default to 1 if empty
                        self.book_id_var.get()
                    )
                    my_cursor.execute(update_query, values)
                    conn.commit()
                    self.status_label.config(text=f"Book '{self.title_var.get()}' updated successfully")
                    messagebox.showinfo("Success", "Book updated successfully", parent=self.root)
                else:
                    return
            else:
                # Insert new book
                insert_query = """INSERT INTO books 
                    (id, title, author, publisher, year, isbn, category, price, quantity) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                values = (
                    self.book_id_var.get(),
                    self.title_var.get(),
                    self.author_var.get(),
                    self.publisher_var.get(),
                    self.year_var.get(),
                    self.isbn_var.get(),
                    self.category_var.get(),
                    self.price_var.get(),
                    self.quantity_var.get() or "1"  # Default to 1 if empty
                )
                my_cursor.execute(insert_query, values)
                conn.commit()
                self.status_label.config(text=f"Book '{self.title_var.get()}' added successfully")
                messagebox.showinfo("Success", "Book added successfully", parent=self.root)
            
            conn.close()
            
            # Refresh the book list in the main library window
            if self.library_instance:
                self.library_instance.fetch_books()
                
            # Clear fields after successful operation
            self.clear_fields()
            
        except Exception as es:
            messagebox.showerror("Error", f"Error adding book: {str(es)}", parent=self.root)
    
    def clear_fields(self):
        self.book_id_var.set("")
        self.title_var.set("")
        self.author_var.set("")
        self.publisher_var.set("")
        self.year_var.set("")
        self.isbn_var.set("")
        self.category_var.set("")
        self.price_var.set("")
        self.quantity_var.set("")
        self.status_label.config(text="Ready to add books")
    
    def exit_window(self):
        self.root.destroy()