// Main Task-4 : do-while + prompt (expense calculator)

let total = 0;
let amount;
do{
    amount = prompt("Enter an expense or (type 'done' to finish):");
    if (amount !== "done"){
        total += parseFloat(amount);
    }
}while (amount !== "done");
console.al(`total expense: ${total}`);