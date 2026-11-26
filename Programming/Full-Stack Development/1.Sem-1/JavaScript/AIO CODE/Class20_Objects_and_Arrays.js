// =========================================================
// CLASS 20: OBJECTS & ARRAYS (CRUD Operations)
// =========================================================

// =========================================================
// PART 1: OBJECTS (Grouping related data under one name)
// =========================================================
// Instead of 4 separate variables, put all student details in ONE object (like a Python dictionary)
const student = {
  name: "Likhilesh",
  city: "Delhi",
  college: "KRMU",
  rollNumber: "2616400901"
};

console.log(student);                                       // OUTPUT: { name: "Likhilesh", city: "Delhi", college: "KRMU", rollNumber: "2616400901" }
console.log(typeof student);                                // OUTPUT: object


// =========================================================
// PART 2: CRUD ON OBJECTS (Create, Read, Update, Delete)
// =========================================================

// 1. READ (Dot notation vs Bracket notation)
console.log(student.name);                                  // OUTPUT: Likhilesh
console.log(student["city"]);                               // OUTPUT: Delhi  (bracket notation works like Python)
console.log(student.phone);                                 // OUTPUT: undefined  (missing key gives undefined, NOT an error)

// 2. CREATE & UPDATE (Same syntax! New key = Create, Existing key = Update)
student["country"] = "INDIA";                               // Creates a new key 'country'
student["city"] = "Mumbai";                                 // Updates existing key 'city'
student.college = "Zenith School of AI";                    // Updates existing key 'college'
console.log(student);                                       // OUTPUT: { name: "Likhilesh", city: "Mumbai", college: "Zenith School of AI", rollNumber: "2616400901", country: "INDIA" }

// Note on 'const': You CAN change properties inside a const object,
// but you CANNOT replace the whole variable:
// student = { name: "Someone Else" };                      // OUTPUT: TypeError: Assignment to constant variable

// 3. DELETE
delete student["name"];
delete student.city;
console.log(student);                                       // OUTPUT: { college: "Zenith School of AI", rollNumber: "2616400901", country: "INDIA" }

// 4. COPY BY REFERENCE (Not a real copy!)
const student2 = student;                                   // Both names point to the EXACT SAME object in memory
student2.city = "Jaipur";
console.log(student.city);                                  // OUTPUT: Jaipur  (original changed too!)
console.log(student2.city);                                 // OUTPUT: Jaipur

// Q13: Quick CRUD example on a 'car' object
const car = { brand: "Toyota", model: "Corolla", year: 2020 }; // Create
console.log(car.model);                                        // OUTPUT: Corolla (Read)
car.year = 2024;                                               // Update
delete car.brand;                                              // Delete
console.log(car);                                              // OUTPUT: { model: "Corolla", year: 2024 }


// =========================================================
// PART 3: CRUD ON ARRAYS (Ordered lists, like Python lists)
// =========================================================
const fruitsArr = ["Mango", "Grapes"];
console.log(typeof fruitsArr);                              // OUTPUT: object  (an array is a special object with numbered keys 0, 1, 2...)

// 1. READ
console.log(fruitsArr[0]);                                  // OUTPUT: Mango
console.log(fruitsArr[1]);                                  // OUTPUT: Grapes
console.log(fruitsArr.length);                              // OUTPUT: 2
console.log(fruitsArr[fruitsArr.length - 1]);               // OUTPUT: Grapes  (last item)
console.log(fruitsArr[-1]);                                 // OUTPUT: undefined  (unlike Python, negative index does NOT work!)

// 2. ADDING BY INDEX & HOLES (Avoid skipping indexes!)
fruitsArr[2] = "Apple";
console.log(fruitsArr);                                     // OUTPUT: ["Mango", "Grapes", "Apple"]
// fruitsArr[20] = "Watermelon";                            // BAD! Creates 17 empty "holes" and makes length 21

// 3. ADDING & REMOVING WITH ARRAY METHODS (Safe way!)
fruitsArr.unshift("Watermelon");                            // Adds to START (like Python insert(0, x))
fruitsArr.push("Banana");                                   // Adds to END   (like Python append(x))
console.log(fruitsArr);                                     // OUTPUT: ["Watermelon", "Mango", "Grapes", "Apple", "Banana"]

fruitsArr.shift();                                          // Removes from START (Watermelon)
fruitsArr.pop();                                            // Removes from END   (Banana)
console.log(fruitsArr);                                     // OUTPUT: ["Mango", "Grapes", "Apple"]

// Why NOT use 'delete' on an array?
// delete fruitsArr[1];                                     // BAD! Leaves <1 empty item> hole & length stays 3

// 4. UPDATING AN EXISTING INDEX (Safe!)
fruitsArr[1] = "Orange";
console.log(fruitsArr);                                     // OUTPUT: ["Mango", "Orange", "Apple"]

// 5. SPLICE: One method to Delete, Create, and Update anywhere!
// Syntax: arr.splice(startIndex, deleteCount, itemToAdd1, itemToAdd2, ...)
fruitsArr.push("Grapes", "Watermelon");
console.log(fruitsArr);                                     // OUTPUT: ["Mango", "Orange", "Apple", "Grapes", "Watermelon"]

// Delete with splice
fruitsArr.splice(2, 1);                                     // At index 2, remove 1 item ("Apple")
console.log(fruitsArr);                                     // OUTPUT: ["Mango", "Orange", "Grapes", "Watermelon"]
fruitsArr.splice(1, 2);                                     // At index 1, remove 2 items ("Orange", "Grapes")
console.log(fruitsArr);                                     // OUTPUT: ["Mango", "Watermelon"]

// Create (Insert) with splice (deleteCount = 0)
fruitsArr.splice(1, 0, "Kiwi");                             // At index 1, remove 0, insert "Kiwi"
console.log(fruitsArr);                                     // OUTPUT: ["Mango", "Kiwi", "Watermelon"]
fruitsArr.splice(2, 0, "Guava", "Papaya");                  // At index 2, remove 0, insert "Guava", "Papaya"
console.log(fruitsArr);                                     // OUTPUT: ["Mango", "Kiwi", "Guava", "Papaya", "Watermelon"]

// Update (Replace) with splice (deleteCount = 1 + new item)
fruitsArr.splice(0, 1, "Pineapple");                        // At index 0, remove 1 ("Mango"), insert "Pineapple"
console.log(fruitsArr);                                     // OUTPUT: ["Pineapple", "Kiwi", "Guava", "Papaya", "Watermelon"]

// 6. COPY BY REFERENCE ON ARRAYS (Same as objects!)
const fruitsArr2 = fruitsArr;                               // Both names point to the EXACT SAME array
fruitsArr2.push("Cherry");
console.log(fruitsArr);                                     // OUTPUT: ["Pineapple", "Kiwi", "Guava", "Papaya", "Watermelon", "Cherry"]
console.log(fruitsArr2);                                    // OUTPUT: ["Pineapple", "Kiwi", "Guava", "Papaya", "Watermelon", "Cherry"]
