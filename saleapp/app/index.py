from app import app
from app import dao
from flask import render_template, request
from app import admin


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


if __name__ == "__main__":
    app.run(debug=True)