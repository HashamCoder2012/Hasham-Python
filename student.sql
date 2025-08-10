create table if not exists student0(
    roll_no text primary key,
    name text not null,
    address text,
    phone text,
    age integer
);


insert into student0 values
('1','hasham','bangkok','*****',21),
('2','rafay','islamabad','*****',18),
('3','ricky','dehli','*****',20),
('4','aman','islamabad','*****',18),
('5','john','lahore','*****',20);

select * from student0;

select * from student0 where age=20 and address='dehli';

select * from student0 where age=18 and name='rafay';

select * from student0 where name ='hasham'or name='john';

select * from student0 where age=18 and (name='aman' or name='rafay');