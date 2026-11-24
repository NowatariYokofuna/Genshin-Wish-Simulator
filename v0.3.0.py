# -*- coding: utf-8 -*-
import ctypes
from ctypes import wintypes
ctypes.windll.shcore.SetProcessDpiAwareness(-1)
import random
import os
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import json


print(os.getcwd())
print("Genshin Wish Simulator for Windows v0.3.0")
print("(C) Copyright 2026 Gamedraw.Studio")
print("软件还在测试中，有任何bug或者建议可以找我反馈！祝大家玩的开心！")
print()
changzhu = ["琴", "迪卢克", "莫娜", "七七", "刻晴", "提纳里", "迪希雅", "梦见月瑞希"]
blue = ["飞天御剑", "黎明神剑", "冷刃", "以理服人", "沐浴龙血的剑", "铁影阔剑", "黑缨枪", "翡玉法球", "讨龙英杰谭", "魔导绪论", "弹弓","神射手之誓", "鸦羽弓"]
purple_weapon = ["匣里龙吟", "祭礼剑", "笛剑", "西风剑", "雨裁", "祭礼大剑", "钟剑", "西风大剑", "西风长枪", "匣里灭辰", "昭心", "祭礼残章", "流浪乐章", "西风秘典", "弓藏", "祭礼弓", "绝弦", "西风猎弓"]
purple_characters = ["芭芭拉", "雷泽", "香菱", "北斗", "行秋", "凝光", "菲谢尔", "班尼特", "诺艾尔", "重云", "迪奥娜", "砂糖", "辛焱", "罗莎莉亚", "烟绯", "托马", "早柚", "五郎", "九条裟罗", "鹿野院平藏", "绮良良", "云堇", "久岐忍", "柯莱", "多莉", "莱依拉", "珐露珊", "瑶瑶", "卡维", "琳妮特", "菲米尼", "夏洛蒂", "夏沃蕾","嘉明", "赛索斯", "卡齐娜", "欧洛伦", "蓝砚", "伊安珊", "伊法", "爱诺", "雅珂达", "叶洛亚", "布伦妮", "阿罗夏", "坎蒂丝", "米卡", "塔利雅", "瓦列里"]
gold = 0
purple = 0
wai = 0
purple_wai = 0
j = 1
gems = 0
total_wish = 0
FR_PRIVATE = 0x10
gdi32 = ctypes.WinDLL('gdi32')
add_font = gdi32.AddFontResourceExW
add_font.argtypes = [wintypes.LPCWSTR, wintypes.UINT, wintypes.LPVOID]
add_font.restype = wintypes.UINT

def chujin_wai():
    global gold
    global wai
    global purple
    c = random.randint(0, 7)
    print("\033[1;33m★★★★★" + changzhu[c] + "(" + str(gold + 1) + ")" + "\033[0m")
    gold = 0
    wai = 1
    purple = purple + 1

def chujin_up():
    global gold
    global wai
    global purple
    print("\033[1;33m★★★★★" + gold_name.get() + "(" + str(gold + 1) + ")" + "\033[0m")
    gold = 0
    wai = 0
    purple = purple + 1

def chuzi():
    global gold
    global purple_wai
    global purple
    b = random.randint(1, 2)
    if b == 1 and purple_wai == 0:
        d = random.randint(0, 19)
        if d <= 17:
            print("\033[1;35m★★★★"+purple_weapon[d]+"\033[0m")
            purple = 0
            gold = gold + 1
            purple_wai = 1
        elif 18 <= d <= 19:
            f = random.randint(0, 48)
            print("\033[1;35m★★★★"+purple_characters[f]+"\033[0m")
            purple = 0
            gold = gold + 1
            purple_wai = 1
    else:
        d = random.randint(1, 3)
        if d == 1:
            print("\033[1;35m★★★★"+purple_name1.get()+"\033[0m")
            purple = 0
            gold = gold + 1
            purple_wai = 0
        elif d == 2:
            print("\033[1;35m★★★★"+purple_name2.get()+"\033[0m")
            purple = 0
            gold = gold + 1
            purple_wai = 0
        elif d == 3:
            print("\033[1;35m★★★★"+purple_name3.get()+"\033[0m")
            purple = 0
            gold = gold + 1
            purple_wai = 0

