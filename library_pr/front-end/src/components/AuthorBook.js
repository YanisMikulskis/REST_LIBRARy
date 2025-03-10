import React from "react";
import { useParams } from 'react-router-dom'

const AuthorBookItem = ({book}) => {
    return (
        <tr>
            <td>{book.id}</td>
            <td>{book.name_book}</td>
            <td>{book.author}</td>
        </tr>
    )
}

const AuthorBookList = ({books}) => {

    let { id } = useParams();
    let filtered_books = books.filter((book) => book.author === Number(id))
    return (
        <table>
            <thead>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>AUTHOR</th>

            </tr>
            </thead>
            <tbody>
            {filtered_books.map((book) => (
                <AuthorBookItem key={book.id} book={book} />))}
            </tbody>


        </table>
    )
}

export default AuthorBookList