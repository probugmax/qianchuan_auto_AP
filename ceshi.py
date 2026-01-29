import pyautogui
import pyautogui as pa
import time
from auto import Operation
import threading
from pynput import keyboard
import pyscreeze

tf = Operation.CLICK()


class a:
    def x(self, p, y):
        abc = p + y
        return abc

    def y(self, p, x):
        abc = x * p
        return abc

    def yuan(self, x):
        print(x)
        return x

    def photoshop(self, lujing: str):
        temp = pa.locateAllOnScreen(a, confidence=0.8)
        try:
            for i in temp:
                center = pa.center(i)
                print(f"中心点坐标{center}")
                pa.click(center, clicks=2)
                break
        except pyscreeze.ImageNotFoundException:
            print('程序找不到图片')
            pa.alert("程序找不到图片", "错误")  # type: ignore

    def P(self, lujing: str, tim):
        temp = pa.locateAllOnScreen(lujing, confidence=0.8)
        try:
            for i in temp:
                print(f"找到图片了,坐标为{i}")
                return True
        except pyscreeze.ImageNotFoundException:
            print(f"问题:在此路径下{lujing}找不到指定图片,已等待{tim}秒")


a = a()

zhanghu = 'mobai'

fd_A = a.P(f'Account/{zhanghu}.png', 1)



# i = 0
# while True:
#     temp = pa.locateAllOnScreen(c, confidence=0.8)
#     found = False
#     try:
#         for i in temp:
#             center = pa.center(i)
#             print(f"中心点坐标{center}")
#             # pa.click(center, clicks=2)
#             print(f"找到图片了坐标是{i}")
#             found = True
#             break
#     except pyscreeze.ImageNotFoundException:
#         i += 1
#         print(f'{i}程序找不到图片')
#         # pa.alert("程序找不到图片", "错误")  # type: ignore
#         time.sleep(1)
#         if i == 5:
#             print("问题:找不到账户图片无法进行点击操作")
#             pa.alert("找不到账户图片", "提示")  # type:ignore
#             exit()
#
#     if found:
#         break

# ft.yidongdingwei(376, 493, 1, 0.5)
# for i in range(0, 4):
#     pa.press('Backspace')

# 填入文字
# len_num = [
#     '越用越好用的澡巾，一个用一年',
#     '这还是我用过超好用的搓澡巾了，超级下泥还不疼，而且还是三利大品牌的质量嘎嘎好！',
#     '搓澡的时候你就上下搓，嘎嘎下泥还不疼，它里面是一层一层细沙。',
#     '特别适合我们这种怕疼的，而且还是海绵宝宝联名款，真的太可爱了。',
#     '趁现在价格合适赶紧冲组合装更优惠~ 大人小孩都可以用。'
# ]
# with open('biaotiwenben/bt.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
#     len_num = [line for line in content.splitlines() if line.strip()]
# f.close()
#
# zb = 187
# for i in range(len(len_num)):
#     tf.yidongdingwei(zb, 327, 1, 0.5)
#     pa.hotkey('ctrl', 'a')
#     pa.press('Backspace')
#     # 输入文本
#     tf.shuru(len_num[i])
#     zb += 41

# for i in range(0, len(len_num)):
#     if i == 0:
#         # 移动到第五个输入框，然后点击
#         tf.yidongdingwei(187, 327, 1, 0.5)
#         pa.hotkey('ctrl', 'a')
#         pa.press('Backspace')
#         # 输入文本
#         tf.shuru(len_num[i])
#     elif i == 1:
#         tf.yidongdingwei(545, 373, 1, 0.5)
#         pa.hotkey('ctrl', 'a')
#         pa.press('Backspace')
#         tf.shuru(len_num[i])
#     elif i == 2:
#         tf.yidongdingwei(912, 301, 1, 0.5)
#         pa.hotkey('ctrl', 'a')
#         pa.press('Backspace')
#         tf.shuru(len_num[i])
#     elif i == 3:
#         tf.yidongdingwei(1246, 373, 1, 0.5)
#         pa.hotkey('ctrl', 'a')
#         pa.press('Backspace')
#         tf.shuru(len_num[i])
#     elif i == 4:
#         tf.yidongdingwei(1602, 331, 1, 0.5)
#         pa.hotkey('ctrl', 'a')
#         pa.press('Backspace')
#         tf.shuru(len_num[i])
