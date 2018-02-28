// array

let a = [2, 3, 4]

a === [2, 3, 4]     // false - === performs an identity check with objects
let _ = require('lodash')
_.isEqual(a, [2, 3, 4])
