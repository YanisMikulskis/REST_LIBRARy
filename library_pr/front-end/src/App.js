import logo from './logo.svg'
import './App.css'
import React from "react"
import AuthorList from "./components/Author.js"
import BookList from "./components/Book.js"
import AuthorBookList from "./components/AuthorBook";
import {Route, Link, BrowserRouter, Redirect, Switch} from "react-router-dom"


const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}
class App extends React.Component {
    constructor(props) {
        super(props)

        const author1 = {id: 1, first_name: 'Александр', last_name: 'Грин',  birthday_year: 1880}
        const author2 = {id: 2, first_name: 'Александр', last_name: 'Пушкин', birthday_year: 1799}
        const authors = [author1, author2]

        const book1 = {id: 1, name_book: 'Алые паруса', author: author1.id}
        const book2 = {id: 2, name_book: 'Золотая цепь', author: author1.id}
        const book3 = {id: 3, name_book: 'Пиковая дама', author: author2.id}
        const book4 = {id: 4, name_book: 'Руслан и Людмила', author: author2.id}
        const books = [book1, book2, book3, book4]
        // const books = [4,5,6]
        this.state = {
            'authors': authors,
            'books': books
        }
    }

    render() {
        return (
            <div className='App'>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Authors</Link>
                            </li>
                            <li>
                                <Link to='/books'>Books</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                    <Route exact path='/' render={(props) => <AuthorList authors={this.state.authors} {...props} />} />
                    <Route exact path='/books' render={(props) => <BookList books={this.state.books} {...props} />} />
                    <Route path='/author/:id' render={(props) => <AuthorBookList books={this.state.books} {...props} />} />

                    <Redirect from='/authors' to='/' />
                    <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>

            </div>
        )
    }
}
  //   this.state = {
  //     'authors': []
  //   }
  // }
  //
  // componentDidMount() {
  //   axios.get('http://127.0.0.1:8000/api/author')
  //       .then(response => {
  //         const authors = response.data.results
  //         this.setState(
  //             {
  //               'authors': authors
  //             }
  //         )
  //       }).catch(error => console.log(error))
  //
  // }
  //
  // render() {
  //   return (
  //       <div>
  //         <AuthorList authors={this.state.authors}/>
  //       </div>




// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }




export default App;
