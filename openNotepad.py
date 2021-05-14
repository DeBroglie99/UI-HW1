from datetime import datetime
import os
from datetime import datetime
time = datetime.now().strftime('%Y%m%d%H%M%S')
title = time+".txt"
with open(title, 'w+') as f:
    print('新建NotePad\n',file = f)
    print('现在的时间是：\n' + time, file = f)

os.system(title)
# os.system('del /q time.txt')
