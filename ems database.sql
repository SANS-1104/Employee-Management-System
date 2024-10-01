use iimt;

drop table employee;

create table employee(
	eid int primary key auto_increment,
    ename varchar(40),
    email varchar(25) unique,
    phone bigint(10) unique,
    salary double (10,3),
    department varchar(15),
    post varchar(20)
);

INSERT INTO employee (ename, email, phone, salary, department, post)
VALUES
('John Doe', 'john.doe@gmail.com', 9876543210, 50000.000, 'IT', 'Manager'),
('Jane Smith', 'jane.smith@gmail.com', 9876543211, 45000.000, 'HR', 'HR Executive'),
('Michael Brown', 'michael.b@gmail.com', 9876543212, 55000.000, 'Finance', 'Accountant'),
('Emily Davis', 'emily.d@gmail.com', 9876543213, 60000.000, 'Sales', 'Sales Manager'),
('Chris Evans', 'chris.e@gmail.com', 9876543214, 48000.000, 'IT', 'Software Developer'),
('Sophia Turner', 'sophia.t@gmail.com', 9876543215, 52000.000, 'Marketing', 'Marketing Manager'),
('Liam Wilson', 'liam.w@gmail.com', 9876543216, 47000.000, 'Operations', 'Operations Manager'),
('Olivia Johnson', 'olivia.j@gmail.com', 9876543217, 51000.000, 'HR', 'HR Manager'),
('Noah Miller', 'noah.m@gmail.com', 9876543218, 53000.000, 'Finance', 'Financial Analyst'),
('Ava Martin', 'ava.m@gmail.com', 9876543219, 46000.000, 'IT', 'System Administrator');


select * from employee;

