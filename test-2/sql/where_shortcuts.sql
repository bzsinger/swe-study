/* assume tables:
Student
  sID     int not null, primary key
  sName   text
  GPA     float
*/

/* ------------------------------------------------------------------------ */

/* in */
select *
  from Student
  where sName in ("Amy", "Jay", "Mary")
                          /* returns students with those exact names */

/* equivalent to */

select *
  from Student
  where sName = "Amy" or sName = "Jay" or sName = "Mary"

/* ------------------------------------------------------------------------ */

/* between */
select *
  from Student
  where sID between 50 and 150
              /* (50, 150) - exclusive */

/* equivalent to */

select *
  from Student
  where sID > 50 and sID < 150
