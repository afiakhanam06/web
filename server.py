import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reservation', methods=['POST'])
def reservation():
    # When the form is submitted, just show a thank you message
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        reservation_type = request.form['reservation-type']
        message = request.form['message']

        # Here we won't store the data, just return a thank you message
        return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)
