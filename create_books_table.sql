CREATE TABLE IF NOT EXISTS books (
    id VARCHAR(20) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    publisher VARCHAR(255),
    year VARCHAR(10),
    isbn VARCHAR(20),
    category VARCHAR(50),
    price DECIMAL(10,2),
    quantity INT DEFAULT 1
);

-- Sample books data
INSERT INTO books (id, title, author, publisher, year, isbn, category, price, quantity) VALUES
('BKID5487', 'Head First Book', 'Paull Berry', 'O\'Reilly Media', '2015', '978-0596007126', 'Technology', 375.00, 5),
('BKID8796', 'Learn Python The Hard Way', 'Zed A. Shaw', 'Addison-Wesley', '2013', '978-0321884916', 'Technology', 725.00, 3),
('BKID1245', 'Python Programming', 'John Zhelle', 'Wiley', '2019', '978-1119551072', 'Technology', 500.00, 7),
('BKID2546', 'Python Cookbook', 'Brian Jones', 'O\'Reilly Media', '2013', '978-1449340377', 'Technology', 354.00, 4);