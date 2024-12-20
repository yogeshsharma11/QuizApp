# Online Quiz App

This is a web-based Online Quiz Application built using Flask for the backend and vanilla JavaScript, HTML, and Tailwind CSS for the frontend. The app allows users to take quizzes, view their scores, and retry quizzes. Admins can create and manage quizzes through a dedicated admin panel.

## Features

### User Features
- Take quizzes by selecting options for multiple-choice questions.
- View scores immediately after submitting the quiz.
- Retry a quiz after viewing the results.

### Admin Features
- Create and delete quizzes.
- Add, edit, and delete questions for a quiz.
- View all available quizzes and their associated questions.

## Tech Stack

### Backend
- **Framework:** Flask
- **Database:** SQLite
- **ORM:** SQLAlchemy

### Frontend
- **HTML**
- **CSS Framework:** Tailwind CSS
- **JavaScript**

## Installation and Setup

### Prerequisites
- Python 3.x
- Flask
- Node.js (for managing Tailwind CSS, optional)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/online-quiz-app.git
   cd online-quiz-app
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scripts\activate   # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   flask shell
   >>> from models import db
   >>> db.create_all()
   >>> exit()
   ```

5. Run the application:
   ```bash
   flask run
   ```
   The app will be available at `http://127.0.0.1:5000`.

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

## Admin Login

### Default Admin Credentials
- **Username:** `admin`
- **Password:** `password123`

Admin credentials are stored in `users.json`. You can modify this file to update the username or password.

## Usage

### Adding Quizzes and Questions
1. Log in to the admin panel at `/admin_login`.
2. Create a quiz by providing a title.
3. Add questions to the quiz by selecting the quiz, entering the question, options, and the correct answer.

### Taking a Quiz
1. Enter your name on the home page and start the quiz.
2. Select answers for all questions and submit the quiz.
3. View your score and retry if desired.

## Known Issues
- Currently, the app does not support editing existing questions or quizzes.

## Contribution
Contributions are welcome! If you find any bugs or want to add new features, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy Quizzing!
