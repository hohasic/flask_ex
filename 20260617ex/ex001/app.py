from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello Flask</h1>"

# http://127.0.0.1:5000/hello
@app.route('/hello')
def hello():
    return "Hello Student!!"

# http://127.0.0.1:5000/me
@app.route('/me')
def me():
    return '나는 Flask 개발자 입니다.'

@app.route('/about')
def about():
    return '소개 페이지'

# http://127.0.0.1:5000/users/9
# 동적 URL 처리(Path Parameter)
# int       정수
# string    문자열
# float     실수
# path      전체 경로(중간에 /가 있어도 문자열 끝까지 모두 받는다.)
@app.route('/users/<int:user_id>')
def get_user(user_id):
    print(f'user_id: {user_id}') # 1
    return f'{user_id} 사용자 조회' # 1 사용자 조회

# string
# http://127.0.0.1:5000/users/gildong
@app.route('/users/<string:name>')
def get_name(name):
    return f'{name}님 요청'

# float
# http://127.0.0.1:5000/pi/3.14
@app.route('/pi/<float:pi>')
def get_pi(pi):
    return f'pi: {pi}'

# path      전체 경로(중간에 /가 있어도 문자열 끝까지 모두 받는다.)
# http://127.0.0.1:5000/files/images/cat.jpg
@app.route('/files/<path:filepath>')        # filepath = images/cat.jpg
def files(filepath):
    return f'filepath: {filepath}'          # filepath: images/cat.jpg

# GET
# 1. 경로 변수(path variable)
# http://127.0.0.1:5000/search/7
# @app.route('/search/<int:no>', methods=['GET'])
# def search(no):
#     return f'{no} 사용자'

# 2. 쿼리 스트링(query string)
# http://127.0.0.1:5000/search?uNoo=7&uName=gildong
@app.route('/search', methods=['GET'])
def search():
    uNo = request.args.get('uNoo')
    uName = request.args.get('uName')
    return f'{uNo} {uName} 사용자'

# POST
# http://127.0.0.1:5000/login_form
@app.route('/login_form', methods=['GET'])
def login_form():
    '''
    str = ''
    str += '<form action="/login_confirm" method="post">'
    str += '<input type="text" name="u_id" placeholder="Input user ID!!">'
    str += '<br>'
    str += '<input type="password" name="u_pw" placeholder="Input user PW!!">'
    str += '<br>'
    str += '<input type="submit" value="SIGN UP">'
    str += '</form>'
    return str
    '''

    return '''
    <form action="/login_confirm" method="post">
        <input type="text" name="u_id" placeholder="Input user ID!!">
            <br>
        <input type="password" name="u_pw" placeholder="Input user PW!!">
            <br>
        <input type="submit" value="SIGN UP">
    </form>
    '''

@app.route('/login_confirm', methods=['post'])
def login_confirm():
    u_id = request.form.get('u_id')
    u_pw = request.form.get('u_pw')

    if u_id == 'gildong' and u_pw == '1234':
        return f'{u_id}님 로그인 성공!!'
    else:
        return f'{u_id}님 로그인 성패!!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')