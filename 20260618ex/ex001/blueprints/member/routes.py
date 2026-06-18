from flask import Blueprint, render_template, request
from utils.json_manager import load_members, save_members

member_bp = Blueprint(
    'member',
    __name__,
    url_prefix='/member'
)

# signup_form
@member_bp.route('/signup_form', methods=['GET'])
def signup_form():
    return render_template('signup_form.html')

# signup_confirm
@member_bp.route('/signup_confirm', methods=['POST'])
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

# signin_form
@member_bp.route('/signin_form', methods=['GET'])
def signin_form():
    return render_template('signin_form.html')