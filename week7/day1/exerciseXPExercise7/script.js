
let allBooks = [
    {
        title: "Harry Potter and the Sorcerer's Stone",
        author: "J.K. Rowling",
        image: "https://m.media-amazon.com/images/I/71-++hbbERL.jpg",
        alreadyRead: true
    },
    {
        title: "The Hobbit",
        author: "J.R.R. Tolkien",
        image: "https://m.media-amazon.com/images/I/A11+Gq4ebyL._AC_UF1000,1000_QL80_.jpg",
        alreadyRead: false
    }
];


let sectionElement = document.querySelector(".listBooks");


allBooks.forEach((book) => {
    let bookDiv = document.createElement("div");
    bookDiv.classList.add("book");

    let bookDetails = document.createElement("p");
    bookDetails.textContent = `${book.title} written by ${book.author}`;

    if (book.alreadyRead) {
        bookDetails.style.color = "red";
    }

    let bookImage = document.createElement("img");
    bookImage.src = book.image;
    bookImage.width = 100;

    bookDiv.appendChild(bookDetails);
    bookDiv.appendChild(bookImage);

    sectionElement.appendChild(bookDiv);
});
