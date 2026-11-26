const student = {
    name: "Abhigyan",
    city: "Delhi",
    college: "KRMU",
    rollNumber: "2616400193",
};
console.log(student);       // the whole object as output
console.log(typeof student);    // "object" as output

//Part-2

console.log(student.name);      // Abhigyan
console.log(student["city"]);   // Delhi
console.log(student.phone);     // value: undefined (a datatype)

student["country"] = "INDIA";   // adding a key value pair.
console.log(student);

student["city"] = "Balasore";
console.log(student);

student.college = "Zenith School of AI";    // editing the Key&Value pair, changing the variable.
console.log(student);

// student = {name = "Someone else"}; // This rises TypeError: Assignment to constant variable. as re-assignment is NOT allowed.

delete student["name"];
console.log(student)    // Removes the name key and its Value from the Object.

delete student.city;
console.log(student);   // removes the city key and its value from the Object(student).

const student2 = student;
student2.city = "Jaipur";

console.log(student);
console.log(student2);
// Did it create a secound object? No,It doesn't create a new object, it just created a secound name(referance)pointing to the same object in the memory
