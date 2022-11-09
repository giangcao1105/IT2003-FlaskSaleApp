from app import app, dao, admin, login
from flask import render_template, request, redirect
from flask_login import login_user


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

@app.context_processor
def common_attr():
    categories = dao.load_categories()

    return {'categories' : categories}

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

@app.route('/login_admin', methods = ['post'])
def login_admin():
    username =request.form['username']
    password = request.form['password']

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