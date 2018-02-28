// for loop

let a = [2, 3, 4]
for (let b in a) {        // returns 'keys' - a's indices - as strings
  typeof b === "string"   // order **not** guaranteed
  console.log(b);         // "0" "1" "2"
}

/********/

class A {
  constructor (a, b, c) {
    this.a = a
    this.b = b
    this.c = c
  }
}

let a = new A(1, 2, 3)

for (let n in a) {        // returns 'keys' - a's instance variables
  typeof n === "string"   // order **not** guaranteed
  console.log(n)          // "a" "b" "c"
}


/*********************************************************/

let a = [2, 3, 4]
for (let b of a) {        // returns values
  console.log(b)          // 2 3 4
}

/********/

class A {
  constructor (a, b, c) {
    this.a = a
    this.b = b
    this.c = c
  }
}

let a = new A(1, 2, 3)

// for (let n of a) {        // error - a is not iterable
//   typeof n === "string"   // see ./iterator.js
//   console.log(n)
// }
