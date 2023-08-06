import os
from utils import read_txt, instance_to_json

input_path = '/home/jerry/Documents/dataset/demo_new2/'
save_path = 'route.json'
routes = []
filelist = os.listdir(input_path)
for file in filelist:
    new_product_file = os.path.join(input_path, file)
    data = read_txt(new_product_file)
    for line in data:
        if '---' in line:
            route = line.split('],')[-1].strip()
            print(route)
            routes.append(route)

routes = list(set(routes))
routes.sort()
instance_to_json(routes, save_path)