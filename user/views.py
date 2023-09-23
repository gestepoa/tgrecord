from flask_restful import Resource
from user.models import User, BasicInfo,EduInfo,Family
from database import db
from utils import db_util, query_util
from flask import request, jsonify
import json

# User
class UserView(Resource):

    def get(self):
        users = EduInfo.query.filter().all()
        return db_util.query_to_dict(users)

    def post(self):
        data = json.loads(request.data)
        user = User(username=data.get('username'), password=data.get('password'), email=data.get('email'))
        db.session.add(user)
        return db_util.query_to_dict(user)

# BasicInfo
class BasicInfoViewQuery(Resource):
    
    def get_request(self, request_data):
        if request_data.data.decode('utf-8') == '':
            filter_conditions = {}
            relation_conditions = {}
            paginate_conditions = {}
        else: 
            params = request_data.json
            valid_keys = [key for key in params if key in BasicInfo.__table__.columns]
            relation_keys = [key for key in params if key in BasicInfo.__mapper__.relationships]
            paginate_keys = [key for key in params if key in ["page", "per_page"]]
            filter_conditions = {key: params[key] for key in valid_keys}
            relation_conditions = {key: params[key] for key in relation_keys}
            paginate_conditions = {key: params[key] for key in paginate_keys}
        return filter_conditions, relation_conditions, paginate_conditions

    def post(self):
        try:
            filter_conditions, relation_conditions, paginate_conditions = self.get_request(request)    
            page = paginate_conditions.get('page', 1)
            per_page = paginate_conditions.get('per_page', 10)
            results = BasicInfo.query.filter_by(**filter_conditions).order_by(BasicInfo.id.desc()).paginate(page=page, per_page=per_page)
            data = []
            for result in results:
                # get familyinfo record
                results_familyinfo = []
                familyinfo_params = relation_conditions.get('familyinfo', {})
                for family in result.familyinfo:
                    results_familyinfo_single = {
                        "id": family.id,
                        "name": family.name,
                        "relation": family.relation
                    }
                    if query_util.check_dict_equality(results_familyinfo_single, familyinfo_params):
                        results_familyinfo.append(results_familyinfo_single)
                # get eduinfo record
                results_eduinfo = []
                eduinfo_params = relation_conditions.get('eduinfo', {})
                for eduinfo in result.eduinfo:
                    results_eduinfo_single = {
                        "id": eduinfo.id,
                        "level": eduinfo.level,
                        "school_name": eduinfo.school_name
                    }
                    if query_util.check_dict_equality(results_eduinfo_single, eduinfo_params):
                        results_eduinfo.append(results_eduinfo_single)
                # get main table record
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
