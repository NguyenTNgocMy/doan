from qlhs.models import  User, Students, MonHoc, DSLop, NienKhoa, BangDiem
from qlhs import db
from sqlalchemy import func, extract
from flask_login import current_user


def add_students(name, ngaysinh, SDT, sex, diachi, email):
    hs = Students(name=name, ngaysinh=ngaysinh, SDT=SDT, sex=sex, diachi=diachi, email=email)
    db.session.add(hs)
    db.session.commit()

# def get_students(hs_id):
#     return Students.query.get(hs_id)