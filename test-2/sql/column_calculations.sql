/* assume tables:
Student
  sID     int not null, primary key
  sName   text
  GPA     float
*/

/* ------------------------------------------------------------------------ */

/* count - returns number of non-null rows
    produces single value, can't use for projection */
select count(sName)
  from Student

/* min - returns the minimum value of the column */
select min(sID)
  from Student

/* max - returns the maximum value of the column */
select max(sID)
  from Student

/* avg - returns the average value of the column */
select avg(GPA)
  from Student

/* ------------------------------------------------------------------------ */

/* group by */

select min(sID)
  from Student
  group by sName
  /* does min on a per-group basis - condenses all of same name into a group */

select min(sID)
  from Student
  group by sName
  having count(*) >= 2
  /* only includes results from names shared by at least 2 students */
