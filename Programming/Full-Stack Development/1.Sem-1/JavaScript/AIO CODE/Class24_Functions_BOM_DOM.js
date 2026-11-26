// =========================================================
// CLASS 24: FUNCTIONS, EXECUTION CONTEXT, SCOPE, BOM & DOM
// =========================================================

// =========================================================
// PART 1: MEMORY, EXECUTION CONTEXT, HOISTING & SCOPE
// =========================================================
// Every Execution Context runs in 2 phases:
//   1. Memory Phase: scans code & reserves space:
//      - var       -> initialized as undefined
//      - let/const -> reserved in Temporal Dead Zone (TDZ) (cannot use yet)
//      - function  -> entire function definition is stored
//   2. Code Phase: runs line by line, assigning real values & executing calls.

// Q1: Execution Context & Call Stack Trace
console.log("----- START -----");                           // OUTPUT: ----- START -----
let a = 2;
var b = 3;
console.log(a, b);                                          // OUTPUT: 2 3

function multiplyByTwo(n) {
  console.log("----- INSIDE FUNCTION -----");               // OUTPUT: ----- INSIDE FUNCTION -----
  let result = n * 2;
  console.log("----- FUNCTION ABOUT TO RETURN RESULT -----"); // OUTPUT: ----- FUNCTION ABOUT TO RETURN RESULT -----
  return result;                                            // Returns 4 & immediately pops EC off Call Stack
  console.log("----- FUNCTION COMPLETED -----");            // NEVER PRINTS (unreachable after return!)
}

console.log("----- MID -----");                             // OUTPUT: ----- MID -----
let c = multiplyByTwo(a);                                   // Pushes multiplyByTwo(2) onto Call Stack
console.log(c);                                             // OUTPUT: 4
console.log("----- END -----");                             // OUTPUT: ----- END -----

// Q2: Hoisting with 'var'
console.log(x);                                             // OUTPUT: undefined  (hoisted in Memory Phase as undefined)
var x = 5;
console.log(x);                                             // OUTPUT: 5

// Q3: Hoisting with Function Declarations
sayHi();                                                    // OUTPUT: Hi!  (whole function is hoisted, so calling early works)
function sayHi() {
  console.log("Hi!");
}

// Q4: Temporal Dead Zone (TDZ) with 'let' / 'const'
// console.log(y);                                          // OUTPUT: ReferenceError: Cannot access 'y' before initialization
let y = 10;

// Q5: Lexical Scope (Inner code can see outer/global variables)
let college = "Zenith";
function intro() {
  console.log("I study at " + college);                     // Looks outside function & finds 'college'
}
intro();                                                    // OUTPUT: I study at Zenith

// Q6: Variable Shadowing (Local variable does NOT overwrite Global)
let city = "Pune";
function showCity() {
  let city = "Delhi";                                       // Separate local variable inside showCity
  console.log(city);                                        // OUTPUT: Delhi
}
showCity();
console.log(city);                                          // OUTPUT: Pune  (outer 'city' is untouched)

// Q7: Block Scope (let vs var inside { })
function printGrade(marks) {
  if (marks >= 50) {
    let grade = "Pass";                                     // Block-scoped: lives ONLY inside this if { }
    console.log(grade);                                     // OUTPUT: Pass
  }
  // console.log(grade);                                    // OUTPUT: ReferenceError (with 'var grade', this WOULD print "Pass")
}
printGrade(80);
// console.log(grade);                                      // OUTPUT: ReferenceError (even 'var' cannot escape a function!)


// =========================================================
// PART 2: THE BROWSER OBJECT MODEL (BOM)
// Note: Run Part 2 & Part 3 in a browser console / HTML page
// =========================================================
// 'window' is the browser's global object. Writing 'window.' is optional.

// Q8: window prefix is optional
window.console.log("Hi");                                   // OUTPUT: Hi
console.log("Hi");                                          // OUTPUT: Hi
// window.alert("Hello");                                   // Same as alert("Hello")

