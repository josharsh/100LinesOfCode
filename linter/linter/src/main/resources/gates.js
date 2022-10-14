function and(a,b) {
  if (a === 1 && b === 1) {
    return 1
  } else {
    return 0
  }
}

function or(a,b) {
  if (a === 1)
    return 1
  if (b === 1)
    return 1
  else
    return 0
}

function xor(a,b) {
  if (and(a,b))
    return 0;
  return or(a,b);
}

function not(a) {
  if (a === 0)
    return 1
  else
    return 0
}

function nand(a,b) {
  return not(and(a, b))
}

function nor(a,b) {
  return not(or(a,b))
}

function add1(a,b) {
  overflow = and(a,b)
  sum = xor(a,b)
  return {sum, overflow}
}

function zadd1(a,b,z) {
  var ones, zf;
  zf = or(or(and(a,b), and(b,z)), and(a,z));

  j = or(a, nor(b,z));
  k = or(b, nor(a,z))
  l = or(z, nor(a,b))

  console.log("jkl", j, k, l);

  ones = xor(j, xor(k, l));
  return {ones, zf};
}

// add1(0, 1)
// add2(00, 01)
// add4(0000, 1001)
// add8(10100000, 11001001)
function add2(a,b) {
  twos = add1(a[0], b[0])
  ones = add1(a[1], b[1]);

}


console.log("xor 00", xor(0,0))
console.log("xor 01", xor(0,1))
console.log("xor 10", xor(1,0))
console.log("xor 11", xor(1,1))
console.log()

console.log("nor 00", nor(0,0))
console.log("nor 01", nor(0,1))
console.log("nor 10", nor(1,0))
console.log("nor 11", nor(1,1))
console.log()

console.log("nand 00", nand(0,0))
console.log("nand 01", nand(0,1))
console.log("nand 10", nand(1,0))
console.log("nand 11", nand(1,1))
console.log()

console.log("add1 00", add1(0,0))
console.log("add1 01", add1(0,1))
console.log("add1 10", add1(1,0))
console.log("add1 11", add1(1,1))
console.log()

console.log("zadd1 000", zadd1(0, 0,0))
console.log("zadd1 001", zadd1(0, 0,1))
console.log("zadd1 010", zadd1(0, 1,0))
console.log("zadd1 011", zadd1(0, 1,1))
console.log("zadd1 100", zadd1(1, 0,0))
console.log("zadd1 101", zadd1(1, 0,1))
console.log("zadd1 110", zadd1(1, 1,0))
console.log("zadd1 111", zadd1(1, 1,1))