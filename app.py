import pyautogui as pa
import time
import pyperclip
from auto import Operation as Op
from auto import InputNum
import pyscreeze
import glob

# 类实例化
tf = Op.CLICK()

# 把输入的数据转化成数组
cleaned_list = InputNum.arr()

# 素材名字
sucaimingcheng = cleaned_list[0]
# 出价
chujia = cleaned_list[1]
# 编辑当天计划的名字
jihuaName = cleaned_list[2]
# 账户选择
zhanghu = cleaned_list[3]
# 商品号
shangpinnum = cleaned_list[4]

# 操控鼠标点击“投放商品”
temp = pa.locateAllOnScreen("Judgment/toufanganniu.png", confidence=0.8)
if temp:
    for x in temp:
        center = pa.center(x)  # type:ignore
        c_x = center.x
        c_y = center.y
        tf.yidongdingwei(c_x, c_y, 1, 1)
        break
else:
    print('图片未识别')
    exit()
time.sleep(2)
# 对点击后的页面进行判断，如果页面正常打开则跳出循环，如果页面没有打开则进入循环
i = 0
while True:
    i += 1
    time.sleep(1)
    # 判定页面是否加载出来了
    fd = tf.Php_Mv('Judgment/QUTF.png', i)
    if fd:
        break
    else:
        # 5秒刷新，10秒后退出程序
        if i == 5:
            tf.yidongdingwei(94, 58, 1, 0.5)
        if i == 10:
            tf.yidongdingwei(94, 58, 1, 0.5)
        if i == 15:
            print("图片未识别，终止程序")
            exit()



###########################################################

# 移动到选择抖音号那一列，然后点击，给列展开，并识别账户的像素点,如果正常识别则进行移动操作，并确认
# 如果没有正常识别，则跳出循环
tf.yidongdingwei(693, 288, 1, 0.5)
i = 0
while True:
    i += 1
    time.sleep(1)
    # 移动到账户列表上，进行点击操作
    # 识别图片
    fd_A = tf.Php_Mv(f'Account/{zhanghu}.png', i)
    if fd_A:
        # 移动到账户上进行点击
        tf.Photoshop(f'Account/{zhanghu}.png')
        time.sleep(1)
        # 识别账号变更提示出来没有
        fd_A_a = tf.Php_Mv('Judgment/querengenggai.png', i)
        time.sleep(1)
        # 判断是否有出现账号变更的提示，如有提示点击确认
        if fd_A_a:
            tf.yidongdingwei(1133, 603, 1, 0.5)
        # 完成操作后跳出循环
        break
    else:
        pa.moveTo(738, 445, 0.5)
        pa.scroll(-200)
        print(f'找不到账户下滑{i}次')
        # 5秒刷新，10秒后退出程序
        if i == 5:
            tf.yidongdingwei(94, 58, 1, 0.5)
            time.sleep(1)
            tf.yidognxiahua(170, 649, "+1500")
            time.sleep(1)
            tf.yidongdingwei(693, 288, 1, 0.5)
            time.sleep(1)
        if i == 10:
            print("账户未识别，终止程序")
            exit()

#######################################################

# 开始添加商品
# 移动到添加商品的位置进行点击操作
tf.yidongdingwei(512, 370, 1, 0.5)
time.sleep(4)
i = 0
while True:
    i += 1
    time.sleep(1)
    # 判断商品页面加载出来了没有（图片）
    fd_P = tf.Php_Mv('Judgment/shangpinpanduan.png', 1)
    if fd_P:
        # 移动到输入框，输入商品号
        tf.yidongdingwei(1001, 256, 1, 0.5)
        # 输入内容
        tf.shuru(shangpinnum)
        time.sleep(3)
        # 移动到商品位置点击选择
        tf.yidongdingwei(988, 450, 1, 0.5)
        # 点击确认
        tf.yidongdingwei(1851, 1006, 1, 0.5)
        # 完成之后跳出循环
        break
    else:
        # 5秒刷新，10秒后退出程序
        if i == 5:
            # 先移动到空白地方进行点击
            tf.yidongdingwei(236, 740, 1, 0.5)
            # 然后移动到刷新按钮上进行点击
            tf.yidongdingwei(94, 58, 1, 0.5)
            time.sleep(4)
            # 再次移动到添加商品，进行点击
            tf.yidongdingwei(512, 370, 1, 0.5)
            time.sleep(5)
        if i == 10:
            print("图片未识别，终止程序")
            exit()

# 添加预算更改净成交
i = 0
while True:
    i += 1
    time.sleep(1)
    # 判定页面是否加载出来了
    fd = tf.Php_Mv('Judgment/dunpai.png', i)
    if fd:
        break
    else:
        # 5秒刷新，10秒后退出程序
        if i == 5:
            tf.yidongdingwei(94, 58, 1, 0.5)
        if i == 10:
            print("图片未识别，终止程序")
            exit()

# 添加预算
# 移动到控成本投放，然后点击切换
tf.yidongdingwei(611, 641, 1, 0.5)
# 移动到‘日预算’输入框，然后点击
tf.yidongdingwei(514, 794, 1, 0.5)
# 输入文本
tf.shuru(500)

