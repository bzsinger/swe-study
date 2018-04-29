# exceptions

## all exceptions must extend BaseException
class MyException(BaseException):
    pass

# raise an exception
raise Exception('Stuff broke here')
raise

# handle an exception
try:
    # do stuff
    # <exception raised>   # jump to 'except' as soon as
    # other stuff          # exception raised
    pass
except StopIteration:      # runs if error is StopIteration
                           # or if the error is of a type
                           # that is a subclass of StopIteration

                           # always put child exception type
                           # before parent - otherwise only parent
                           # will run
    pass
except Exception as e:     # can have more than one except clause

    print(e.args)          # tuple of exception arguments
    pass
else:                      # only runs if **no exception raised**
    pass
finally:                   # **always runs** - even with unhandled
    pass                   # exception

# **only one** except clause will run - the **first** clause that
# might work
