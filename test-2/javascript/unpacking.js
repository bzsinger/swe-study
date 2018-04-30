/* unpacking */

function f(x, y, z) {
  return [x, y, z]
}

const a = [2, 3]
const b = [4]

f()           /* [undefined, undefined, undefined] */
f(...a)       /* [2, 3, undefined] */
f(...a, ...b) /* [2, 3, 4] */
