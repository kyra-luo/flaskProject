from flask import Flask, request, render_template,jsonify

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['DEBUG'] = True
@app.route('/')  # 这里是新添加的路由，表示根路径
def index():
    return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')  # 确保有 login.html 文件
    else:  # 处理 POST 请求
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "expected_username" and password == "expected_password":
            return jsonify(status='success')
        else:
            return jsonify(status='fail', error='Invalid credentials')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()






