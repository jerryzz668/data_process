
import time

current_time = int(time.time())  # 1631186249
localtime = time.localtime(current_time)  # 转换为localtime
dt = time.strftime('%Y-%m-%d %H:%M:%S', localtime)  # 利用strftime()函数重新格式化时间
print(dt)