def chulan():
    global gold
    global purple
    e = random.randint(0, 12)
    print("\033[1;34m★★★"+blue[e]+"\033[0m")
    gold = gold + 1
    purple = purple + 1

def close_input_window():
    tanchu = messagebox.askokcancel("退出","确认退出吗？")
    if tanchu:
        shuru.destroy()
        quit()

def save_input():
    shuru.destroy()

def select_wish_event():
    selected = kachi[kachi_name.get()]
    gold_name.set(selected["upg"])
    purple_name1.set(selected["upp1"])
    purple_name2.set(selected["upp2"])
    purple_name3.set(selected["upp3"])

def wish():
    global gold
    global purple_wai
    global purple
    global wai
    global gems
    global total_wish
    i = 1
    print("正在祈愿")
    while (i <= cishu):  # 连抽循环
        if 72 <= gold <= 80 and purple != 9:  # 73至81抽爆率
            a = random.random()
            if a <= 0.15 and wai == 0:
                chujin_wai()
            elif a <= 0.3:
                chujin_up()
            elif 0.3 < a <= 0.351:
                chuzi()
            else:
                chulan()
        elif 81 <= gold <= 88 and purple != 9:  # 82至89抽爆率
            a = random.random()
            if a <= 0.2 and wai == 0:
                chujin_wai()
            elif a <= 0.4:
                chujin_up()
            elif 0.4 < a <= 0.451:
                chuzi()
            else:
                chulan()
        elif gold == 89:  # 保底
            a = random.random()
            if a <= 0.5 and wai == 0:
                chujin_wai()
            else:
                chujin_up()
        elif purple >= 9 and gold != 89:
            chuzi()
        else:  # 1至72抽爆率
            a = random.random()
            if a <= 0.003 and wai == 0:
                chujin_wai()
            elif a <= 0.006:
                chujin_up()
            elif 0.006 < a <= 0.057:
                chuzi()
            else:
                chulan()
        i = i + 1  # 返回小循环
        gems = gems + 160
        total_wish = total_wish + 1
    print("还有" + str(10 - purple) + "抽必出四星")
    print("还有" + str(90 - gold) + "抽必出五星")

def danchou():
    global cishu
    cishu = 1
    wish()
    gems_var.set(gems)
    total_wish_var.set(total_wish)

def shilian():
    global cishu
    cishu = 10
    wish()
    gems_var.set(gems)
    total_wish_var.set(total_wish)

try:
    with open("wish_event_record.json", "r", encoding="utf-8") as f:
        kachi = json.load(f)
        kclist = kachi["kclist"]
except FileNotFoundError:
    kachi = {}
    kclist = []
    messagebox.showerror("警告", "文件缺失，请重新下载资源！")
    quit()

shuru = tk.Tk()

