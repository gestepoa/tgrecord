from database import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, comment="用户id")
    username = db.Column(db.String(255), unique=False, nullable=False, comment="用户名")
    email = db.Column(db.String(255), unique=False, nullable=True, comment="邮箱")
    password = db.Column(db.String(255), unique=False, nullable=True, comment="密码")
    note = db.Column(db.String(255), unique=False, nullable=True, comment="备注")
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_time = db.Column(db.DateTime, default=None, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username


class BasicInfo(db.Model):
    __tablename__ = 'basic_info'

    id = db.Column(db.Integer, primary_key=True, comment="基础信息id")
    code = db.Column(db.String(255), unique=True, nullable=True, comment="编号")
    name = db.Column(db.String(255), unique=True, nullable=False, comment="姓名")
    gender = db.Column(db.String(255), unique=False, nullable=True, comment="性别")
    ethnic = db.Column(db.String(255), unique=False, nullable=True, comment="民族")
    ancestral_province = db.Column(db.String(255), unique=False, nullable=True, comment="籍贯省份")
    ancestral_local = db.Column(db.String(255), unique=False, nullable=True, comment="籍贯县市")
    birthplace_province = db.Column(db.String(255), unique=False, nullable=True, comment="出生省份")
    birthplace_local = db.Column(db.String(255), unique=False, nullable=True, comment="出生县市")
    birth = db.Column(db.String(255), unique=False, nullable=True, comment="出生年份")
    birthday = db.Column(db.Date, unique=False, nullable=True, comment="出生日期")
    participate = db.Column(db.Integer, unique=False, nullable=True, comment="入党年份")
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_time = db.Column(db.DateTime, default=None, nullable=True)
    eduinfo = db.relationship('EduInfo', backref='basicinfo', lazy='dynamic', cascade='all, delete-orphan')
    familyinfo = db.relationship('Family', backref='basicinfo', lazy='dynamic', cascade='all, delete-orphan')
    resumeinfo = db.relationship('Resume', backref='basicinfo', lazy='dynamic', cascade='all, delete-orphan')
    ideologyinfo = db.relationship('Ideology', backref='basicinfo', lazy='dynamic', cascade='all, delete-orphan', uselist=False)

    def __repr__(self):
        return '<BasicInfo %r>' % self.name


class EduInfo(db.Model):
    __tablename__ = 'edu_info'

    id = db.Column(db.Integer, primary_key=True, comment="教育信息id")
    level = db.Column(db.String(255), unique=False, nullable=False, comment="教育等级")
    school_province = db.Column(db.String(255), unique=False, nullable=True, comment="学校所在省")
    school_local = db.Column(db.String(255), unique=False, nullable=True, comment="学校所在县市")
    school_name = db.Column(db.String(255), unique=False, nullable=False, comment="学校名称")
    enrollment = db.Column(db.Date, unique=False, nullable=True, comment="入学时间")
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
    birthday = db.Column(db.Date, unique=False, nullable=True, comment="出生日期")
    remarks = db.Column(db.String(255), unique=False, nullable=True, comment="备注")
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_time = db.Column(db.DateTime, default=None, nullable=True)
    basic_info_id = db.Column(db.Integer, db.ForeignKey('basic_info.id'))

    def __repr__(self):
        return '<family %r>' % self.name


class Resume(db.Model):
    __tablename__ = 'resume'

    id = db.Column(db.Integer, primary_key=True, comment="履历信息id")
    target = db.Column(db.String(255), unique=False, nullable=False, comment="目标人物")
    province = db.Column(db.String(255), unique=False, nullable=True, comment="所在省份")
    local = db.Column(db.String(255), unique=False, nullable=True, comment="所在县市")
    govpos = db.Column(db.String(255), unique=False, nullable=True, comment="职务")
    domains = db.Column(db.String(255), unique=False, nullable=True, comment="领域")
    time = db.Column(db.Integer, unique=False, nullable=True, comment="起始年份")
    duration = db.Column(db.Integer, unique=False, nullable=True, comment="持续时间（年）")
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_time = db.Column(db.DateTime, default=None, nullable=True)
    basic_info_id = db.Column(db.Integer, db.ForeignKey('basic_info.id'))

    def __repr__(self):
        return '<resume %r>' % self.target


class Position(db.Model):
    __tablename__ = 'position'

    id = db.Column(db.Integer, primary_key=True, comment="职务信息id")
    name = db.Column(db.String(255), unique=False, nullable=True, comment="姓名")
    position_name = db.Column(db.String(255), unique=False, nullable=True, comment="职务名称")
    position_domains = db.Column(db.String(255), unique=False, nullable=True, comment="职务领域")
    position_level = db.Column(db.String(255), unique=False, nullable=True, comment="职务等级")
    note = db.Column(db.String(255), unique=False, nullable=True, comment="说明")
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_time = db.Column(db.DateTime, default=None, nullable=True)

    def __repr__(self):
        return '<posiiton %r>' % self.position_name


class Ideology(db.Model):
    __tablename__ = 'ideology'

    id = db.Column(db.Integer, primary_key=True, comment="意识形态id")
    orientation = db.Column(db.Enum('激进', '保守', '不作为'), unique=False, nullable=True, comment="政治倾向")
    economic_view = db.Column(db.Enum('国家资本主义', '自由经济', '斯大林模式'), unique=False, nullable=True, comment="经济观点")
    nation_view = db.Column(db.Enum('汉族主义', '完整公民权', '中华民族'), unique=False, nullable=True, comment="民族观点")
    war_view = db.Column(db.Enum('沙文主义', '和平主义'), unique=False, nullable=True, comment="战争观点")
    political_view = db.Column(db.Enum('精英政治', '民粹主义'), unique=False, nullable=True, comment="政治观点")
    ideology_cpc = db.Column(db.Enum('毛泽东思想', '中国特色社会主义', '新时代思想'), unique=False, nullable=True, comment="中共意识形态")
    family_background = db.Column(db.Enum('贵族', '平民'), unique=False, nullable=True, comment="家庭出身")
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    delete_time = db.Column(db.DateTime, default=None, nullable=True)
    basic_info_id = db.Column(db.Integer, db.ForeignKey('basic_info.id'))

    def __repr__(self):
        return '<ideology %r>' % self.orientation