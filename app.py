from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)
secret_number = str(random.randint(1000, 9999))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = request.form.get('guess')
    feedback = evaluate_guess(user_guess)
    return render_template('index.html', feedback=feedback)

def evaluate_guess(guess):
    correct_digits = sum(1 for digit in guess if digit in secret_number)
    correctly_placed = sum(1 for i in range(4) if guess[i] == secret_number[i])

    if correctly_placed == 4:
        return f"Congratulations! You guessed the number {secret_number}."
    else:
        return f"Correct digits: {correct_digits}, Correctly placed digits: {correctly_placed}"

if __name__ == "__main__":
    app.run(debug=True)
