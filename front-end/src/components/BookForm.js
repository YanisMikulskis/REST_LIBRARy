import React from "react";

class BookForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name_book: '',
      authors: props.authors.length > 0 ? props.authors[0].id : null
      // authors: props.authors[0].id
    };
  }

  handleChange = (event) => {
    this.setState({
      [event.target.name]: event.target.value });
  }

  handleSubmit = (event) => {
    event.preventDefault();
    this.props.createBook(this.state.name_book, [parseInt(this.state.authors)]);


  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Name</label>
          <input
            type="text"
            className="form-control"
            name="name_book"
            value={this.state.name_book}
            onChange={this.handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="author">Author</label>
          <select
            name="authors"
            className="form-control"
            value={this.state.authors}
            onChange={this.handleChange}
            required
          >
            {this.props.authors.map((item) => (
              <option key={item.id} value={item.id}>{item.first_name} {item.last_name}</option>
            ))}
          </select>
        </div>

        <input type="submit" className="btn btn-primary" value="Save" />
      </form>
    );
  }
}

export default BookForm;