shuru.title("抽卡模拟器 v0.3.0")
shuru.geometry("400x700")
shuru.iconbitmap("ys.ico")
shuru.protocol("WM_DELETE_WINDOW", close_input_window)
kachi_name = tk.StringVar()
gold_name = tk.StringVar()
purple_name1 = tk.StringVar()
purple_name2 = tk.StringVar()
purple_name3 = tk.StringVar()
gems_var = tk.IntVar()
total_wish_var = tk.IntVar()
txt7 = tk.Label(shuru, text="原神抽卡模拟器", font=("汉仪文黑-85W Heavy", 16))
txt7.place(x=125, y=10)
txt8 = tk.Label(shuru, text="选择历史卡池", font=("汉仪文黑-85W Heavy", 12))
txt8.place(x=25, y=40)
combo1 = Combobox(shuru, width=18, textvariable=kachi_name, values=kclist, state="readonly", height = 5,font=("汉仪文黑-85W Heavy", 12))  # 创建菜单
combo1.current(0)  # 菜单设置默认值
combo1.place(x=25, y=75)
selected = kachi[kachi_name.get()]
bt1 = tk.Button(shuru, command = select_wish_event, text = "确定", font=("汉仪文黑-85W Heavy", 12), width=10)
bt1.place(x=275, y=70)
txt1 = tk.Label(shuru, text="请输入up五星：", font=("汉仪文黑-85W Heavy", 16))
txt1.place(x=100, y=110)
ent1 =tk.Entry(shuru, textvariable = gold_name, width=16, font=("汉仪文黑-85W Heavy", 16))
ent1.place(x=50, y=150)
txt2 = tk.Label(shuru, text="请输入up四星：", font=("汉仪文黑-85W Heavy", 16))
txt2.place(x=100, y=190)
ent2 =tk.Entry(shuru, textvariable =purple_name1, width=16, font=("汉仪文黑-85W Heavy", 16))
ent2.place(x=50, y=230)
txt3 = tk.Label(shuru, text="请输入up四星：", font=("汉仪文黑-85W Heavy", 16))
txt3.place(x=100, y=270)
ent3 =tk.Entry(shuru, textvariable =purple_name2, width=16, font=("汉仪文黑-85W Heavy", 16))
ent3.place(x=50, y=310)
txt4 = tk.Label(shuru, text="请输入up四星：", font=("汉仪文黑-85W Heavy", 16))
txt4.place(x=100, y=350)
ent4 =tk.Entry(shuru, textvariable =purple_name3, width=16, font=("汉仪文黑-85W Heavy", 16))
ent4.place(x=50, y=390)
txt5 = tk.Label(shuru, text="已消耗原石", font=("汉仪文黑-85W Heavy", 16))
txt5.place(x=50, y=430)
ent5 =tk.Entry(shuru, textvariable = gems_var, state = "disabled", width=6,font=("汉仪文黑-85W Heavy", 16), fg="blue")
ent5.place(x=175, y=430)
txt6 = tk.Label(shuru, text="总抽数", font=("汉仪文黑-85W Heavy", 16))
txt6.place(x=50, y=470)
ent6 =tk.Entry(shuru, textvariable = total_wish_var, state = "disabled", width=6,font=("汉仪文黑-85W Heavy", 16), fg="blue")
ent6.place(x=175, y=470)
bt2 = tk.Button(shuru, command = danchou, text = "祈愿1次", font=("汉仪文黑-85W Heavy", 12), width=12)
bt2.place(x=25, y=510)
bt2 = tk.Button(shuru, command = shilian, text = "祈愿10次", font=("汉仪文黑-85W Heavy", 12), width=12)
bt2.place(x=225, y=510)
txt9 = tk.Label(shuru, text="软件版本：v0.3.0", font=("汉仪文黑-85W Heavy", 11))
txt9.place(x=0, y=550)
txt10 = tk.Label(shuru, text="本软件仍在测试中，不代表最终品质，如有bug请与我联系。", font=("汉仪文黑-85W Heavy", 11))
txt10.place(x=0, y=570)
txt11 = tk.Label(shuru, text="©2026 Gamedraw.Studio，采用CC BY-NC-SA 3.0授权", font=("汉仪文黑-85W Heavy", 11))
txt11.place(x=0, y=590)
txt12 = tk.Label(shuru, text="制作：野渡横舟。原神UID:346668889", font=("汉仪文黑-85W Heavy", 11))
txt12.place(x=0, y=610)
txt13 = tk.Label(shuru, text="仅为模拟祈愿，一切祈愿概率以官方为准。", font=("汉仪文黑-85W Heavy", 11))
txt13.place(x=0, y=630)
txt14 = tk.Label(shuru, text="祝大家玩的开心！十连双金！", font=("汉仪文黑-85W Heavy", 11), fg="yellow")
txt14.place(x=0, y=650)
shuru.mainloop()