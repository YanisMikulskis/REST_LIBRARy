import './App.css'
import React from "react"
import AuthorList from "./components/Author.js"
import BookList from "./components/Book.js"
import AuthorBookList from "./components/AuthorBook";
import {BrowserRouter, Link, Redirect, Route, Switch} from "react-router-dom"

import axios from 'axios'
import LoginForm from "./components/Auth";
import Cookies from "universal-cookie";
import BookForm from "./components/BookForm";

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
        this.state = {
            'authors': [],
            'books': [],
            'token': ''
        }
    }






    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, ()=>this.load_data())
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }
    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, ()=>this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8001/api-token-auth/', {username: username,
            password: password})
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated())
            {
                headers['Authorization'] = 'Token ' + this.state.token
            }
            return headers
    }


    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8001/api/author/', {headers})
            .then(response => {
                this.setState({'authors': response.data.results})
            }).catch(error => console.log(error))


        axios.get('http://127.0.0.1:8001/api/book/', {headers})
            .then(response => {
                this.setState({'books': response.data.results})
            }).catch(error => {
                console.log(error)
                this.setState({books: []})
        })
    }

    componentDidMount() {
        this.get_token_from_storage()
        // this.load_data()
    }

    deleteBook(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8001/api/book/${id}/`, {headers: headers})
            .then(response => {
                this.setState({books: this.state.books.filter((book)=>book.id !== id)})

            }).catch(error => console.log(error))
    }





    createBook(name_book, authors) {
        const headers = this.get_headers()
        const data = {name_book:name_book, authors:authors}
        console.log('fsdfsfsfssd')
        console.log(data)
        axios.post('http://127.0.0.1:8001/api/book/', data, {headers: headers})
            .then(response => {
                // let new_book = response.data
                // new_book.authors = this.state.authors.filter((author) => new_book.authors.includes(author.id))
                //
                // this.setState({books: [...this.state.books, new_book]})
                this.load_data()
            }).catch(error => console.log(error))



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
                            <li>
                                {this.is_authenticated() ? <button
                                    onClick={()=>this.logout()}>Logout</button>: <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                    <Route exact path='/authors' render={(props) => <AuthorList authors={this.state.authors} {...props} />} />
                    <Route exact path='/books' render={(props) => <BookList books={this.state.books} deleteBook={(id) => this.deleteBook(id)} {...props} />} />
                    <Route exact path='/login' render={(props) => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                    <Route path='/authors/:id' render={(props) => <AuthorBookList books={this.state.books} authors={this.state.authors} {...props} />} />
                    <Route exact path='/books/create' component={ () => <BookForm authors={this.state.authors}
                                                                                  createBook={(name_book, authors) => this.createBook(name_book, authors)}/>}
                        />



                    <Redirect from='/' to='/authors' />
                    <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>

            </div>
        )
    }
}


export default App;
