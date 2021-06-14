import os

def check_if_path_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)


def generate_paths(path,service_path,object_path):
    save_path = f'{path}{service_path}'
    check_if_path_exist(save_path)

    object_path = object_path.replace(" ","")

    save_path = f'{save_path}/{object_path}/'
    check_if_path_exist(save_path)

    return save_path