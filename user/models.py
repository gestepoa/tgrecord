from database import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=False, nullable=True)
    password = db.Column(db.String(255), unique=False, nullable=True)
    note = db.Column(db.String(255), unique=False, nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_time = db.Column(db.DateTime, default=None, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username


class BasicInfo(db.Model):
    __tablename__ = 'basic_info'

    id = db.Column(db.Integer, primary_key=True, comment="基础信息id")
    name = db.Column(db.String(255), unique=False, nullable=False, comment="姓名")
    gender = db.Column(db.String(255), unique=False, nullable=True, comment="性别")
    ethnic = db.Column(db.String(255), unique=False, nullable=True, comment="民族")
    ancestral_province = db.Column(db.String(255), unique=False, nullable=True, comment="籍贯省份")
    ancestral_local = db.Column(db.String(255), unique=False, nullable=True, comment="籍贯县市")
    birthplace_province = db.Column(db.String(255), unique=False, nullable=True, comment="出生省份")
    birthplace_local = db.Column(db.String(255), unique=False, nullable=True, comment="出生县市")
    birthday = db.Column(db.DateTime, unique=False, nullable=True, comment="出生年份")
    participate = db.Column(db.Integer, unique=False, nullable=True, comment="入党年份")
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_time = db.Column(db.DateTime, default=None, nullable=True)
    eduinfo = db.relationship('EduInfo', backref='basicinfo', lazy='dynamic')
    familyinfo = db.relationship('Family', backref='basicinfo', lazy='dynamic')

    def __repr__(self):
        return '<BasicInfo %r>' % self.name


class EduInfo(db.Model):
    __tablename__ = 'edu_info'

    id = db.Column(db.Integer, primary_key=True, comment="教育信息id")
    level = db.Column(db.String(255), unique=False, nullable=False, comment="教育等级")
    school_province = db.Column(db.String(255), unique=False, nullable=True, comment="学校所在省")
    school_local = db.Column(db.String(255), unique=False, nullable=True, comment="学校所在县市")
    school_name = db.Column(db.String(255), unique=False, nullable=False, comment="学校名称")
    enrollment = db.Column(db.DateTime, unique=False, nullable=True, comment="入学时间")
    isnational = db.Column(db.String(255), unique=False, nullable=True, comment="是否是国内高校")
    remarks = db.Column(db.String(255), unique=False, nullable=True, comment="备注")
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_time = db.Column(db.DateTime, default=None, nullable=True)
    basic_info_id = db.Column(db.Integer, db.ForeignKey('basic_info.id'))

    def __repr__(self):
        return '<edu_info %r>' % self.school_name


class Family(db.Model):
    __tablename__ = 'family'

    id = db.Column(db.Integer, primary_key=True, comment="家族信息id")
    name = db.Column(db.String(255), unique=False, nullable=False, comment="姓名")
    relation = db.Column(db.String(255), unique=False, nullable=False, comment="关系")
    birthday = db.Column(db.DateTime, unique=False, nullable=True, comment="出生日期")
    remarks = db.Column(db.String(255), unique=False, nullable=True, comment="备注")
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_time = db.Column(db.DateTime, default=None, nullable=True)
    basic_info_id = db.Column(db.Integer, db.ForeignKey('basic_info.id'))

    def __repr__(self):
        return '<family %r>' % self.name
