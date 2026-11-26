// =========================================================
// CLASS 25: DYNAMIC RENDERING (DOM Manipulation Practice)
// Note: Link this file to index.html and open with Live Server.
// =========================================================

/* REQUIRED HTML (index.html) & CSS (styles.css) REFERENCE:
------------------------------------------------------------
index.html (inside <body>):
  <header></header>
  <main id="root">
    <div class="card">
      <img src="https://cloud-computing-lectures-likhilesh-abcdxyz.s3.ap-south-1.amazonaws.com/likhi-laptop.jpg" />
      <div class="product-info">
        <h4>Macbook Pro M1 - 2022</h4>
        <p>Price: $1100</p>
        <p>Rating: 4.9</p>
      </div>
    </div>
  </main>
  <footer></footer>
  <script src="./script.js"></script>

styles.css:
  * { padding: 0; margin: 0; box-sizing: border-box; }
  .card {
    margin: 24px auto; padding-right: 24px; border: 1px solid brown;
    border-radius: 16px; display: flex; align-items: center;
    gap: 24px; max-width: fit-content;
  }
  img {
    max-height: 125px;
    border-top-left-radius: 12px; border-bottom-left-radius: 12px;
  }
------------------------------------------------------------
*/


// =========================================================
// PART 1: THE DOM TREE & ADDING A CARD WITH JAVASCRIPT
// =========================================================
// Q1:
//   (a) Parent chain from document to h4:
//       document -> html -> body -> main#root -> div.card -> div.product-info -> h4
//   (b) Direct children of div.card:
console.log(document.querySelector(".card").children);      // OUTPUT: HTMLCollection(2) [img, div.product-info]

// Steps 1 to 5: Create a 2nd card dynamically
const root = document.getElementById("root");

const stepCard = document.createElement("div");             // Step 1: Create <div> in memory (not visible yet)
stepCard.className = "card";                                // Step 2: Give it class="card"
stepCard.innerHTML = `                                      // Step 3: Put HTML inside it
  <img src="https://cloud-computing-lectures-likhilesh-abcdxyz.s3.ap-south-1.amazonaws.com/likhi-laptop.jpg" />
  <div class="product-info">
    <h4>Macbook Pro M1 - 2022</h4>
    <p>Price: $1100</p>
    <p>Rating: 4.9</p>
  </div>
`;
// Q2: The card ONLY appears on the page after appendChild() attaches it to #root!
// root.appendChild(stepCard);                              // PAGE: A 2nd identical Macbook card appears


// =========================================================
// PART 2: RENDERING FROM DATA (Object -> HTML)
// =========================================================
// Q3 & Q4: Keeping data in an object means you only edit the object,
//          NEVER the HTML template!
const product = {
  title: "Macbook Pro M1 - 2022",
  price: "$999",                                            // Updated from "$1100"
  rating: 4.5,                                              // Updated from 4.9
};

const dataCard = document.createElement("div");
dataCard.className = "card";
dataCard.innerHTML = `
  <img src="https://cloud-computing-lectures-likhilesh-abcdxyz.s3.ap-south-1.amazonaws.com/likhi-laptop.jpg" />
  <div class="product-info">
    <h4>${product.title}</h4>
    <p>Price: ${product.price}</p>
    <p>Rating: ${product.rating}</p>
  </div>
`;
// root.appendChild(dataCard);                              // PAGE: Renders card with "$999" and "4.5"


// =========================================================
// PART 3: RENDERING FROM AN ARRAY OF OBJECTS (Manual way)
// =========================================================
const manualProducts = [
  { title: "Bag", price: "$200", rating: 4.2 },
  { title: "Mat", price: "$100", rating: 3.9 },
];

// Card 1 -> manualProducts[0] (Bag)
const newCard1 = document.createElement("div");
newCard1.className = "card";
newCard1.innerHTML = `
  <img src="https://images.jdmagicbox.com/quickquotes/images_main/sara-30-liters-polyester-black-school-bag-black-178207114-ksaft.jpg" />
  <div class="product-info">
    <h4>${manualProducts[0].title}</h4>
    <p>Price: ${manualProducts[0].price}</p>
    <p>Rating: ${manualProducts[0].rating}</p>
  </div>
`;
// root.appendChild(newCard1);                              // PAGE: Renders Bag card

// Q5: Card 2 -> manualProducts[1] (Mat) — reuses the same 'root' variable
const newCard2 = document.createElement("div");
newCard2.className = "card";
newCard2.innerHTML = `
  <img src="https://rukminim2.flixcart.com/image/480/640/l58iaa80/mat/z/t/w/medium-natural-korai-grass-sleeping-mat-3-5-x-6-feet-river-grass-original-imagfyhgq4jvgmrg.jpeg?q=90" />
  <div class="product-info">
    <h4>${manualProducts[1].title}</h4>
    <p>Price: ${manualProducts[1].price}</p>
    <p>Rating: ${manualProducts[1].rating}</p>
  </div>
`;
// root.appendChild(newCard2);                              // PAGE: Renders Mat card below Bag
// Q6: Doing this manually means copying the whole block for every new product!


// =========================================================
// PART 4: RENDERING WITH A LOOP & FUNCTION (Final Clean Code!)
// =========================================================
// Put the image URL inside each object ('thumbnail') and let a loop do the work!
const products = [
  {
    title: "Bag",
    price: "$200",
    rating: 4.2,
    thumbnail: "https://images.jdmagicbox.com/quickquotes/images_main/sara-30-liters-polyester-black-school-bag-black-178207114-ksaft.jpg",
  },
  {
    title: "Mat",
    price: "$100",
    rating: 3.9,
    thumbnail: "https://rukminim2.flixcart.com/image/480/640/l58iaa80/mat/z/t/w/medium-natural-korai-grass-sleeping-mat-3-5-x-6-feet-river-grass-original-imagfyhgq4jvgmrg.jpeg?q=90",
  },
  // Q8: Adding a 3rd product here requires ZERO changes to main()!
  {
    title: "Headphones",
    price: "$150",
    rating: 4.7,
    thumbnail: "https://cloud-computing-lectures-likhilesh-abcdxyz.s3.ap-south-1.amazonaws.com/likhi-laptop.jpg",
  },
];

function main(arr) {
  const root = document.getElementById("root");

  for (let i = 0; i < arr.length; i++) {
    // Q7: Why doesn't the 2nd card replace the 1st?
    //     Because each loop run creates a BRAND-NEW <div> in memory,
    //     and appendChild() ADDS it to the end of #root.
    const newCard = document.createElement("div");
    newCard.className = "card";
    newCard.innerHTML = `
      <img src="${arr[i].thumbnail}" />
      <div class="product-info">
        <h4>${arr[i].title}</h4>
        <p>Price: ${arr[i].price}</p>
        <p>Rating: ${arr[i].rating}</p>
      </div>
    `;
    root.appendChild(newCard);
  }
}

main(products);                                             // PAGE: Dynamically renders ALL 3 product cards below Macbook!
