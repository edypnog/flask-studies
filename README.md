# Simple CRUD App with Flask

This README.md file provides an overview of a basic CRUD (Create, Read, Update, Delete) application built with Flask. The application allows you to manage a collection of items by performing CRUD operations on them.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python (3.11 or later)
- Flask (web framework)
- SQLite (database, comes pre-installed with Python)

## Getting Started

1. Clone the repository:

```bash
git clone <https://github.com/edypnog/flask-studies>
```

2. Navigate to the project directory:

```bash
cd <flask-crud>
```

3. Install the required dependencies using `pip`:

```bash
pip install flask
```

4. Set up the database by running the following commands:

```bash
python
```

```python
from app import db
db.create_all()
exit()
```

## Running the Application

To start the Flask development server, execute the following command:

```bash
python app.py
```

The server should be up and running at `http://localhost:8000/`.

## Project Structure

The project follows a simple structure:

```
<flask-studies>/
  ├── app.py                # Main application file (contains routes)
  ├── templates/            # HTML templates for rendering views
  │   ├── index.html        # Homepage to list all items
  │   ├── edit.html         # View to display the edit page
  └── static/               # Static files (e.g., CSS, JavaScript)
      └── style.css
```

## Data Models

The application uses a simple SQLite database with a single model.

- `id` (Primary Key): Unique identifier for each item.
- `title`: Title of the book.
- `author`: Author of the book.

## Contributing

Contributions to this CRUD application are welcome. Feel free to open issues and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
