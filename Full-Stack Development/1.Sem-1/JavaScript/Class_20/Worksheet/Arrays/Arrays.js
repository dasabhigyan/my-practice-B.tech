// if you  know Python, this is JS version of a list.

//Q14
const fruitsArr = ["Mango", "Grapes"];
console.log(fruitsArr);

const fruitsObj = {
    0 : "Mango",
    1 : "Grapes"
};
console.log(fruitsObj);

console.log(typeof fruitsArr);
console.log(typeof fruitsObj);
// both the type of are "object", this is because in JavaScript an array is just a special type of object

//Q15
console.log(fruitsArr[0]);  ///Mango
console.log(fruitsArr[1]);  //Grapes
console.log(fruitsArr.length);  //2
console.log(fruitsArr[fruitsArr.length - 1]);   //Grapes

//Q16
console.log(fruitsArr[-1]);  // undefined negative indexing doesn't exits in JavaScript 

//Q17
fruitsArr[2] = "Apple";     //Adds another element in the array
console.log(fruitsArr);

//Q18
fruitsArr[20] = "Wtarmelon";
console.log(fruitsArr);
console.log(fruitsArr.length);  // The length is 21 (here it means that length does't tells the actual length like python, it tell the last index + the 0th index of the array, and the indexes between them is marked as empty, and when printed the value is ubdefined,(the empty slots are called as holes in an array.) )

//Q19
fruitsArr.unshift("Watermelon");   // Added the term watermelon to the very beginging of the array
fruitsArr.push("Banana")    //  adds the element in ths last of the array
console.log(fruitsArr)

//Q19 splice method
//array.splice(startIndex, deleteCount, item1, item2, ...);
// for adding watermelon 
fruitsArr.splice(0, 0, "Watermelon");   // This works just like unshift
fruitsArr.splice(fruitsArr.length, 0, "Banana"); // This works like push 
console.log(fruitsArr);

//Q20
fruitsArr.shift();  // Removes the 1st element from the array
fruitsArr.pop();    // Removes the last element from the array 
console.log(fruitsArr);

//20 splice method 
fruitsArr.splice(0, 1); // this works just like shift
fruitsArr.splice(fruitsArr - 1, 1); // this works just like pop
console.log(fruitsArr)

//Q21
delete fruitsArr[1];    // This removes the value, but it make  a hole at athat index
console.log(fruitsArr);
console.log(fruitsArr.length);

//Q22
fruitsArr[1] = "Orange";
console.log(fruitsArr);

//Q22 with splice method
fruitsArr.splice(1, 1, "Orange");
console.log(fruitsArr)


