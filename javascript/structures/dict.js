// dictionary

let d = {2: "abc", 3: "def", 4: "ghi"}

d === {2: "abc", 3: "def", 4: "ghi"}     // false - === performs an identity check with objects
let _ = require('lodash')
_.isEqual(d, {2: "abc", 3: "def", 4: "ghi"})
