create table if not exists student(
    roll_no text primary key,
    name text not null,
    address text,
    phone text,
    age integer
);

insert into student values
('1','hasham','bangkok','****',21),
('2','rafay','islamabad','****',18),
('3','ricky','dehli','****',20),
('4','aman','islamabad','*****',19),
('5','john','lahore','******',20),

select * from student;