def read_txt(path):
    with open(path, "r", encoding='utf-8') as f:  # 打开文件
        data = f.readlines()  # 读取文件
    return data

def write_txt(content, path):
    with open(path, "a", encoding='utf-8') as f:  # 打开文件
        f.write(content)  # 读取文件