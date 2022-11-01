from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import Product, Category
from app import app, db


admin = Admin(app=app, name='Quản trị bán hàng', template_mode='bootstrap4')
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))