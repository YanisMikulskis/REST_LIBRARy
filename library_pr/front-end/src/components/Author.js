import React from "react";

import {Link} from 'react-router-dom'
const AuthorItem = ({author}) => {
    return (
        <tr>
            <td><Link to={`authors/${author.id}`}>{author.id}</Link></td>
            <td>{author.first_name}</td>
            <td>{author.birthday_year}</td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
      <table>
          <th>
              id
          </th>
          <th>
              First name (author.js)
          </th>
          <th>
              Last Name (author.js)
          </th>
          <th>
              Birthday year
          </th>
          {authors.map((author) => <AuthorItem author={author} />)}
      </table>
    )
}

export default AuthorList