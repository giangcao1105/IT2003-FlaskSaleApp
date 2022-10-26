from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from app import db, app

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=False)

    def __str__(self):
        return self.name

class Product(BaseModel):
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    category_id= Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='Điện thoại')
        # c2 = Category(name='Máy tính bảng')
        # c3 = Category(name='Phụ kiện')
        # #db.create_all()

        # db.session.add_all([c1, c2, c3])
        # db.session.commit()

        p1 = Product(name='Iphone 6', description='Apple', price=2500000, image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248512/ntpwfnoqnvoxijrruim5.jpg', category_id=1)
        p2 = Product(name='Iphone X', description='Apple', price=2500000, image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248512/ntpwfnoqnvoxijrruim5.jpg', category_id=1)
        p3 = Product(name='Iphone 14', description='Apple', price=2500000, image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248512/ntpwfnoqnvoxijrruim5.jpg', category_id=2)

        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)

        db.session.commit()