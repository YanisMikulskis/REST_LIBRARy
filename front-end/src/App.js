import logo from './logo.svg'
import './App.css'
import React from "react"
import AuthorList from "./components/Author.js"
import BookList from "./components/Book.js"
import AuthorBookList from "./components/AuthorBook";
import AuthorBook from "./components/AuthorBook";
import {Route, Link, BrowserRouter, Redirect, Switch} from "react-router-dom"

import axios from 'axios'
import LoginForm from "./components/Auth";
import Cookies from "universal-cookie";

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
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username,
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
        axios.get('http://127.0.0.1:8000/api/author/', {headers})
            .then(response => {
                this.setState({'authors': response.data.results})
                console.log('jkjlkk')
                console.log(response.data)
            }).catch(error => console.log(error))


        axios.get('http://127.0.0.1:8000/api/book/', {headers})
            .then(response => {
                this.setState({'books': response.data.results})
                console.log('j009990')
                console.log(response.data)
                console.log(response.data.results.authors)
            }).catch(error => {
                console.log(error)
                this.setState({books: []})
        })
    }

    componentDidMount() {
        this.get_token_from_storage()
        // this.load_data()
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
                    <Route exact path='/books' render={(props) => <BookList books={this.state.books} {...props} />} />
                    <Route exact path='/login' render={(props) => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                    <Route path='/authors/:id' render={(props) => <AuthorBookList books={this.state.books} authors={this.state.authors} {...props} />} />

                    <Redirect from='/' to='/authors' />
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
