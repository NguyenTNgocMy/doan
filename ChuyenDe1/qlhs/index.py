from flask import render_template, request, redirect, session
from qlhs import utils, app, models,controllers
from qlhs.models import User, Students, MonHoc, DSLop, NienKhoa, BangDiem




app.add_url_rule('/', 'index', controllers.index)
app.add_url_rule('/students', 'students', controllers.students)

if __name__ == '__main__':
    app.run(debug=True)