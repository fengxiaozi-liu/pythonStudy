import json, pickle

base_dir = 'file/'


def open_dir(file_name):
    with open(base_dir + file_name, 'r', encoding='utf8') as file:
        content = file.read()
        return content


def read_json(file_name):
    file = base_dir + file_name
    old_data = json.load(open(file, 'r'))
    return old_data


def write_json(data, file_name):
    file = base_dir + file_name
    json.dump(data, open(file, 'w'))


def read_pickle(file_name):
    file = base_dir + file_name
    old_data = pickle.load(open(file, 'rb'))
    return old_data


def write_pickle(data, file_name):
    file = base_dir + file_name
    pickle.dump(data, open(file, 'wb'))



