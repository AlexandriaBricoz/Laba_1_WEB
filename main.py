# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# О университете
@app.route('/about')
def about():
    return render_template('about.html')

# Факультеты
@app.route('/faculties')
def faculties():
    faculties = [
        {'name': 'Архитектурный факультет', 'abbr': 'АФ'},
        {'name': 'Факультет аэрокосмический', 'abbr': 'ФАК'},
        {'name': 'Факультет военного обучения', 'abbr': 'ФВО'},
        {'name': 'Факультет вычислительной математики и информатики', 'abbr': 'ВМИ'},
        {'name': 'Факультет журналистики', 'abbr': 'ФЖ'},
        {'name': 'Факультет лингвистики и международных коммуникаций', 'abbr': 'ЛМК'},
        {'name': 'Факультет материаловедения и металлургических технологий', 'abbr': 'ММТ'},
        {'name': 'Факультет механико-технологический', 'abbr': 'МТ'},
        {'name': 'Факультет предвузовской подготовки', 'abbr': 'ФПП'},
        {'name': 'Факультет прикладной математики, физики и технических наук', 'abbr': 'ПМФ'},
        {'name': 'Факультет психологии', 'abbr': 'ФП'},
        {'name': 'Факультет экономики и управления', 'abbr': 'ФЭУ'},
        {'name': 'Юридический факультет', 'abbr': 'ЮФ'},
    ]
    return render_template('faculties.html', faculties=faculties)

# Контакты
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Форма обратной связи
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Здесь можно добавить обработку формы (отправка email, сохранение в БД и т.д.)
        print(f"Получено сообщение от {name} ({email}): {message}")
        return redirect(url_for('feedback_thanks'))
    return render_template('feedback.html')

# Благодарность за обратную связь
@app.route('/feedback/thanks')
def feedback_thanks():
    return render_template('feedback_thanks.html')

if __name__ == '__main__':
    app.run(debug=True)