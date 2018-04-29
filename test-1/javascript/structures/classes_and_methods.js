// class
class A {
    // function definition
    f() { }       // methods  - functions that belong to a class -
                  //  do not need the 'function' keyword
}

function g () { } // functions outside of classes need the 'function'
                  //  keyword

// dynamically typed
x = new A()       // need the 'new' keyword when constructing an object
y = new A()
z = new A()

z instanceof A    // true - instanceof only works for objects

/*********************************************************/

class B {
  constructor (a, b) {  // class constructor
    this.a = a
    this.b = b
  }
}

let b = new B(2, 3)   // need 'new' keyword to create new instance
b.a === 2             // access instance variables
b["a"] === 2
b.b === 3
b["b"] === 3
