// =========================================================
// CLASS 23: JAVASCRIPT FUNCTIONS PRACTICE
// =========================================================

// =========================================================
// PART 1: BASIC FUNCTION PRACTICE
// =========================================================

// Q1: Cube of a number
function cubeNumber(n) {
  return n * n * n;
}
console.log(cubeNumber(3));                                 // OUTPUT: 27

// Q2: Check if adult (1-line version works because >= already gives true/false)
function isAdult(age) {
  return age >= 18;
}
console.log(isAdult(18));                                   // OUTPUT: true
console.log(isAdult(17));                                   // OUTPUT: false

// Q3: Local Variables (Scope)
function calculateBMI(weight, height) {
  let bmi = weight / (height * height);                     // 'bmi' ONLY exists inside this function
  return bmi;
}
console.log(calculateBMI(70, 1.75));                        // OUTPUT: 22.857142857142858
// console.log(bmi);                                        // OUTPUT: ReferenceError: bmi is not defined

// Q4: Multiple return statements (once a return runs, the function stops!)
function gradeFromMarks(marks) {
  if (marks >= 90) return "A";
  if (marks >= 75) return "B";
  if (marks >= 50) return "C";
  return "F";
}
console.log(gradeFromMarks(90), gradeFromMarks(89));        // OUTPUT: A B
console.log(gradeFromMarks(75), gradeFromMarks(74));        // OUTPUT: B C
console.log(gradeFromMarks(50), gradeFromMarks(49));        // OUTPUT: C F

// Q5: Default parameter (10% discount for members)
function applyDiscount(price, isMember = false) {
  if (isMember) {
    return price * 0.9;                                     // 10% off
  }
  return price;
}
console.log(applyDiscount(500));                            // OUTPUT: 500
console.log(applyDiscount(500, true));                      // OUTPUT: 450

// Q6: Count lowercase vowels using a loop
function countVowels(word) {
  let count = 0;
  for (let i = 0; i < word.length; i++) {
    let ch = word[i];
    if (ch === "a" || ch === "e" || ch === "i" || ch === "o" || ch === "u") {
      count++;
    }
  }
  return count;
}
console.log(countVowels("banana"));                         // OUTPUT: 3


// =========================================================
// PART 2: FUNCTIONS INSIDE FUNCTIONS & CALL STACK
// =========================================================

// Q7: Combining helper functions
function square(n) {
  return n * n;
}
function cube(n) {
  return n * n * n;
}
function sumOfSquareAndCube(n) {
  return square(n) + cube(n);
}
console.log(sumOfSquareAndCube(3));                         // OUTPUT: 36  (9 + 27)

// Q8: CALL STACK TRACE for sumOfSquareAndCube(3)
// Think of a stack of plates — Last In, First Out!
//   Step 1: [ GEC ]                                        -> Script starts
//   Step 2: [ GEC, sumOfSquareAndCube(3) ]                 -> sumOfSquareAndCube is called (pushed)
//   Step 3: [ GEC, sumOfSquareAndCube(3), square(3) ]      -> square(3) is called (pushed)
//   Step 4: [ GEC, sumOfSquareAndCube(3) ]                 -> square(3) returns 9 and pops off
//   Step 5: [ GEC, sumOfSquareAndCube(3), cube(3) ]        -> cube(3) is called (pushed)
//   Step 6: [ GEC, sumOfSquareAndCube(3) ]                 -> cube(3) returns 27 and pops off
//   After that: sumOfSquareAndCube adds 9 + 27 = 36, returns 36, pops off, leaving [ GEC ],
//   and finally GEC pops off when the script finishes -> [ Empty stack ].

// Q9: Safe Square Root using helper functions
function isPositive(n) {
  return n >= 0;
}
function absoluteValue(n) {
  return n < 0 ? -n : n;                                    // Turns negative into positive (e.g., -16 -> 16)
}
function safeSquareRoot(n) {
  if (isPositive(n)) {
    return Math.sqrt(n);
  }
  return Math.sqrt(absoluteValue(n));
}
console.log(safeSquareRoot(16));                            // OUTPUT: 4
console.log(safeSquareRoot(-16));                           // OUTPUT: 4


// =========================================================
// PART 3: FUNCTIONS + ARRAYS & OBJECTS
// =========================================================

// Q10: Find the largest number in an array (without Math.max)
function findMax(numbers) {
  let max = numbers[0];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
  }
  return max;
}
console.log(findMax([4, 19, 7, 12]));                       // OUTPUT: 19

// Q11: Sum all prices in an array of product objects
const products = [
  { title: "Pen", price: 10 },
  { title: "Notebook", price: 45 },
  { title: "Bag", price: 500 }
];

function totalPrice(products) {
  let total = 0;
  for (let i = 0; i < products.length; i++) {
    total += products[i].price;
  }
  return total;
}
console.log(totalPrice(products));                          // OUTPUT: 555
