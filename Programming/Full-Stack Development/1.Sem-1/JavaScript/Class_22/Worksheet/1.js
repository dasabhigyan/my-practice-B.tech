let data = {
  "products": [
    {
      "id": 26,
      "title": "Green Chili Pepper",
      "price": 0.99
    },
    {
      "id": 27,
      "title": "Honey Jar",
      "price": 6.99
    },
    {
      "id": 28,
      "title": "Ice Cream",
      "price": 5.49
    },
    {
      "id": 29,
      "title": "Juice",
      "price": 3.99
    },
    {
      "id": 30,
      "title": "Kiwi",
      "price": 2.49
    },
    {
      "id": 31,
      "title": "Lemon",
      "price": 0.79
    },
    {
      "id": 32,
      "title": "Milk",
      "price": 3.49
    },
    {
      "id": 33,
      "title": "Mulberry",
      "price": 4.99
    },
    {
      "id": 34,
      "title": "Nescafe Coffee",
      "price": 7.99
    },
    {
      "id": 35,
      "title": "Potatoes",
      "price": 2.29
    }
  ],
  "total": 194,
  "skip": 25,
  "limit": 10
}

//--------------------
//Q1
// 1.To access the whole list:

// data.products

// 2.To access the first Product:

// data.products

// 3.To access the first title and product:

// data.products.title
// data.products.price

//Q2
//evey item  with price in INR

for (i = 0; i < data.products.length; i++) {
    const product = data.products[i];
    const priceINR = Math.round(product.price * 100)
    console.log(`${product} : ${priceINR}`)
}