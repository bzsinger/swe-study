// types

class A { }
let a = new A()
typeof a          // object
a instanceof A

typeof 3          // number

typeof "a"        // string

typeof [2, 3, 4]  // object
[2, 3, 4] instanceof Array
[2, 3, 4] instanceof Object

typeof null       // object

let x
typeof x          // undefined

function f() { }
typeof f          // function

let g = () => {}  // arrow function
typeof g          // function
