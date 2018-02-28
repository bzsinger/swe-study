// lodash

const _ = require('lodash')

// range
//   usage: _.range(<start>, <end>)
//   returns array containing values [start, end)
_.range(1, 5)               // returns [2, 3, 4] - **not** lazy

// reduce
//   usage: _.reduce(<iterable>, <function>, <seed>)
_.reduce(_.range(1, 5), (x, y) => { return x + y }, 0)  // returns 0 + 1 + ...
                                                        //    ... + 4 = 10
