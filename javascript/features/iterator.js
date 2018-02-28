// iterator

class MyYieldIterator {
  constructor(start, end) {
    this.start = start
    this.end = end
  }

  [Symbol.iterator]() {         // implement this function to make the class
    return this                 //  iterable
  }

  next() {
    let ret = {                         // iterator returns object with 'value'
      "value": this.start,
      "done": (this.start >= this.end)  // and 'done' boolean
    }
    this.start += 1
    return ret
  }
}

let a = new MyYieldIterator(1, 3)
a === p[Symbol.iterator]()      // true - pointing to the same object
a.next()                        // {"value": 1, "done": false}
a.next()                        // {"value": 2, "done": false}
a.next()                        // {"value": 3, "done": true}
