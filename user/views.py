from flask_restful import Resource
from user.models import User, BasicInfo
from database import db
from utils import db_util
from flask import request, jsonify
import json


class UserView(Resource):
    # get方法
    def get(self):
        users = User.query.filter().all()
        return db_util.query_to_dict(users)

    # post方法
    def post(self):
        data = json.loads(request.data)
        user = User(username=data.get('username'), password=data.get('password'), email=data.get('email'))
        db.session.add(user)
        return db_util.query_to_dict(user)


class BasicInfoView(Resource):

    def get(self):
        results = BasicInfo.query.all()
        data = []
        for result in results:
            # 获取子表1内容
            results_familyinfo = []
            for family in result.familyinfo:
                results_familyinfo_single = {
                    "id": family.id,
                    "name": family.name,
                    "relation": family.relation
                }
                results_familyinfo.append(results_familyinfo_single)
            # 获取子表2内容
            results_eduinfo = []
            for eduinfo in result.eduinfo:
                results_eduinfo_single = {
                    "id": eduinfo.id,
                    "level": eduinfo.level,
                    "school_name": eduinfo.school_name
                }
                results_eduinfo.append(results_eduinfo_single)
            # 获取主表信息
            result_data = {
                "id": result.id,
                'name': result.name,
                "gender": result.gender,
                "ethnic": result.ethnic,
                'familyinfo': results_familyinfo,
                'eduinfo': results_eduinfo
            }
            data.append(result_data)
        return jsonify(data)

    def post(self):
        data = json.loads(request.data)
        result = BasicInfo(name=data.get('name'))
        db.session.add(result)
        db.session.commit()
        return db_util.query_to_dict(result)
