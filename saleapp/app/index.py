from app import app, dao, admin, login
from flask import render_template, request, redirect
from flask_login import login_user, logout_user
import cloudinary.uploader


@app.route("/")
def index():
    kw = request.args.get('keyword')
    cate_id = request.args.get('category_id')
    products = dao.load_products(category_id=cate_id, kw=kw)
    return render_template('index.html', products=products)

@app.route('/products/<int:product_id>')
def product_detail(product_id):
    p = dao.get_product_by_id(product_id)
    return render_template('details.html', product=p)

@app.route('/register', menthods=['get', 'post'])
def register():
    err_msg = ''
    if request.method == 'POST':
        password = request.form['password']
        confirm = request.form['confirm']
        if password.__eq__(confirm):
            #upload cloudinary
            avatar = ''
            if request.files:
                res = cloudinary.uploader.upload(request.files['avatar'])
                avatar = res['secure_url']
            #Save user
            try:
                dao.register(name=request.form['name'],
                             username=request.form['username'],
                             password=request.form['password'],
                             avatar=avatar)
            except:
                err_msg = 'Đã có lỗi xảy ra vui lòng quay lại sau !'
            else:
                return redirect('/login')
        else:
            err_msg = 'Mật khẩu xác thực không khớp với mật khẩu gốc !'

    return render_template('/register.html', err_msg=err_msg)

@app.route('/login', menthods=['get', 'post'])
def login_my_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)
            return redirect('/')

    return render_template('login.html')

@app.route('/logout')
def logout_my_user():
    logout_user()
    return redirect('/login')

@app.context_processor
def common_attr():
    categories = dao.load_categories()

    return {'categories' : categories}

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route('/login-admin', methods=['post'])
def login_admin():
    username = request.form['username']
    password = request.form['password']

    user = dao.auth_user(username=username,password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')

if __name__ == "__main__":
    app.run(debug=True)