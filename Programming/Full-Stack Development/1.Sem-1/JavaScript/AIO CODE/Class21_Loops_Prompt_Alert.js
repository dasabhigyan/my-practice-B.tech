// =========================================================
// CLASS 21: LOOPS, PROMPT, PARSING & ALERT
// Note: Run Part 2 & Part 3 in a browser (linked to an HTML file)
// because prompt() and alert() are browser popups.
// =========================================================

// =========================================================
// PART 1: LOOPS (for, while, do-while)
// =========================================================

// 1. FOR LOOP: Use when you know EXACTLY how many times to run
//    (start; condition; update)
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
// OUTPUT: 1, 2, 3, 4, 5 (each on a new line)

// 2. WHILE LOOP: Use when you don't know how many times, just a condition
let w = 1;
while (w <= 5) {
  console.log(w);
  w++;                                                      // MUST update manually! Forgetting w++ causes an INFINITE LOOP
}
// OUTPUT: 1, 2, 3, 4, 5

// 3. DO-WHILE LOOP: Runs AT LEAST ONCE, then checks the condition at the end
let d = 10;
do {
  console.log(d);                                           // OUTPUT: 10 (runs once even though 10 < 5 is false!)
  d++;
} while (d < 5);


// =========================================================
// PART 2: PROMPT, PARSING & ALERT (Browser Popups)
// =========================================================

// Step 1 & 2: prompt() ALWAYS returns a STRING
let userName = prompt("What is your name?");                // Suppose user types: "Ajay"
console.log(`Hello, ${userName}!`);                         // OUTPUT: Hello, Ajay!

// Parsing functions (turning strings into numbers for math):
console.log(parseInt("42px"));                              // OUTPUT: 42    (whole number, stops at non-digits)
console.log(parseFloat("3.14 kg"));                         // OUTPUT: 3.14  (keeps decimals)
console.log(Number("42"));                                  // OUTPUT: 42
console.log(Number("42px"));                                // OUTPUT: NaN   (fails if ANY character isn't a number)

// Step 3: Converting prompt input to a number
let ageInput = prompt("How old are you?");                  // Suppose user types: "20"
console.log(ageInput + 1);                                  // OUTPUT: "201" (TRAP! String + number glues them together)
let age = parseInt(ageInput);                               // Converts "20" -> 20
console.log(`Next year you'll be ${age + 1}.`);             // OUTPUT: Next year you'll be 21.

// Step 4: do-while + prompt (Expense Calculator)
let expenseTotal = 0;                                       // Declare OUTSIDE the loop so it doesn't reset to 0!
let amount;
do {
  amount = prompt("Enter an expense (or type 'done'):");    // Suppose user enters: "100", "50.5", "done"
  if (amount !== "done") {
    expenseTotal += parseFloat(amount);
  }
} while (amount !== "done");
console.log(`Total expenses: ${expenseTotal}`);             // OUTPUT: Total expenses: 150.5

// Step 5: for loop + alert (3 Reminders)
for (let i = 1; i <= 3; i++) {
  alert(`Reminder ${i} of 3: Don't forget to water the plants!`);
}
// POPUPS:
// 1st popup: Reminder 1 of 3: Don't forget to water the plants!
// 2nd popup: Reminder 2 of 3: Don't forget to water the plants!
// 3rd popup: Reminder 3 of 3: Don't forget to water the plants!


// =========================================================
// PART 3: IMPLEMENTATION TASKS
// =========================================================

// TASK 1: Shopping Cart Total (do-while)
let cartTotal = 0;                                          // Declared OUTSIDE loop so it keeps adding up
let addMore;
do {
  let title = prompt("Item title?");                        // e.g. "Coffee", then "Sandwich"
  let price = parseFloat(prompt("Item price?"));            // e.g. "4.50",   then "8.00"
  cartTotal += price;
  console.log(`${title}: $${price} | Running total: $${cartTotal}`);
  addMore = prompt("Add another item? (yes/no)");           // e.g. "yes",    then "no"
} while (addMore !== "no");

alert(`Final total: $${cartTotal.toFixed(2)}`);
// CONSOLE OUTPUT:
// Coffee: $4.5 | Running total: $4.5
// Sandwich: $8 | Running total: $12.5
// POPUP: Final total: $12.50

// TASK 2: Average Score Calculator (for loop)
let count = parseInt(prompt("How many scores?"));           // parseInt -> count is a whole number (e.g. "3")
let scoreSum = 0;

for (let i = 1; i <= count; i++) {
  let score = parseFloat(prompt(`Score ${i}?`));            // parseFloat -> scores can have decimals (e.g. 90, 80, 78)
  scoreSum += score;
}

let average = scoreSum / count;
alert(`Average score is: ${average.toFixed(2)}`);           // POPUP: Average score is: 82.67
