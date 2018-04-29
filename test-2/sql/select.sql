/* select */

/*
select
    - takes: table, predicate
    - produces: table

- returns full row for every entry that matches predicate
*/


/* assume tables:
Student
  sID     int not null, primary key
  sName   text
  GPA     float


Apply
  sID     int
  cName   varchar(8)

  foreign key(sID) references Student(sID)

*/

select *
  from Student
  where (GPA > 3.7)

select *
  from Student
  where (GPA > 3.7) and (sID > 100)
  /* can use standard boolean operations */
