# Algebra

**Has:**
 - set of elements
 - set of operations

**Can be:**
 - closed - only produces elements of element type
 - open - may produce elements of other types

 ex.
  - elements=integers
  - operations=addition
  - **Closed** (only produces elements of type integer)

# Relational Algebra
  - set of elements: relations (tables)
  - set of operations: select, project, joins

## Structured Query Language (SQL)
  - declarative language
    - say what you want, not how to get it

### Terms
  - foreign key - connect multiple tables

ex.
```
title         year    director          genre
"shane"       1953    "george stevens"  western
"star wars"   1977    "george lucas"    western
```
- move directors to new table, because multiple movies per director
- replace director name with ```id``` of director
  - id - **primary key** of directors table, **foreign key** of movies table
- order of filling in tables important because we need to reference directors within movies

```
title         year    director    genre
"shane"       1953    1           western
"star wars"   1977    2           western

director table:
id    name
1     "george stevens"
2     "george lucas"
```
