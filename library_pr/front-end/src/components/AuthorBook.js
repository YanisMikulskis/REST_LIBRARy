import React from "react";
import { useParams } from 'react-router-dom'

const AuthorBookItem = ({book, authors}) => {
    const authorNames = book.authors && book.authors.length > 0
    ? book.authors
            .map(authorId => {
                const author = authors.find(a => a.id === authorId);
                return author ? `${author.first_name} ${author.last_name}` : null;
            })
            .filter(name => name !== null)
            .join(", ")
        : "нет авторов";
    console.log('book.authors:', book.authors);
    console.log('authors from props:', authors);
    return (
        <tr>
            <td>{book.id}</td>
            <td>{book.name_book}</td>
            <td>{authorNames}</td>
        </tr>
    )
}

const AuthorBookList = ({books, authors}) => {
    console.log('какие книги')
    console.log(books)
    let { id } = useParams();
    let filtered_books = books.filter((book) => book.authors.includes(Number(id)))
    console.log('проверка авторов')
    console.log(filtered_books)
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
                <AuthorBookItem key={book.id} book={book} authors={authors} />))}
            </tbody>


        </table>
    )
}

export default AuthorBookList