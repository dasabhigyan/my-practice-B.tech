// // This is an Object created with Object()
// // const studen1 = Object();
// // console.log(studen1);

// // This is an Object created with {}
// const student1 = {
//     name: "abhigyan",
//     age: "18",
//     city: "Delhi",
//     bloodGroup:"AB+",
//     name: "Divyangshini"    // cascading (you can't have reapted )
// };

// // keys should always be string or symbol
// // JavaScript will try to convert anything else to string equivalient
// // The key should be a vaild identifier or a string --> variable naming conventions

// console.log(student1);
// console.log(student1.name)

// const laptop = {
//     os: "Windows",
//     brand: "lenovo",
//     screenSize: "15 inch",
// };

// console.log(laptop);

// const   key = prompt("What do yo want to add:");
// console.log("Key:", key);

// const value = prompt(`what is the value for ${key}`);
// console.log("value:", value);

// // add a key and value pair Inside the Object:
// laptop[key] = value; 
// console.log(laptop);

// const laptop = {
//     os: "Windows",
//     brand: "lenovo",
//     screenSize: "15 inch",
//     ram: "16gb",
//     storage: "256gb",
//     battery: 69,
//     isOnpower: false,
// };

// key should always be string or symbol
// value can be anything 

// console.log(laptop);
// const val1 = prompt(`Do you want to change anything?`);
// const val2 = prompt(`What value you want to change in ${val1}`);

// laptop[val1] = val2; // this is for adding as well as updateing 
// // The value will change if key is present, OR a new key value pair will be inserted if the key is not present.


// console.log(laptop)
// console.log(laptop["os"]) //square bracket allows the use of dynamic key

// const val = prompt(`What do you want to know about my laptop?`);
// console.log(laptop[key]) //this give the value 
// console.log(laptop.key) // this gives the value as undefined 



//---------------------------------------------------------------------------------------------


//  const laptop = {
//     os: "Windows",
//     brand: "lenovo",
//     screenSize: "15 inch",
//     ram: "16gb",
//     storage: "256gb",
//     battery: 69,
//     isOnpower: false,
// };


// delete laptop.brand;

// const k = prompt(`What do you want to delete`)
// delete laptop[k]
// console.log(laptop)


//-----------------------------------------------------------------------------
const Abhigyan = {
    name: "Abhigyan", // this is a property
    age: 18, // this is a property
    isGraduated: false, // this is a property
    information: function abcd() { // this is a Method
        console.log("------------");
    }
};
console.log("Das", Abhigyan); // printing a string and the object in the same line 

Abhigyan.information();
// Important: in arrow function the indicats the parent block 
    //  infoemation: () => {}
// The function () the 