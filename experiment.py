import tkinter as tk
import pynput as ut


window = tk.Tk()
window.title('鼠标位置')
window.geometry("500x120")

var = tk.StringVar()


# def insert_t():
#     t.delete("1.0", tk.END)   #button按钮弹起代码执行
#     pynput_n()
#

def pynput_n():
    with ut.mouse.Events() as event:
        for i in event:
            if isinstance(i,ut.mouse.Events.Click):
                global var
                t.delete("1.0", tk.END)
                var = f'({i.x},{i.y})'
                t.insert('insert',var)
                break



t = tk.Text(window,width=12,height=1,font=('宋体',30))
t.pack(side=tk.LEFT,anchor='nw',padx=10,pady=32)  # 设置text的位置


b = tk.Button(window,width=10,height=1,text='获取坐标',
              font=('宋体',20),command=pynput_n)
b.pack(side=tk.LEFT,anchor='nw',pady=30,padx=20) # 设置Button的位置

window.mainloop()