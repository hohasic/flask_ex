from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# signup_form
@app.route('/member/signup_form', methods=['GET'])
def signup_form():
    return render_template('signup_form.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')