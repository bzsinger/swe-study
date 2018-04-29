/* project */

/*
project
    - takes: table, list of attributes (column names)
    - produces: table

- returns requested columns from given table
*/


/* assume tables:
Student
  sID        int not null, primary key
  sName      text
  GPA        float


Apply
  sID        int
  cName      varchar(8)
  major      varchar(255)
  decision   varchar(4)

  foreign key(sID) references Student(sID)

*/

select sID, cName
  from Apply

select major, decision
  from Apply
  order by major /* orders results alphabetically by major */
  limit 5        /* only returns first 5 results */

/* distinct - gets rid of duplicate rows in results */
select distinct major, decision
  from Apply
  order by major desc /* orders results in descending alphabetical order
                            by major
                      */

/* syntax
select (opt. distinct) (columns separated by ',') from (table)
  where (boolean conditions joined by 'or' or 'and') order by (ex. desc) limit (number)
*/
