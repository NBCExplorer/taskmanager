# Taskmanager

Taskmanager is a Python application for managing tasks with a MySQL database. It uses Kivy for the UI, and integrates Sphinx documentation and pytest unit tests.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/<NBCExplorer>/taskmanager.git
   cd taskmanager
   ```

2. **Set Up Virtual Environment & Install Dependencies:**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   ```

3. **Set Up the Database:**

   - Create your MySQL database using the provided SQL script [app/db_creation.sql](app/db_creation.sql).

4. **Environment Variables:**

   - Create an `.env` file in the app folder (or use the provided one) with your database configuration.

## Running the Application

Run the app with:

```bash
python app/main.py
```

## Documentation

The Sphinx documentation is located in the `docs` folder.

- To build the HTML documentation:
  
  ```bash
  cd docs
  make html  # or make.bat html on Windows
  ```

- Open the generated HTML files in `docs/build/html`.

## Testing

Unit tests are located in the `tests` folder. To run the tests:

```bash
pytest --maxfail=1 --disable-warnings -q
```

## GitHub Repository

This project is tracked on GitHub. Commit your changes and push them to your repository for submission.