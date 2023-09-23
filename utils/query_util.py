
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
