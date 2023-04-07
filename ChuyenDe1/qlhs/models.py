from sqlalchemy import Column, String, Integer, Float, ForeignKey, Text, Enum, DateTime
from sqlalchemy.orm import relationship
from qlhs import db, app
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ ='user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(Text)
    user_role = Column(String(20), default='USER')
    diem = relationship('BangDiem', backref='user', lazy=True)

    def __str__(self):
        return self.name


class DSLop(db.Model):
    __tablename__ = 'dslop'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    siso = Column(Integer, nullable=False)
    ngaylap = Column(DateTime, default=datetime.now())

    def __str__(self):
        return self.name


class Students(db.Model):
    __tablename__ = 'hs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    ngaysinh = Column(DateTime, nullable=False)
    SDT = Column(Integer, nullable=False)
    sex = Column(String(20), nullable=False)
    diachi = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    diem= relationship('BangDiem', backref='hs', lazy=True)

    def __str__(self):
        return self.name


class MonHoc(db.Model):
    __tablename__ = 'monhoc'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String(100), nullable=False)


class NienKhoa(db.Model):
    __tablename__ = 'nienkhoa'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hocki = Column(Integer, nullable=False)
    namhoc = Column(Integer, nullable=False)
    diem = relationship('BangDiem', backref='nienkhoa', lazy=True)

class BangDiem(db.Model):
    __tablename__ = 'bangdiem'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # giaTri = Column(Integer) (vd diem 15 phut co 3 cot)
    diem15phut = Column(String(50))
    diem1tiet = Column(String(50))
    diemthi = Column(String(50))
    ngaytao = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey(User.id))
    hs_id = Column(Integer, ForeignKey(Students.id))
    nienkhoa_id = Column(Integer, ForeignKey(NienKhoa.id))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

