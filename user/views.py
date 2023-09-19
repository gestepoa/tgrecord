from flask_restful import Resource
from user.models import User, BasicInfo,EduInfo,Family
from database import db
from utils import db_util
from flask import request, jsonify
import json

# User
class UserView(Resource):

    def get(self):
        users = User.query.filter().all()
        return db_util.query_to_dict(users)
        # results = db.session.query(BasicInfo, EduInfo, Family).join(EduInfo).join(Family).all()
        # for result in results:
        #     print(result)

    def post(self):
        data = json.loads(request.data)
        user = User(username=data.get('username'), password=data.get('password'), email=data.get('email'))
        db.session.add(user)
        return db_util.query_to_dict(user)

# BasicInfo
class BasicInfoViewQuery(Resource):
    
    def get_request(self, request_data):
        if request_data.data.decode('utf-8') == '':
            params = {}
        else: 
            params = request_data.json
        return params

    def get_relationships(self, model_name):
        relation = []
        all_relationships = model_name.__mapper__.relationships
        for relationship in all_relationships:
            relation.append(relationship.key)
        return relation

    def post(self):
        try:
            params = self.get_request(request)
            #get filter_conditions
            valid_keys = [key for key in params if key in BasicInfo.__table__.columns]
            filter_conditions = {key: params[key] for key in valid_keys}
            print(filter_conditions)
            # get relation
            relation = self.get_relationships(BasicInfo)
            print(relation)
            # get pagination
            page = params.get('page', 1)
            per_page = params.get('per_page', 10)
            results = BasicInfo.query.filter_by(**filter_conditions).order_by(BasicInfo.id.desc()).paginate(page=page, per_page=per_page)
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
        except Exception as e:
            return {
                'message': 'DataBase error: {}'.format(str(e)),
                'status': 500
            }


class BasicInfoViewAdd(Resource):

    def post(self):
        try:
            data = json.loads(request.data)
            result = BasicInfo(name=data.get('name'), birth=data.get('birth'), birthday=data.get('birthday'))
            db.session.add(result)
            db.session.commit()
            return {
                'message': 'success',
                'status': 200
            }
        except Exception as e:
            return {
                'message': 'DataBase error: {}'.format(str(e)),
                'status': 500
            }


class BasicInfoViewUpdate(Resource):

    def post(self):
        try:
            data = json.loads(request.data)
            params_id = data.get('id')
            result = BasicInfo.query.filter_by(id=params_id).first()
            result.ethnic = data.get('ethnic')
            db.session.commit()
            return {
                'message': 'success',
                'status': 200
            }
        except Exception as e:
            return {
                'message': 'DataBase error: {}'.format(str(e)),
                'status': 500
            }

class BasicInfoViewDelete(Resource):

    def post(self):
        try:
            data = json.loads(request.data)
            params_id = data.get('id')
            result = BasicInfo.query.filter_by(id=params_id).first()
            db.session.delete(result)
            db.session.commit()
            return {
                'message': 'success',
                'status': 200
            }
        except Exception as e:
            return {
                'message': 'DataBase error: {}'.format(str(e)),
                'status': 500
            }
