# Concepts

### Assertions
**Good for:**
- Preconditions
- Postconditions

**Not good for:**
- testing - assertions raise exceptions that stop all tests
  - better option: unit tests - continues running tests if one fails
- user error - exceptions provide better error messages
  - better option: exceptions

**Use:**
```python
assert <boolean statement>
```
Error gives filename, line, function name, assertion that failed. Traceback shows inciting call.

### Caching
**Memoization:** Remember old values

**Eager cache:** Calculate and cache values before reading input

**Lazy cache:** Calculate results for input values and cache

**Meta cache:** Hard-code values or heuristic values in code

### Testing
**Unit testing:** Test individual methods or parts of the solution

**Acceptance testing:** Test the entire solution – how the parts fit together.

### REPL - Read-Eval-Print Loop
A problem that reads and evaluates input continuously

### Adding to a Python list
```python
a = [2, 3, 4]
a += [5]
a = a + [5]
```
Adding to a Python list takes **amortized constant time.** Adding to the back of a list is not always a constant-time operation because if the list fills up, it has to be copied over to a new larger list – a linear-time operation. However, this gets balanced out by all of the constant-time additions we do.

**Adding to the front or inserting** into a list is a **linear-time** operation.

### Immutability in Python
| Type | Add/Remove | Change element values | Immutable? |
|:----:|:----------:|:---------------------:|:----------:|
| List |     ✅     |           ✅           |     ❌     |
| Tuple|     ❌     |           ❌           |     ✅     |
| Set  |     ✅     |     ❌ (keys)          |     ❌     |
| Frozen set  |  ❌ |     ❌ (keys)          |     ✅     |
| Dict |     ✅     |     ❌ (keys)          |     ❌     |

## Functions
### Function communication to caller (without exceptions)
1. Return mechanism
2. Change the value of a global variable
3. Use a parameter (by reference)

None of these force you to pay attention. You may not notice a problem until you're far away from it.

**Exceptions force you to pay attention when a program stops.**

Exceptions can be raised at a deep level and get handled when necessary at the proper level.

### Types of Functions
**Named functions:**
```python
def f():
  pass
```
**Lambda functions:**
```python
f = lambda x, y : x + y
```
Unnamed, often used when wanting to pass a function to another function as a parameter

**Higher-order functions:**
```python
f(lambda x, y: x + y)
```
A function that either takes another function as an argument or returns a function. (ex. ```sort``` may take a comparison function)

## Recursion
Call to a function with itself. Functions that wait to do an operation before the recursive function returns will consume a stack.

```python
def f(n):
  ...
  return 3 + f(n - 1)
```

Many languages optimize "tail recursion." Python doesn't.

## Iteration
Does not consume a stack. Returns one value at a time. Allows multiple users to simultaneously iterate over a data structure.
