from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'secret_key' 

# Questions pool
questions = [
    (["Apple", "Banana", "Mango", "Carrot"], "Carrot"),
    (["Cat", "Dog", "Lion", "Rose"], "Rose"),
    (["Red", "Blue", "Green", "Circle"], "Circle"),
    (["Mercury", "Venus", "Mars", "Sun"], "Sun"),
    (["BMW", "Audi", "Tesla", "Pizza"], "Pizza")
]

@app.route('/')
def index():
    if 'score' not in session:
        session['score'] = 0
        session['round'] = 1

    items, odd_one = random.choice(questions)
    shuffled_items = items[:]
    random.shuffle(shuffled_items)

    session['current_question'] = items
    session['odd_one'] = odd_one
    return render_template('index.html',
                           items=shuffled_items,
                           score=session['score'],
                           round=session['round'])

@app.route('/answer', methods=['POST'])
def answer():
    selected = request.form['selected']
    correct = session['odd_one']

    if selected == correct:
        session['score'] += 1
        result = 'Correct!'
    else:
        result = f'Wrong! The correct answer was {correct}.'

    session['round'] += 1

    if session['round'] > 5:
        final_score = session['score']
        session.clear()
        return render_template('index.html', result=result, final_score=final_score, items=[], score=final_score, round=5)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
