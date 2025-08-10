create table supplier(
sno text primary key,
sname text,
status integer,
city text
);

insert into supplier values
('s1','sminth',20,'london'),
('s1','jones',10,'paris'),
('s3','baber',30,'paris'),
('s4','clarke',20,'london'),
('s5','sandy',30,'athens');

select sname,status from supplier;

select * from supplier;

create table student(
roll_number text,
sname text,
m1 real,
m2 real
);

insert into student VALUES
('1','sandy',45,55.3),
('2','rafay',88,22.78);

select * from student;