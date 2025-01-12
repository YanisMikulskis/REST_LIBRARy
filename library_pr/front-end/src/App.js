import logo from './logo.svg';
import './App.css';
import React from "react";
import AuthorList from "./components/Author";

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authors': []
    }
  }

  componentDidMount() {
    const authors = [
      {
        'first_name': 'Иван',
        'last_name': 'Иванов',
        'birthday_year': 1995
      },
      {
        'first_name': 'Пётр',
        'last_name': 'Сергеев',
        'birthday_year': 2000
      },
      {
        'first_name': 'Виктор',
        'last_name': 'Иванов',
        'birthday_year': 1950
      }
    ]
    this.setState(
        {
          'authors': authors
        }
    )
  }

  render () {
    return (
        <div>
          <AuthorList authors={this.state.authors} />
        </div>
    )
  }


}

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
