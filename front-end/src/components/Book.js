import React from "react";
import {Link} from 'react-router-dom'

const BookItem = ({book, deleteBook}) => {
    return (
        <tr>
            <td>
                {book.id}
            </td>
            <td>
                {book.name_book}
            </td>
            <td>
                {book.authors.map((author, index) => (
                        <span key={index}>
                        {author.first_name} {index < book.authors.length - 1 ? ', ' : ''}
                        </span>
                    ))}
            </td>

            <td><button onClick={() => deleteBook(book.id)} type='button'>Delete</button></td>
        </tr>
    )
}

const BookList = ({books, deleteBook}) => {
    return (
        <div>

      <table>
          <th>
              id
          </th>
          <th>
              name_book
          </th>
          <th>
              authors
          </th>
          <th></th>

          {books.map((book) => <BookItem key={book.id} book={book} deleteBook={deleteBook}/>)}
      </table>
        <Link to='/books/create'>Create</Link>
            </div>
    )
}

export default BookList