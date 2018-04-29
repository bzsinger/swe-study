/* regular expressions */

/* assume tables:
Student
  sID     int not null, primary key
  sName   text
  GPA     float
*/

/* % - equivalent to .*, captures any number of characters */
select *
  from Student
  where sName like "%y" /* returns students whose names end in 'y'
                              - equivalent to '.*y' */

/* _ - equivalent to ., captures single character */
select *
  from Student
  where sName like "__y" /* returns students whose names are three letters long
                              and end in y
                              - equivalent to '..y' */
