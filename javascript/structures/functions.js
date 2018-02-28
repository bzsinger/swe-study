// functions

function f() {    // normal function

}

let g = () => {}  // arrow function

function h() {
  function i() {  // function within a function
    console.log("inner function")
  }

  console.log("outer function")
  i()
}

h()               // outer function
                  // inner function

function j(k, l) {
  this.k = k
  this.l = l
}

// j()              // error - no 'this'

let m = new j(2, 3) // now j has a 'this'

m.k === 2
m["k"] === 2

m.l === 3
m["l"] === 3
