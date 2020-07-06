//Book Construtor 
class Book {
    constructor(title, author, isbn){
        this.title = title;
        this.author = author;
        this.isbn = isbn;
    }
}

//UI construtor
class UI {

    //add book to list function
    addBookToList(book){

        const list = document.getElementById('book-list');
        //create a tr element
        const row = document.createElement('tr');
        //insert cols in tr
        row.innerHTML = `
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${book.isbn}</td>
            <td><a href="#" class="delete">X</a></td>
        `;

        list.appendChild(row);

    }

    clearFields(){
        document.getElementById('title').value = '';
        document.getElementById('author').value = '';
        document.getElementById('isbn').value = '';
    }

    showAlert(message, className){

        const div = document.createElement('div');
        div.className = `alert ${className}`;
        div.appendChild(document.createTextNode(message));

        //get parent 
        const container = document.querySelector('.container');

        const form = document.getElementById('book-form');

        container.insertBefore(div, form);
        setTimeout(() => {
            document.querySelector('.alert').remove();
        }, 3000);

    }

    deleteBook(target){
        if(target.className === 'delete'){
            target.parentElement.parentElement.remove();
        }
    }
    
}

//Create event listeners 
document.getElementById('book-form').addEventListener('submit', function(e){

    const title = document.getElementById('title').value;
          author = document.getElementById('author').value;
          isbn = document.getElementById('isbn').value;

    //Init book
    const book = new Book(title, author, isbn);

    //Init UI
    const ui = new UI();

    //Validate 
    if(title === '' || author === '' || isbn === ''){
        ui.showAlert('Please fill in all fields', 'error')
    }else{
        ui.addBookToList(book);
        ui.clearFields();
        ui.showAlert("Book added", "success")
    }

    e.preventDefault();
})

// To remove book from list
const removeBtn = document.getElementById('book-list').addEventListener('click', function(e){

    const ui = new UI();
    ui.deleteBook(e.target);
    ui.showAlert("Successfully deleted", "success");
    e.preventDefault();
});