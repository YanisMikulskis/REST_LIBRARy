import React from "react";


const BookItem = ({book}) => {
    return (
        <tr>
            <td>
                {book.id}
            </td>
            <td>
                {book.name_book}
            </td>
            <td>
                {book.author}
            </td>

        </tr>
    )
}

const BookList = ({books}) => {
    return (
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

          {books.map((book) => <BookItem book={book} />)}
      </table>
    )
}

export default BookList