// yield

function* arr_iterator(arr) {   // function* to use yield in a function
  for (let k of arr) {
    yield k
  }
}

let g = arr_iterator([2, 3, 4])
g === g[Symbol.iterator]()            // true -
                                      //  using 'yield' gives us a free iterator
g.next()                              // {"value": 2, "done": false}
g.next()                              // {"value": 3, "done": false}
g.next()                              // {"value": undefined, "done": true}
