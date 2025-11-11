from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gastos_var')
def gastos_var():
    return render_template('gastos_var.html')

if __name__ == "__main__":
    app.run(debug=True)