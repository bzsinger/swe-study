// exceptions

const assert = require('assert')

try {
  throw new Error("abc")
  assert(false)
} catch(e) {                // runs if error is thrown - stored in e
  console.log("caught")
} finally {                 // runs whether or not error thrown
  console.log("finally")
}
