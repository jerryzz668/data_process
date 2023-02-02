import numpy as np
import os, time
from utils import read_txt, write_txt

# test_path = 'data_analysis/log/ori_log/demo_d_current_pop-02-01.txt'
test_path = 'data_analysis/log/ori_log/demo_d_new_population-02-01.txt'
# test_path = 'data_analysis/log/ori_log/demo_c_current_pop-01-30.txt'
new_name = os.path.basename(test_path).split('.')[0] + '_format.txt'
format_save_path = os.path.join(os.path.dirname(test_path), new_name)

save_path = os.path.join('data_analysis/log/log', os.path.basename(test_path))

lines = read_txt(test_path)
for line in lines:
    if line[-2:] == ',\n':
        line = line.strip('\n')  # strip()表示删除掉数据中的换行符
    write_txt(line, format_save_path)

# time.sleep(2)
data = read_txt(format_save_path)

for i in range(len(data)):
    data[i] = data[i].replace('array(', '')
    data[i] = data[i].replace(')', '')
    data[i] = data[i].replace('[', '')
    data[i] = data[i].replace(']', '')
    write_txt(data[i], save_path)

