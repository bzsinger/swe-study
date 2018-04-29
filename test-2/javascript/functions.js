// defaults

function f(x, y, z=3) {   // if no argument passed in for z, uses value 3
    return [x, y, z]
  return [x, y, z];
}

f(1, 2, 4)  // [1, 2, 4]
f(1, 2)     // [1, 2, 3]

// middle argument
function g(x, y=3, z) {  // in JavaScript, middle argument can have default
    return [x, y, z]
  return [x, y, z];
}

g();        // [undefined, 5, undefined]
g(1, 2, 4); // [1, 2, 4]
g(1, 2);    // [1, 2, undefined]
g(1);       // [1, 3, undefined]

// mutables
function h(x=[]) {      // uses a new array each time
  x.push(2);
}

h();        // [2]
h();        // [2]
