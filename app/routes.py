from flask import Blueprint, render_template, request
import sqlite3

main = Blueprint('main', __name__)


def get_db_connection():
    conn = sqlite3.connect('data/questions.db')
    conn.row_factory = sqlite3.Row
    return conn


@main.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()

    # Dropdown values
    subjects = [row['subject'] for row in conn.execute("SELECT DISTINCT subject FROM questions")]
    years = [row['year'] for row in conn.execute("SELECT DISTINCT year FROM questions")]

    data = None
    selected_subject = request.form.get('subject')
    selected_year = request.form.get('year')
    selected_question = request.form.get('question')

    # Filtered questions
    questions = []
    if selected_subject and selected_year:
        questions = [row['question'] for row in conn.execute(
            "SELECT DISTINCT question FROM questions WHERE subject=? AND year=?",
            (selected_subject, selected_year)
        )]

    # Load data
    if selected_subject and selected_year and selected_question:
        query = """
        SELECT * FROM questions
        WHERE subject=? AND year=? AND question=?
        """
        data = conn.execute(query, (selected_subject, selected_year, selected_question)).fetchone()

    conn.close()
    return render_template("index.html", subjects=subjects, years=years,
                           questions=questions, data=data,
                           selected_subject=selected_subject,
                           selected_year=selected_year,
                           selected_question=selected_question)
