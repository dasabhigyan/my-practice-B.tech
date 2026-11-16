console.log("JS is Loosely Typed and Dinamicly Typed")

a = 10;
b = 20;

console.log(a + b);    // log means printion on the console

console.warn (a + b);

console.error(a + b);


// var is very powerful --> bugs
// var userName = "Abhigyan";
// console.log(userName);
// var userName = "Diviyangshini";
// console.log(userName);
//----------------------------------------------------------
//VAR
// re-declaration is allowed
// re-assignment is allowed (changing the value is allowed)
//----------------------------------------------------------

// let userName = "Abhigyan";
// console.log(userName);
// userName = "Divyangshini";  
// console.log(userName);

//----------------------------------------------------------
//LET
// re-declaration is NOT allowed
// re-assignment is allowed (changing the value is allowed)
//----------------------------------------------------------

// const userName = "Abhigyan";
// console.log(userName);
// userName = "Divyangshini";
// console.log(userName);

//----------------------------------------------------------
//CONST
// re-declaration is NOT allowed
// re-assignment is NOT allowed

// NAMING CONSERVATION AND RULES
// 1.Use meaningfull names. isAllowed, getCategories
// 2.Use Camelcase
// 3. allowed character are: letter, digit, underscore(_), doller($)
// 4. must begin with letter/_/$   
// a. allowed: test_1, subjects_marks, $page, page$
// b. notAllowed: 1test, -marks, subject-marks
// 5. Cannot be reserved keyword 
// 6. variabel are case sensitive