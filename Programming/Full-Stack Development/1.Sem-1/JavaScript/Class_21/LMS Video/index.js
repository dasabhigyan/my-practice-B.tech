//------------------------------WHILE LOOP------------------------------

// let i = 1;                           // Initialization
// console.log("Start")
// while (i < 11 ) {                    // Check Condition
//     console.log(i);                  // logic 
//     i++;                             // increment (change)
// }
// console.log("End")

// ---------------------------------DO-WHILE LOOP-------------------------

// let i = 5;                             // Initialization

// do{
//     console.log(i);                     // logic
//     i++;                                // increment
// }while(i<4);                            // check condition

// The difference between while loop and do while loop is 
// while loop checks the condion 1st then execute the code 
// do while loop execute 1st then checks the condition.
//------------------------------FOR LOOP--------------------------------

// here initialization; check contion; incrementation, then {logic} all in one line in for loop 
// for (i = 1; i<11; i++) {
//     console.log(i)
// };

//-------------------------------------------------------------------------

// Here is a Question where to know that the users DOB is a Leap year or not:

let userDOB = Number(prompt("Which year were you born?"));

let cnt = 0

for( i = userDOB; i <= 2026; i++){
    if( i%4 === 0){
        console.log(`${i} is a leap year`)
        cnt++;
    }
}
console.log(`You have seen ${cnt} leap years.`)