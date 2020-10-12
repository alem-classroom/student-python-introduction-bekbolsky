dict = {'first': 'первый', 'second': 'второй'}


def reverse_dict(dict):
    rev_dict = {}
    for key in dict.keys():
        new_key = dict[key]
        new_value = key
        rev_dict[str(new_key)] = str(new_value)
    return rev_dict


print(reverse_dict(dict))
