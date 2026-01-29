import pyautogui as pa
import time
import pyperclip
import pyscreeze

class CLICK:
    # 进行移动点击的操作
    # a,b 是屏幕位置坐标
    # clicks点击次数
    # tm 是移动到目标位置时间
    def yidongdingwei(self, a, b, clicks, tm):
        pa.moveTo(x=a, y=b, duration=tm)
        time.sleep(0.5)
        pa.click(clicks=clicks)

    # 获取当前位置的像素点，并且输出
    # a,b 是屏幕坐标
    def huoqu(self, a, b):
        sb = pa.screenshot()
        x = sb.getpixel((a, b))
        print(x)

    # 进行像素点判断，返回ture或fluse
    # a,b 是屏幕坐标
    # yuan 是屏幕坐标的像素点的rgb数值
    def panduan(self, a, b, yuan):
        result = pa.pixelMatchesColor(x=a, y=b, expectedRGBColor=yuan)
        return result

    # 移动到目标位置，点击一下，往下滑动
    # a,b 是屏幕坐标
    # scroll 是下滑数值
    def yidognxiahua(self, a, b, scroll: str):
        scroll = int(scroll)
        pa.click(x=a, y=b, clicks=1)
        pa.scroll(scroll)

    # 进行内容输入
    # str_ 是字符内容
    def shuru(self, str_):
        pyperclip.copy(str_)
        pa.hotkey('ctrl', 'v')
        pa.press('enter')

    # 找到图片进行点击，如果找到就进行移动点击，完成操作就跳出整个循环，找不到则等待
    def Photoshop(self, lujing: str):
        i = 0
        while True:
            temp = pa.locateAllOnScreen(lujing, confidence=0.8)
            found = False
            try:
                for x in temp:
                    center = pa.center(x)
                    print(f"中心点坐标{center}")
                    pa.click(center, clicks=1, duration=0.5)
                    print(f"找到图片了路径:{lujing}")
                    found = True
                    break
            except pyscreeze.ImageNotFoundException:
                i += 1
                time.sleep(1)
                print(f'程序找不到图片,第{i}次')
                if i == 5:
                    print(f"问题:找不到路径{lujing}图片无法进行点击操作")
                    # pa.alert("找不到账户图片,程序终止", "提示")  # type:ignore
                    exit()

            if found:
                break

    # 这段代码只找图片并且返回布尔值
    def Php_Mv(self, lujing: str, tim):
        temp = pa.locateAllOnScreen(lujing, confidence=0.8)
        try:
            for i in temp:
                print(f"找到图片{lujing}了,坐标为{i}")
                return True
        except pyscreeze.ImageNotFoundException:
            print(f"问题:在此路径下{lujing}找不到指定图片,已等待{tim}秒")





