pip install mysql-connector-python
CREATE DATABASE student;
USE student;

CREATE TABLE student (
    phone INT PRIMARY KEY,
    dep VARCHAR(20),
    course VARCHAR(20),
    year VARCHAR(20),
    sem VARCHAR(30),
    name VARCHAR(50),
    hall VARCHAR(20),
    roll VARCHAR(20),
    gender VARCHAR(10),
    dob varchar(10),
    email VARCHAR(50),
    reg varchar(10),
    address VARCHAR(100),
    photo VARCHAR(255)
);
INSERT INTO student values(154,"CSE","BTECH","2022","SECOND","NITISH","LH","154","MALE","2005","NVNDJNV","547","HDHVNIDS","NO");
select*FROM student;

 