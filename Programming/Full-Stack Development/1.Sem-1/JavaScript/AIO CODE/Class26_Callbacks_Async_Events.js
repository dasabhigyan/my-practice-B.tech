// =========================================================
// CLASS 26: CALLBACKS, ASYNC, EVENT LOOP & EVENTS
// =========================================================

// =========================================================
// PART 1: CALLBACKS & HIGHER-ORDER FUNCTIONS (HoF)
// =========================================================

// Q1: Functions are values (can be stored in variables without calling them)
function sayHello() {
  console.log("Hello!");
}
const greet = sayHello;                                     // No () -> stores the FUNCTION itself, not its result
console.log(greet);                                         // OUTPUT: [Function: sayHello]
greet();                                                    // OUTPUT: Hello!

// Q2: Function Expression (anonymous function stored in a const)
// sayBye();                                                // OUTPUT: ReferenceError (const is in TDZ! Unlike 'function sayHello()')
const sayBye = function () {
  console.log("Bye!");
};
sayBye();                                                   // OUTPUT: Bye!

// Q3 & Q4: Higher-Order Function (calculate) & Callbacks (add, multiply, subtract)
function add(a, b) {
  return a + b;
}
function multiply(a, b) {
  return a * b;
}
function subtract(a, b) {                                   // Q4
  return a - b;
}

// 'calculate' is a Higher-Order Function because it takes a function ('operation') as an argument
function calculate(a, b, operation) {
  return operation(a, b);
}

console.log(calculate(4, 5, add));                          // OUTPUT: 9   (operation holds 'add')
console.log(calculate(4, 5, multiply));                     // OUTPUT: 20  (operation holds 'multiply')
console.log(calculate(10, 3, subtract));                    // OUTPUT: 7   (Q4 check)

// Q5: TRAP -> Passing add() instead of add!
// console.log(calculate(4, 5, add()));                     // OUTPUT: TypeError: operation is not a function
// Why? add() runs IMMEDIATELY -> undefined + undefined = NaN, so you passed NaN instead of the function!

// Q6: Inline Anonymous Callback (no name needed when used only once)
console.log(calculate(2, 10, function (a, b) {
  return a ** b;                                            // 2 to the power of 10
}));                                                        // OUTPUT: 1024


// =========================================================
// PART 2: ASYNC CALLBACKS (setTimeout & setInterval)
// =========================================================
// Synchronous = runs line by line, waiting for each line to finish.
// Asynchronous = starts a timer/task now, runs its callback LATER without blocking.

// Q7: setTimeout(callback, ms) runs ONCE after 'ms' milliseconds
function printB() {
  console.log("B");
}
console.log("A");                                           // OUTPUT (1st): A
setTimeout(printB, 2000);                                   // Hands timer to browser, JS moves on immediately!
console.log("C");                                           // OUTPUT (2nd): C
                                                            // OUTPUT (3rd, after 2 seconds): B

// Q8: TRAP -> sayHi vs sayHi() inside setTimeout
function sayHi() {
  console.log("Hi!");
}
setTimeout(sayHi, 3000);                                    // OUTPUT (after 3 seconds): Hi!
// setTimeout(sayHi(), 3000);                               // OUTPUT (IMMEDIATELY!): Hi! (because () called it right away!)

// Q9: setInterval(callback, ms) runs REPEATEDLY every 'ms' milliseconds
/*
let tickCount = 0;
setInterval(function () {
  tickCount++;
  console.log("Tick " + tickCount);
}, 1000);
// OUTPUT: Tick 1 (1s), Tick 2 (2s), Tick 3 (3s)... until page is refreshed!
*/


// =========================================================
// PART 3: THE EVENT LOOP
// =========================================================
// Flow: Call Stack -> hands timer to Web APIs -> timer finishes -> Callback Queue
//       -> Event Loop moves callback to Call Stack ONLY when Call Stack is EMPTY!

// Q10: Even with 0 ms delay, B still prints AFTER C!
console.log("A");                                           // OUTPUT (1st): A
setTimeout(function () {
  console.log("B");
}, 0);                                                      // Goes to Web APIs -> Callback Queue -> waits for empty stack
console.log("C");                                           // OUTPUT (2nd): C
                                                            // OUTPUT (3rd): B  (runs after Call Stack is empty)

// Q11: Blocking the Call Stack delays async callbacks!
/*
console.log("A");                                           // OUTPUT (1st, 0s): A
setTimeout(() => console.log("B"), 1000);                   // Ready in Callback Queue at 1s, but MUST WAIT!
const start = Date.now();
while (Date.now() - start < 3000) {}                        // Keeps Call Stack busy for 3 full seconds
console.log("C");                                           // OUTPUT (2nd, ~3s): C
                                                            // OUTPUT (3rd, ~3s): B (finally runs once stack is empty!)
*/


// =========================================================
// PART 4: EVENTS (Reacting to User Actions)
// =========================================================
/* REQUIRED HTML (index.html <body>):
   <button onclick="increase()">Click me</button>
   <button onclick="resetCount()">Reset</button>
   <p id="msg">Clicked 0 times</p>
   <script src="./script.js"></script>
*/

let count = 0;

// Q12: Does NOT run on page load — the browser calls it ONLY when the user clicks the button!
function increase() {
  count++;
  const msg = document.getElementById("msg");
  msg.innerText = "Clicked " + count + " times";            // PAGE: Click 1 -> "Clicked 1 times", Click 2 -> "Clicked 2 times"
}

// Q13: Reset button handler
function resetCount() {
  count = 0;
  const msg = document.getElementById("msg");
  msg.innerText = "Clicked 0 times";                        // PAGE: Resets back to "Clicked 0 times"
}
