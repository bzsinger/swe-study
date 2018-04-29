# what is the output of the following?

class A (BaseException) :
    pass

class B (A) : # child of A
    pass

def f (n) :
    if n == 2 :
        raise A()
    if n == 3 :
        raise B()

def g (n) :
    try :
        print("try", end = " ")
        f(n)
        print("body", end = " ")
    except A :
        print("except A", end = " ")
    except B :
        print("except B", end = " ")
    else :
        print("else", end = " ")
    finally :
        print("finally", end = " ")

def test1 () :
    g(1)

# -------------------------------------------------------

# what is the output of the following?

class A (BaseException) :
    pass

class B (A) : # child of A
    pass

def f (n) :
    if n == 2 :
        raise A()
    if n == 3 :
        raise B()

def g (n) :
    try :
        print("try", end = " ")
        f(n)
        print("body", end = " ")
    except A :
        print("except A", end = " ")
    except B :
        print("except B", end = " ")
    else :
        print("else", end = " ")
    finally :
        print("finally", end = " ")

def test2 () :
    g(2)

# -------------------------------------------------------

# what is the output of the following?

class A (BaseException) :
    pass

class B (A) : # child of A
    pass

def f (n) :
    if n == 2 :
        raise A()
    if n == 3 :
        raise B()

def g (n) :
    try :
        print("try", end = " ")
        f(n)
        print("body", end = " ")
    except A :
        print("except A", end = " ")
    except B :
        print("except B", end = " ")
    else :
        print("else", end = " ")
    finally :
        print("finally", end = " ")

def test3 () :
    g(3)
