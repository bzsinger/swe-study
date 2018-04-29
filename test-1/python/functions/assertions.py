"""
Assertions
Good for:
- Preconditions
- Postconditions

Not good for:
- testing - assertions raise exceptions that stop all tests
  - better option: unit tests - continues running tests if one fails
- user error - exceptions provide better error messages
  - better option: exceptions

Error gives filename, line, function name, assertion that failed. Traceback
shows inciting call.
"""

# assert <boolean statement>    # if it fails, raises AssertionError
