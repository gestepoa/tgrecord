from flask_restful import Resource
from user.models import User, BasicInfo,EduInfo,Family
from database import db
from utils import db_util, query_util
from flask import request
import json
import math

# User
class UserView(Resource):

    def get(self):
        users = User.query.filter().all()
        return db_util.query_to_dict(users)

    def post(self):
        data = json.loads(request.data)
        user = User(username=data.get('username'), password=data.get('password'), email=data.get('email'))
        db.session.add(user)
        return db_util.query_to_dict(user)

# BasicInfo
class BasicInfoViewQuery(Resource):
    
    def post(self):
        try:
            filter_conditions, relation_conditions, paginate_conditions = query_util.get_request(BasicInfo, request)
            query = db.session.query(BasicInfo).filter_by(**filter_conditions).order_by(BasicInfo.id.desc())
            count = query.count()
            page = paginate_conditions.get('page', 1)
            per_page = paginate_conditions.get('per_page', 10)
            if math.ceil(count/per_page) < page:
                return {
                    'message': 'error: page exceed count',
                    'status': 501
                }
            results = query.paginate(page=page, per_page=per_page)
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
            return {
                'message': 'success',
                'status': 200,
                'data': data,
                'count': count,
                'page': page
            }
        except Exception as e:
            return {
                'message': 'DataBase error: {}'.format(str(e)),
                'status': 500
            }


class BasicInfoViewAdd(Resource):

    def post(self):
        try:
            filter_conditions, relation_conditions, paginate_conditions = query_util.get_request(BasicInfo, request)
            if not filter_conditions:
                return {
                    'message': 'error: request body empty',
                    'status': 501
                }
            result = BasicInfo(
                name=filter_conditions.get('name', ''),
                code=query_util.generate_random_code(filter_conditions),
                gender=filter_conditions.get('gender', ''), 
                ethnic=filter_conditions.get('ethnic', ''),
                birth=filter_conditions.get('birth', ''),
                birthday=filter_conditions.get('birthday')
            )
            # add eduinfo
            eduinfo_conditions = relation_conditions.get("eduinfo")
            if eduinfo_conditions:
                for eduinfo_condition in eduinfo_conditions:
                    eduinfo_result = EduInfo(
                        level=eduinfo_condition.get('level'),
                        school_name=eduinfo_condition.get('school_name')
                    )
                    result.eduinfo.append(eduinfo_result)
            # add familyinfo
            familyinfo_conditions = relation_conditions.get("familyinfo")
            if familyinfo_conditions:
                for familyinfo_condition in familyinfo_conditions:
                    familyinfo_result = Family(
                        name=familyinfo_condition.get('name'),
                        relation=familyinfo_condition.get('relation')
                    )
                    result.familyinfo.append(familyinfo_result)
            # add all
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
            filter_conditions, relation_conditions, paginate_conditions = query_util.get_request(BasicInfo, request)
            if not filter_conditions.get('id'):
                return {
                    'message': 'error: upodate id empty',
                    'status': 502
                }
            params_id = filter_conditions.get('id')
            result = BasicInfo.query.filter_by(id=params_id).first()
            if filter_conditions.get("gender"):
                result.gender = filter_conditions.get("gender")
            if filter_conditions.get("ethnic"):
                result.ethnic = filter_conditions.get("ethnic")
            if filter_conditions.get("ancestral_province"):
                result.ancestral_province = filter_conditions.get("ancestral_province")
            if filter_conditions.get("ancestral_local"):
                result.ancestral_local = filter_conditions.get("ancestral_local")
            if filter_conditions.get("birthplace_province"):
                result.birthplace_province = filter_conditions.get("birthplace_province")
            if filter_conditions.get("birthplace_local"):
                result.birthplace_local = filter_conditions.get("birthplace_local")
            if filter_conditions.get("birth"):
                result.birth = filter_conditions.get("birth")
            if filter_conditions.get("birthday"):
                result.birthday = filter_conditions.get("birthday")
            if filter_conditions.get("participate"):
                result.participate = filter_conditions.get("participate")
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
