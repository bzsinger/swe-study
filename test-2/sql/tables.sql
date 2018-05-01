/* creating tables */

drop table if exists Student /* guarantees no conflicts creating table */
drop table if exists Apply   /*   remove what already exists */

create table Student (
  sID   int not null, /* integer ID, cannot be null */
  sName text,
  GPA   float,
  primary key(sID),
)

create table Apply (
  sID   int,
  cName varchar(8),
  foreign key(sID) references Student(sID)
)

/* add values */
insert into Student values (123, "Amy", 4.0)
