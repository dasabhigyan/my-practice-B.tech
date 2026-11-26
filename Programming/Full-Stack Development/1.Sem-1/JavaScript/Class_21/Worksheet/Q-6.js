
// Main Task-1 : Prompt & console.log basic:

let name = prompt("What is your Name?");    // prompt is eqivalent to input in python.
console.log(name);

// Main Task-2 : Rewrie with Tamplate Literal

console.log(`Hello, ${name}`);


//---------------------Concept - prompt(): Always Returns a String.-------------
// 1. parseInt(str) ---> praseInt("42px") -> 42
// 2. parseFloat(str) ---> parseFloat("3.14 kg") -> 3.14
// 3. Number(str) ---> Number("42") -> 42 but Number("42px") -> NaN
//--------------------------------------------------------------------------

// Main Task-3 : Converting the prompt input into number
let ageInput = prompt("How old are you?");
let age = parseInt(ageInput);
console.log(`Next year you'll be ${age+1}`);