// 1. Ask how many test scores the user wants to enter
let countInput = prompt(`How many scores?`);
let count = parseInt(countInput);

let total = 0;

for (let i = 1; i <= count; i++) {
    let scoreInput = prompt(`Score ${i}`);
    let score = parseFloat(scoreInput);
    total += score;
}

let averageInt = total/count;
let average = averageInt

alert(`Average score is: ${average}`)
