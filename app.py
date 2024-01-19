from flask import Flask, render_template

import random
app = Flask(__name__, template_folder='templates')


y_new = random.uniform(10000.000000, 80000.000000)






@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():


    return render_template('result.html', y_new=y_new)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