# 更改净成交
# 移动到净成交输入框，然后点击
tf.yidongdingwei(998, 781, 1, 0.5)
# 循环四次进行删除系统的价格
for tmp in range(0, 4):
    pa.press('Backspace')
# 输入自己的出价
tf.shuru(chujia)

# 往下滑动直至最下面的页面
tf.yidognxiahua(1601, 656, "-1000")
time.sleep(1)

# 素材设置
# 移动到自选投放素材，点击进行切换（图片）
tf.Photoshop('Judgment/sucai1.png')

# 添加素材的商品，然后点击商品添加（图片）
tf.Photoshop('Judgment/sucaishangpin.png')
tf.Photoshop('Judgment/sucaishangpin111.png')

# 往下滑动直至最下面的页面
tf.yidognxiahua(170, 649, "-1000")
time.sleep(1)

######################################################################

# 添加素材

# 添加一个判断，万一添加视频这个按钮找不到，比如网页下面多了行东西，这可以自动网上移动
i = 0
while True:
    i += 1
    found = False
    temp = pa.locateAllOnScreen("Judgment/tianjiasucaipanduan.png", confidence=0.8)
    try:
        for x in temp:
            center = pa.center(x)  # type:ignore
            tf.Photoshop('Judgment/tianjiashipin.png')
            found = True
            break
    except:
        tf.yidognxiahua(227, 677, "+300")
    if found:
        break
    if i == 5:
        exit()

i = 0
while True:
    i += 1
    # 判定页面是否加载出来了
    fd_J = tf.Php_Mv('Judgment/sucaishangchuan.png', i)
    time.sleep(1)
    if fd_J:
        time.sleep(1)
        # 点击视频来源列表
        tf.Photoshop('Judgment/shipinlaiyuanliebiao.png')
        # 开始选择视频来源
        tf.Photoshop('Judgment/bendishangchuan.png')
        # 移动到空白位置点击一下
        tf.yidongdingwei(1494, 112, 1, 0.5)
        # 移动到输入框点击一下，输入视频名称
        tf.yidongdingwei(946, 252, 1, 0.5)
        # 输入素材名称
        tf.shuru(sucaimingcheng)
        # 等待加载
        time.sleep(3)
        # 移动到复选框点击全选
        tf.Photoshop('Judgment/benyequanxuan.png')
        # 点击确定按钮
        # 可以优化
        tf.yidongdingwei(1855, 1011, 1, 0.5)
        break
    else:
        # 5秒往上滑动，10秒后退出程序
        if i == 5:
            # tf.yidongdingwei(94, 58, 1, 0.5)
            # tf.Photoshop('Judgment/tianjiashipin.png')
            pass
        if i == 10:
            print("图片未识别，终止程序")
            exit()

######################################################################


# 往下滑动直至最下面的页面
tf.yidognxiahua(227, 677, "-1500")
time.sleep(1)

# 移动到添加标题的位置（图片）
i = 0
while True:
    i += 1
    temp = pa.locateAllOnScreen("Judgment/table.png", confidence=0.8)
    found = False
    try:
        for x in temp:
            center = pa.center(x)  # type: ignore
            print(f"中心点坐标{center}")
            pa.click(center, clicks=5, duration=0.5, interval=0.5)
            print(f"找到图片了")
            found = True
            break
    except pyscreeze.ImageNotFoundException:
        time.sleep(1)
        print(f'程序找不到图片,第{i}次')
        if i == 5:
            print("错误：找不到此路径下:Judgment/table.png的图片无法进行点击操作，程序终止")
            exit()
    if found:
        break

# 往下滑动到最下面
tf.yidognxiahua(227, 677, "-1000")
time.sleep(1)

# 获取biaotiwenben文件夹下面的文本文件
text_files = glob.glob("biaotiwenben/*.txt")
# 打开文本读取数据，填入文字
with open(text_files[0], 'r', encoding='utf-8') as f:
    content = f.read()
    len_num = [line for line in content.splitlines() if line.strip()]
f.close()

# 标题定位
z_x = 0
z_y = 0
temp = pa.locateAllOnScreen("Judgment/biaotidingwei.png", confidence=0.8)
for x in temp:
    center = pa.center(x)  # type:ignore
    # print(f"中心点坐标{center}")
    # pa.moveTo(center, duration=0.5)
    z_x = center.x
    z_y = center.y
    break

# 循环增加y值,自动添加文字
z_y = z_y - 60
for i in range(len(len_num)):
    # 移动位置
    tf.yidongdingwei(z_x, z_y, 1, 0.5)
    # 输入文本
    tf.shuru(len_num[i])
    z_y -= 41

# 往下滑动直至最下面的页面
tf.yidognxiahua(139, 566, "-500")
time.sleep(1)

# 发布计划
# 移动到计划名称输入框，然后点击
tf.yidongdingwei(661, 877, 1, 0.5)
# 给系统名字全选然后删除
pa.hotkey('ctrl', 'a')
pa.press('Backspace')


# 使用strftime()自定义格式,编辑计划的名称
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
data_list = formatted_time.split(' ')
JN = data_list[0] + '_' + jihuaName + '_' + data_list[1]


# 填入自己编辑的名字
tf.shuru(JN)


# 点击发布计划
tf.yidongdingwei(472, 964, 1, 0.5)

















