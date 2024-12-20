import json
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, Quiz, Question
from flask import jsonify

app = Flask(__name__)
#Use Sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SECRET_KEY'] = 'a76b0e3382738170d6f881a39134d02d'
'''
#When Connect to MYSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/quiz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
'''
app.config['SECRET_KEY'] = 'a76b0e3382738170d6f881a39134d02d'
db.init_app(app)

def load_user_data():
    with open('users.json') as f:
        return json.load(f)

'''
#When use Mysql
with app.app_context():
    db.create_all() 
'''

@app.route('/')
def index():
    quizzes = Quiz.query.all() 
    return render_template('index.html', quizzes=quizzes)

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        users = load_user_data()
        admin = users.get('admin', {})

        if admin and admin['username'] == username and admin['password'] == password:
            session['logged_in'] = True  
            return redirect(url_for('admin'))  
        else:
            flash('!Invalid Username or Password', 'error')
            return redirect(url_for('admin_login')) 

   
    return render_template('admin_login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):  
        return redirect(url_for('admin_login'))

    if request.method == 'POST':
        if request.form.get('title'):
            title = request.form.get('title')
            new_quiz = Quiz(title=title)
            db.session.add(new_quiz)
            db.session.commit()

        quiz_id = request.form.get('quiz_id')
        if quiz_id:
            question_text = request.form.get('question_text')
            options = {
                'a': request.form.get('option_a'),
                'b': request.form.get('option_b'),
                'c': request.form.get('option_c'),
                'd': request.form.get('option_d')
            }
            correct_option = request.form.get('correct_option')

            if question_text:
                new_question = Question(
                    question_text=question_text,
                    option_a=options['a'],
                    option_b=options['b'],
                    option_c=options['c'],
                    option_d=options['d'],
                    correct_option=correct_option,
                    quiz_id=quiz_id
                )
                db.session.add(new_question)
                db.session.commit()

        return redirect(url_for('admin'))

    quizzes = Quiz.query.all()
    return render_template('admin.html', quizzes=quizzes)

@app.route('/delete_quiz/<int:quiz_id>', methods=['POST'])
def delete_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    for question in quiz.questions:
        db.session.delete(question)
    db.session.delete(quiz)
    db.session.commit()
    return redirect(url_for('admin'))

@app.route('/delete_question/<int:question_id>', methods=['POST'])
def delete_question(question_id):
    question = Question.query.get_or_404(question_id)
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('admin'))

@app.route('/quiz_questions/<int:quiz_id>')
def quiz_questions(quiz_id):
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    question_data = []
    for question in questions:
        question_data.append({
            "id": question.id,
            "question_text": question.question_text,
            "a": question.option_a,
            "b": question.option_b,
            "c": question.option_c,
            "d": question.option_d,
            "correct_option": question.correct_option,
        })

    return jsonify({"questions": question_data})

@app.route('/logout')
def logout():
    session.pop('logged_in', None) 
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
