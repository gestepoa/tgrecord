import random
import string

def check_dict_equality(dict1, dict2):
    for key, value1 in dict1.items():
        if key in dict2:
            value2 = dict2[key]
            if value1 != value2:
                return False
    return True


def get_sub(main_table_class):
    for relationship, sub_class_name in main_table_class.__mapper__.relationships.items():
        print("this is the relation name")
        print(relationship)
        print('this is the class name')
        print(sub_class_name.mapper.class_.__name__)


def get_request(table_class, request_data):
    if request_data.data.decode('utf-8') == '':
        filter_conditions = {}
        relation_conditions = {}
        paginate_conditions = {}
    else: 
        params = request_data.json
        valid_keys = [key for key in params if key in table_class.__table__.columns]
        relation_keys = [key for key in params if key in table_class.__mapper__.relationships]
        paginate_keys = [key for key in params if key in ["page", "per_page"]]
        filter_conditions = {key: params[key] for key in valid_keys}
        relation_conditions = {key: params[key] for key in relation_keys}
        paginate_conditions = {key: params[key] for key in paginate_keys}
    return filter_conditions, relation_conditions, paginate_conditions


def generate_random_code(filter_conditions):
    code_back = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    birthday = filter_conditions.get('birthday')
    code_front = 'ID' + birthday.replace('-', '')
    return code_front + code_back
