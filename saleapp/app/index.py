from app import app
from app import dao
from flask import render_template


@app.route("/")
def index():
    categories = dao.load_categories()
    products = dao.load_products()
    return render_template('index.html', categories=categories, products=products)

if __name__ == "__main__":
    app.run(debug=True)