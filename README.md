# Online Quiz App

This is a web-based Online Quiz Application built using Flask for the backend and vanilla JavaScript, HTML, and Tailwind CSS for the frontend. The app allows users to take quizzes, view their scores, and retry quizzes. Admins can create and manage quizzes through a dedicated admin panel.

---

## Features

### User Features
- Take quizzes by selecting options for multiple-choice questions.
- View scores immediately after submitting the quiz.
- Retry a quiz after viewing the results.

### Admin Features
- Create and delete quizzes.
- Add, edit, and delete questions for a quiz.
- View all available quizzes and their associated questions.

---

## Tech Stack

### Backend
- **Framework:** Flask
- **Database:** SQLite (default) or MySQL
- **ORM:** SQLAlchemy

### Frontend
- **HTML**
- **CSS Framework:** Tailwind CSS
- **JavaScript**

---

## Installation and Setup

### Prerequisites
- Python 3.x
- Flask
- Node.js (for managing Tailwind CSS, optional)
- MySQL (optional, if using MySQL instead of SQLite)

---

### Steps to Set Up the Project

1. **Clone the repository:**
   ```bash
   git clonehttps://github.com/yogeshsharma11/QuizApp
   cd QuizApp
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database:**
   - **For SQLite (default):**
     - The app will use `quiz.db` in the project root without any additional setup.
   - **For MySQL:**
     - Update the `SQLALCHEMY_DATABASE_URI` in `app.py`:
       ```python
       app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/quiz_db'
       ```

5. **Initialize the database:**
   - Create tables based on your database choice:
     ```bash
     flask shell
     >>> from models import db
     >>> db.create_all()
     >>> exit()
     ```

6. **Run the application:**
   ```bash
   flask run
   ```
   The app will be available at `http://127.0.0.1:5000`.

---

## Switching Between SQLite and MySQL

1. **Edit the `SQLALCHEMY_DATABASE_URI` in `app.py`:**
   - **SQLite** (default):
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
     ```
   - **MySQL:**
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/quiz_db'
     ```

2. **Reinitialize the database:**
   ```bash
   flask shell
   >>> from models import db
   >>> db.create_all()
   >>> exit()
   ```

---

## Folder Structure

```
project-root/
├── templates/            # HTML templates
├── static/               # Static files (CSS, JS, etc.)
├── app.py                # Main Flask app
├── models.py             # Database models
├── requirements.txt      # Python dependencies
├── users.json            # Admin credentials
├── README.md             # Project documentation
└── quiz.db               # SQLite database (generated after initialization)
```

---

## Admin Login

### Default Admin Credentials
- **Username:** `admin`
- **Password:** `password123`

Admin credentials are stored in `users.json`. You can modify this file to update the username or password.

---

## Usage

### Adding Quizzes and Questions
1. Log in to the admin panel at `/admin_login`.
2. Create a quiz by providing a title.
3. Add questions to the quiz by selecting the quiz, entering the question, options, and the correct answer.

### Taking a Quiz
1. Enter your name on the home page and start the quiz.
2. Select answers for all questions and submit the quiz.
3. View your score and retry if desired.

---

## Known Issues
- Currently, the app does not support editing existing questions or quizzes.

---

## Contribution

Contributions are welcome! If you find any bugs or want to add new features, please feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy Quizzing!

        