// Q9: prompt() return values
// let userName = prompt("Your name?");                     // Typing "Ajay" -> "Ajay" | Clicking Cancel -> null
// alert("Hello " + userName);                              // POPUP: "Hello Ajay" or "Hello null"

// Q10: location object (inspecting & changing the URL)
console.log(location.href);                                 // OUTPUT: Full URL (e.g. "http://127.0.0.1:5500/index.html")
console.log(location.hostname);                             // OUTPUT: Domain/host (e.g. "127.0.0.1")
console.log(location.pathname);                             // OUTPUT: Path (e.g. "/index.html")
console.log(location.search);                               // OUTPUT: Query string (e.g. "?id=5" or "")
// location.href = "https://zenithschool.ai";               // Navigates/redirects the browser tab to that URL

// Q11: document.title (browser tab title)
console.log(document.title);                                // OUTPUT: Current tab title (e.g. "Document")
document.title = "My Page";                                 // Changes the browser tab text to "My Page"


// =========================================================
// PART 3: THE DOCUMENT OBJECT MODEL (DOM)
// =========================================================
/* HTML required in index.html <body> for Part 3:
   <h1 id="title">My Shop</h1>
   <ul id="list">
     <li class="item">Pen</li>
     <li class="item">Notebook</li>
     <li class="item special">Bag</li>
   </ul>
   <p class="note">Prices in <b>INR</b></p>
*/

// Q12: Navigating DOM children
console.log(document.body.children);                        // OUTPUT: HTMLCollection [h1#title, ul#list, p.note, script]
console.log(document.body.children[0]);                     // OUTPUT: <h1 id="title">My Shop</h1>
console.log(document.body.children[1].children);            // OUTPUT: HTMLCollection [li.item, li.item, li.item.special]
console.log(document.body.children[1].children[0]);         // OUTPUT: <li class="item">Pen</li>

// Q13: getElementById vs getElementsByClassName
console.log(document.getElementById("title"));              // OUTPUT: <h1 id="title">My Shop</h1>  (single element)
console.log(document.getElementsByClassName("item"));       // OUTPUT: HTMLCollection(3) [li, li, li] (collection, length 3)

// Q14: querySelector vs querySelectorAll (uses CSS selectors: . for class, # for id)
console.log(document.querySelector(".item"));               // OUTPUT: <li class="item">Pen</li>     (FIRST match only)
console.log(document.querySelectorAll(".item"));            // OUTPUT: NodeList(3) [li, li, li]      (ALL matches)
console.log(document.querySelector("#list .special"));      // OUTPUT: <li class="item special">Bag</li>

// Q15: Changing CSS styles with JS (use camelCase: backgroundColor, not background-color)
const title = document.getElementById("title");
title.style.color = "crimson";                              // Page: heading text turns crimson
title.style.backgroundColor = "lightyellow";                // Page: heading background turns light yellow

// Q16: innerText vs innerHTML
const note = document.querySelector(".note");
console.log(note.innerText);                                // OUTPUT: "Prices in INR"         (plain visible text only)
console.log(note.innerHTML);                                // OUTPUT: "Prices in <b>INR</b>"  (includes HTML tags)

note.innerText = "Prices in <i>USD</i>";                    // Page shows literal text: Prices in <i>USD</i>
note.innerHTML = "Prices in <i>USD</i>";                    // Page renders HTML tag:   Prices in USD (with USD in italics)

// Q17: Loop over querySelectorAll & update heading using .length
const items = document.querySelectorAll(".item");
for (let i = 0; i < items.length; i++) {
  items[i].style.color = "blue";                            // Page: Pen, Notebook, Bag all turn blue
}
title.innerText = `My Shop (${items.length} items)`;        // Page: heading changes to "My Shop (3 items)"

// Q18: Creating & Attaching new elements
const newItem = document.createElement("li");               // Created in memory ONLY (not on page yet!)
newItem.innerText = "Eraser";
console.log(newItem);                                       // OUTPUT: <li>Eraser</li>

const parent = document.getElementById("list");
parent.appendChild(newItem);                                // NOW "Eraser" appears on the page at the end of the list!
