// Declare the running total and loop control variable outside the loop
let total = 0;
let addAnother;

do{
    // Prompt for item name and price
    itemName = prompt(`Item title?`);
    priceInt = prompt(`Item price?`);
    price = parseFloat(priceInt);

    // 2. Add price to running total
    total += price;

    // 3. Log item details and updated running total
    console.log(`item: ${itemName} | price: ${price} | Running total: ${total}`);

    // 4. Ask the user wheter to continue
    addAnother = prompt(`Add another item?(yes/no)`)

} while (addAnother !== "no");

// 5. Display the final total in alert 
alert(`Final total: ${total.toFixed(2)}`)
