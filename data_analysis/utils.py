import json

def read_txt(path):
    with open(path, "r", encoding='utf-8') as f:  # 打开文件
        data = f.readlines()  # 读取文件
    return data

def write_txt(content, path):
    with open(path, "a", encoding='utf-8') as f:  # 打开文件
        f.write(content)  # 读取文件

def instance_to_json(instance, json_file_path):
    with open(json_file_path, 'w', encoding='utf-8') as f:
        content = json.dumps(instance, ensure_ascii=False, indent=2)
        f.write(content)