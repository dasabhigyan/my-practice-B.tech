// =========================================================
// PART 1: WORKING WITH API DATA (Objects & Arrays Revision)
// =========================================================
let data = {
  products: [
    { id: 26, title: "Green Chili Pepper", price: 0.99 },
    { id: 27, title: "Honey Jar", price: 6.99 },
    { id: 28, title: "Ice Cream", price: 5.49 },
    { id: 29, title: "Kiwi", price: 2.49 }
  ]
};

// Q2: Print every item with its price in INR (1 USD = 100 INR)
for (let i = 0; i < data.products.length; i++) {
  let item = data.products[i];
  let priceInINR = Math.round(item.price * 100);
  console.log(`${item.title} : ${priceInINR}`);
}
// OUTPUT:
// Green Chili Pepper : 99
// Honey Jar : 699
// Ice Cream : 549
// Kiwi : 249

// Q3: Total price of all items in INR
let totalUSD = 0;
for (let i = 0; i < data.products.length; i++) {
  totalUSD += data.products[i].price;
}
console.log("Total in INR:", Math.round(totalUSD * 100));   // OUTPUT: Total in INR: 1596

// Q4: Find the item with the maximum price
let maxItem = data.products[0];
for (let i = 1; i < data.products.length; i++) {
  if (data.products[i].price > maxItem.price) {
    maxItem = data.products[i];
  }
}
console.log("Most expensive:", maxItem.title);              // OUTPUT: Most expensive: Honey Jar


// =========================================================
// PART 2: DESTRUCTURING (Unpacking values in one line)
// =========================================================

// 1. Object Destructuring (matches by EXACT KEY NAME)
const student = { name: "Ajay", age: 20, rollNumber: "2616400901" };
const { name, age, city } = student;

console.log(name, age);                                     // OUTPUT: Ajay 20
console.log(city);                                          // OUTPUT: undefined  (key 'city' doesn't exist)

// 2. Array Destructuring (matches by POSITION: 0, 1, 2...)
const fruits = ["Apple", "Banana", "Mango"];
const [first, second] = fruits;

console.log(first, second);                                 // OUTPUT: Apple Banana

// 3. Destructuring is NOT a Deep Copy
const course = { title: "Web Dev", topics: ["HTML", "CSS"] };
let { title, topics } = course;

title = "Full Stack";   // Plain string -> copied by VALUE (original unchanged)
topics.push("JS");      // Array -> copied by REFERENCE (original ALSO changes!)

console.log(course);                                        // OUTPUT: { title: "Web Dev", topics: ["HTML", "CSS", "JS"] }
console.log(topics === course.topics);                      // OUTPUT: true  (both point to the exact same array)


// =========================================================
// PART 3: COMPARING OBJECTS (== vs ===)
// =========================================================
const s1 = { name: "Ajay" };
const s2 = { name: "Ajay" };
const s3 = s1;          // s3 points to the exact same memory address as s1

console.log(s1 === s2);                                     // OUTPUT: false  (two different objects in memory)
console.log(s1 === s3);                                     // OUTPUT: true   (same object in memory)
console.log([1, 2] === [1, 2]);                             // OUTPUT: false  (two different arrays in memory)

// Loose (==) vs Strict (===) with primitives
console.log([5] == 5);                                      // OUTPUT: true   (== converts [5] -> "5" -> 5)
console.log([5] === 5);                                     // OUTPUT: false  (=== checks type too: array !== number)


// =========================================================
// PART 4: INTRODUCING FUNCTIONS
// =========================================================

// Defining a function (nothing prints yet)
function printPrice(item, usd) {
  console.log(`${item} : ${Math.round(usd * 100)}`);
}

// Calling the function
printPrice("Honey Jar", 6.99);                              // OUTPUT: Honey Jar : 699
printPrice("Kiwi", 2.49);                                   // OUTPUT: Kiwi : 249

// console.log() inside a function gives back 'undefined'
function addWithoutReturn(a, b) {
  console.log(a + b);
}
let res1 = addWithoutReturn(2, 3);                          // OUTPUT: 5
console.log(res1);                                          // OUTPUT: undefined
console.log(res1 * 2);                                      // OUTPUT: NaN  (undefined * 2)

// 'return' sends the value back AND stops the function
function sumWithReturn(a, b) {
  return a + b;
  console.log("Never runs");
}
let res2 = sumWithReturn(10, 20);                           // (nothing printed yet, 30 is stored in res2)
console.log(res2);                                          // OUTPUT: 30
console.log(res2 * 2);                                      // OUTPUT: 60

// Reusable helper function
function toINR(usd) {
  return Math.round(usd * 100);
}
console.log("Kiwi in INR:", toINR(2.49));                   // OUTPUT: Kiwi in INR: 249


// =========================================================
// PART 5: ARGUMENTS, PARAMETERS & DEFAULT VALUES
// =========================================================
function introduce(name, city) {
  console.log(`${name} lives in ${city}`);
}
introduce("Ajay");                                          // OUTPUT: Ajay lives in undefined
introduce("Ajay", "Pune", "India");                         // OUTPUT: Ajay lives in Pune  ("India" is ignored)

// Default Value (triggers ONLY for missing argument or undefined)
function welcome(name = "Guest") {
  console.log(`Welcome, ${name}!`);
}
welcome("Ravi");                                            // OUTPUT: Welcome, Ravi!
welcome();                                                  // OUTPUT: Welcome, Guest!
welcome(undefined);                                         // OUTPUT: Welcome, Guest!
welcome(null);                                              // OUTPUT: Welcome, null!  (null skips the default)
```[cite: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]