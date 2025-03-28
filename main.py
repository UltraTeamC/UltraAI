import random
import time
import sys
import os
from question import q1
from question import q2
from question import q3
from uinput   import i1
from uinput   import i2
from uinput   import i3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

while 5>3:
    uinput = str(input("我是UltraAI[v0.22]测试版，你有什么问题可以向我提问："))
    if i1.B000001 in uinput:
        q1.B000001()        
    elif i1.H000001 in uinput:
        q1.H000001()
    elif i1.H000002 in uinput:
        q1.H000002()        #文字游戏
    elif i1.H000003 in uinput:
        q1.H000003()
    elif i1.I000001 in uinput:
        i1.I000001()
    elif i1.J000001 in uinput:
        q1.J000001()        #脏话
    elif i1.J000002 in uinput:
        q1.J000002()        #脏话
    elif i1.A000001 in uinput:
        q1.A000001()        #关于自然的文章
    else:
        print("UltraAI还才疏学浅，问他一些简单的问题吧!")