/* join */

/* assume tables:
Student
  sID     int not null, primary key
  sName   text
  GPA     float

Apply
  sID        int
  cName      varchar(8)
  major      varchar(255)
  decision   varchar(4)

  foreign key(sID) references Student(sID)
*/

/* ------------------------------------------------------------------------ */

/* cross join
    - input: table, table
    - output: table
*/

select *
  from Student
  cross join Apply
  order by Student.id

  /* takes every student, matches each row of Apply table to every student
        (even if matching doesn't make sense) */

/* if table A has x rows, and table B has y rows, A cross join B has
        x * y rows */

/* ------------------------------------------------------------------------ */

/* theta join
    - input: table, table, predicate (identify matching attributes)
    - output: table
*/

select *
  from Student
  inner join Apply
  on Student.sID = Apply.sID
  /* sets which attributes should be related in joins
        tolerates different field names (ex. if Student's id was named 'id') */

select *
  from Student
  inner join Apply (using sID)
  /* only usable if use same name for both fields */
  /* only returns rows that match */

/* if table A has x rows, and table B has y rows, A inner join B has
      at most max(x, y) rows */

/* ------------------------------------------------------------------------ */

/* natural join
    - takes: table, table
    - produces: table
*/

select *
  from Student
  natural join Apply
  /* joins on any matching field in both tables */

  /* if no attributes match, returns *cross join*
      if an attribute matches, returns only rows with matching values for those
        attributes */

/* ------------------------------------------------------------------------ */

/* right join
    - takes: table, table
    - produces: table
*/

select *
  from Student
  left join Apply on (Student.sID = Apply.sID)

/* includes values from left (Student) table even if Apply doesn't have
      matching values - uses NULL values as substitutes for missing values */

/* ------------------------------------------------------------------------ */

/* right join
    - takes: table, table
    - produces: table
*/

select *
  from Student
  right join Apply on (Student.sID = Apply.sID)

  /* includes values from right (Apply) table even if Student doesn't have
      matching values - uses NULL values as substitutes for missing values */


/* ------------------------------------------------------------------------ */

/* since join produces a table, can use 'where' to do a select and replace
      * with column names to do a project */

select sName, GPA
  from Student
  inner join Apply (using sID)
  where (GPA > 3.0) and
        (sID < 200)

/* can do multiple joins in single SQL statement */

select *
  from Student
    inner join Apply (using sID)
    inner join Apply (using cName)
  where
    (sizeHS > 1000)     and
    (major = "CS")      and
    (decision = "true") and
    (enrollment > 20000)

/* ------------------------------------------------------------------------ */

/* if doing self join, need to rename tables */

select R.cName, R.state
  from College as R
    inner join College as S
  where (R.cName != S.cName) and
        (R.state = S.state)
        /* only returns college if state has > 1 college */
