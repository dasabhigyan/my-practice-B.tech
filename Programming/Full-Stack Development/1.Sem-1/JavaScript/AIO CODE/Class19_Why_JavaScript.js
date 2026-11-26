// =========================================================
// CLASS 19: WHY JAVASCRIPT? (Console, Variables, Math & Data)
// =========================================================

// =========================================================
// PART 1 & 2: WHY JAVASCRIPT? & THE CONSOLE
// =========================================================
// HTML = Structure (buttons, text)
// CSS  = Style (colors, layout, hover effects)
// JS   = Brain/Interactivity (making "Add to Cart" actually update the count!)

// Typing math directly in the console evaluates it immediately:
console.log(5 + 3);                                         // OUTPUT: 8


// =========================================================
// PART 3 & 4: VARIABLES & DOING MATH
// =========================================================
let price = 10;                                             // Stores 10 under the name 'price'
console.log(price);                                         // OUTPUT: 10

price = 20;                                                 // Reassigns 'price' to a new value
console.log(price);                                         // OUTPUT: 20

// Basic Math Operators
console.log(10 + 3);                                        // OUTPUT: 13
console.log(10 - 3);                                        // OUTPUT: 7
console.log(10 * 3);                                        // OUTPUT: 30
console.log(10 / 3);                                        // OUTPUT: 3.3333333333333335 (JS uses decimals)
console.log(10 % 3);                                        // OUTPUT: 1  (% is Modulus -> gives the REMAINDER)


// =========================================================
// PART 5: DATATYPES (7 Primitives + 1 Non-Primitive)
// =========================================================
// Primitives (7): string, number, boolean, undefined, null, bigint, symbol
// Non-Primitive (1): object

console.log(typeof 'Alex');                                 // OUTPUT: string
console.log(typeof 21);                                     // OUTPUT: number
console.log(typeof true);                                   // OUTPUT: boolean


// =========================================================
// PART 6: LINKING JS TO HTML (<script> tag)
// =========================================================
// Inline:   <script>console.log("Hello!");</script>        (Right before </body>)
// External: <script src="script.js"></script>              (Best practice: keeps HTML & JS clean and separate)


// =========================================================
// PART 7: var vs let vs const
// =========================================================
// 1. Redeclaration
var x = 5;
var x = 10;                                                 // var ALLOWS redeclaring (causes bugs!)
console.log(x);                                             // OUTPUT: 10

let y = 5;
// let y = 10;                                              // OUTPUT: SyntaxError (let blocks redeclaring)

// 2. Block Scope (inside { })
if (true) {
  var a = "I'm var";
  let b = "I'm let";
  console.log("inside:", a);                                // OUTPUT: inside: I'm var
  console.log("inside:", b);                                // OUTPUT: inside: I'm let
}
console.log("outside:", a);                                 // OUTPUT: outside: I'm var  (var leaks out of { }!)
// console.log("outside:", b);                              // OUTPUT: ReferenceError: b is not defined (let stays inside)

// 3. Using before declaring (Hoisting)
console.log(hoistedVar);                                    // OUTPUT: undefined  (var silently gives undefined)
var hoistedVar = 5;

// console.log(hoistedLet);                                 // OUTPUT: ReferenceError: Cannot access before initialization
let hoistedLet = 5;

// GOLDEN RULES:
// - Avoid 'var'.
// - Default to 'const' (locked value). Use 'let' ONLY if the value needs to change.
// - Use camelCase for names: productPrice, cartTotal, isLoggedIn.


// =========================================================
// PART 8: STRINGS (Concatenation vs Template Literals)
// =========================================================
let firstName = 'Nikhil';
let lastName = 'Bhatt';

// Concatenation (+) glues strings together with NO automatic space
console.log(firstName + lastName);                          // OUTPUT: NikhilBhatt
console.log(firstName + ' ' + lastName);                    // OUTPUT: Nikhil Bhatt  (you added the space)
console.log(firstName, lastName);                           // OUTPUT: Nikhil Bhatt  (console.log adds a space)

// Left-to-Right Trap with +
let itemPrice = 28;
console.log('Total: ' + itemPrice + 5);                     // OUTPUT: Total: 285    (string + 28 -> "Total: 28" + 5 -> "Total: 285")
console.log(itemPrice + 5 + ' total');                      // OUTPUT: 33 total      (28 + 5 = 33, then glued to ' total')

// Template Literals (Backticks ` ` and ${ }) -> The clean modern way!
let userName = 'Chaitanya';
let item = 'coffee';
console.log(`Hello ${userName}, your ${item} is ready!`);   // OUTPUT: Hello Chaitanya, your coffee is ready!
console.log(`Total: ${itemPrice + 5}`);                     // OUTPUT: Total: 33     (Math inside ${ } runs first!)


// =========================================================
// PART 9: CONDITIONALS (=== vs ==)
// =========================================================
// Strict Equality (=== and !==): Checks BOTH Value AND Datatype (ALWAYS USE THIS)
console.log(5 === 5);                                       // OUTPUT: true   (same value, both are numbers)
console.log(5 === '5');                                     // OUTPUT: false  (number !== string)
console.log(5 !== '5');                                     // OUTPUT: true   (they are strictly NOT equal)

// Loose Equality (== and !=): Converts types behind the scenes (AVOID THIS)
console.log(5 == '5');                                      // OUTPUT: true   (converts '5' to 5 first)
console.log(5 != '5');                                      // OUTPUT: false  (thinks 5 and '5' are equal)
