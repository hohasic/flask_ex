from flask import Flask, render_template, request
from utils.json_manager import load_members, save_members

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# signup_form
@app.route('/member/signup_form', methods=['GET'])
def signup_form():
    return render_template('signup_form.html')

# signup_confirm
@app.route('/member/signup_confirm', methods=['POST'])
def signup_confirm():
    mId = request.form['mId']
    mPw = request.form['mPw']
    mMail = request.form['mMail']
    mPhone = request.form['mPhone']

    members = load_members()

    # 아이디 중복 첵!
    if mId in members:
        return render_template('signup_result.html', 
                               result = 'NG')

    members[mId] = {
        "mId": mId,
        "mPw": mPw,
        "mMail": mMail,
        "mPhone": mPhone,
    }

    save_members(members)

    return render_template('signup_result.html', 
                           result = 'OK')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')