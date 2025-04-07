CREATE TABLE register (
    fname VARCHAR(100),
    lname VARCHAR(100),
    contact VARCHAR(15),
    email VARCHAR(100) PRIMARY KEY,
    securityQ VARCHAR(50),
    securityA VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE library (
    Member_type VARCHAR(50),
    PRN_No VARCHAR(50) PRIMARY KEY,
    ID_No VARCHAR(50),
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Address1 VARCHAR(255),
    Address2 VARCHAR(255),
    PostCode VARCHAR(10),
    Mobile VARCHAR(20),
    Bookid VARCHAR(50),
    Booktitle VARCHAR(255),
    Auther VARCHAR(100),
    DateBorrowed DATE,
    DateDue DATE,
    DaysOfBook INT,
    LateReturnFine VARCHAR(50),
    DateOverDue VARCHAR(50),
    FinalPrice VARCHAR(50)
);
