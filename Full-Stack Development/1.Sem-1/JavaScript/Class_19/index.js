//Q.18
// if (true) {
//     var a = "I am var";
//     let b = "I am let";              //("let" the value inside let stays inside the curly bracket)
//     console.log("Inside", a);
//     console.log("Inside", b);
// }
// console.log("Outside", a);
// console.log("Outside", b);

//Q.22
let firstName = 'Abhigyam';
let lastName = ' Das';              // manually Space needed.
console.log(firstName + lastName);  // CONCEPT: Concatenation
console.log(firstName + ' ' + lastName);    //Q23
console.log(firstName, lastName);           //Q23

// Q 24 and 25
let price = 28;
console.log('Total:' + price + 5);      //Total:285         This is because JavaScrpit reads from left to right at 1st the 1st var was a string so it treated as Concatenation.
console.log(price + 5 + 'total');       //33total           This is because JavaScript reads from left to right and the 1st var was a number so a math calculation happened.

//Q.26
let name = 'Abhigyan';
let item = 'Coffee';
console.log(`Hello ${name}, your ${item} is ready!`);

//Q.29
console.log(5 === 5);
console.log(5 === '5');

//Q.30
console.log(5 == '5');

//Q.31
console.log(5 !== '5');
console.log(5 != '5');
