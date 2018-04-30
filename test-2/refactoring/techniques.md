# Refactoring

## Methods
- extract method (110)
  - take complicated code out of a method, turn it into its own method

- move method (142)
  - move method to a class it's better suited to be in

- temp with query (120)
  - call method multiple times instead of storing it in a local variable
  - can be expensive and may have side effects, but it makes the code more readable
    - as long as the timing difference is not substantial, clarity of code outweighs the difference

- other
  - if calling a getter over and over again, should feed information in as a parameter

## Class Relationships
- inheritance (is-a)
  - reuse implementation (can't change parents)
  - reuse interface

- container (has-a)
  - reuse implementation (can change what you contain)
