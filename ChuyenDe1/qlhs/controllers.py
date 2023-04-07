from flask import render_template, request, redirect, session
from qlhs import utils, app, models
from qlhs.models import User, Students, MonHoc, DSLop, NienKhoa, BangDiem
from qlhs import db


def index():
    success_msg = ''
    if request.method.__eq__('POST'):
        id = request.form.get('id')
        name = request.form.get('name')
        ngaysinh = request.form.get('ngaysinh')
        sex = request.form.get('sex')
        SDT = request.form.get('SDT')
        diachi = request.form.get('diachi')
        email = request.form.get('email')

        try:
            utils.add_students(id=id, name=name,
                               ngaysinh=ngaysinh,
                               sex=sex,
                               SDT=SDT,
                               diachi=diachi,
                               email=email)
            success_msg = 'Tiếp nhận thành công'
        except:
            success_msg = 'Tiếp nhận  thất bại'
    return render_template('index.html', success_msg=success_msg)


def students():
    a = models.Students.query.all()
    return render_template('students.html', students=a)
