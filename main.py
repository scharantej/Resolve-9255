
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        principal = float(request.form['principal'])
        rate = float(request.form['rate'])
        years = int(request.form['years'])

        # Calculate future value
        future_value = principal * (1 + (rate / 100)) ** years

        # Redirect to result page
        return redirect(url_for('result', future_value=future_value))

    return render_template('index.html')

@app.route('/result')
def result():
    future_value = request.args['future_value']
    return render_template('result.html', future_value=future_value)

if __name__ == '__main__':
    app.run()
