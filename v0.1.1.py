# -*- coding: utf-8 -*-
import random

print("Genshin Wish Simulator for Windows v0.1.1")
print("(C) Copyright 2026 Gamedraw.Studio")
print("软件还在测试中，有任何bug或者建议可以找我反馈！祝大家玩的开心！")
print()
changzhu = ["琴", "迪卢克", "莫娜", "七七", "刻晴", "提纳里", "迪希雅", "梦见月瑞希"]
blue = ["飞天御剑", "黎明神剑", "冷刃", "以理服人", "沐浴龙血的剑", "铁影阔剑", "黑缨枪", "翡玉法球", "讨龙英杰谭", "魔导绪论", "弹弓","神射手之誓", "鸦羽弓"]
purple_weapon = ["匣里龙吟", "祭礼剑", "笛剑", "西风剑", "雨裁", "祭礼大剑", "钟剑", "西风大剑", "西风长枪", "匣里灭辰", "昭心", "祭礼残章", "流浪乐章", "西风秘典", "弓藏", "祭礼弓", "绝弦", "西风猎弓"]
purple_characters = ["芭芭拉", "雷泽", "香菱", "北斗", "行秋", "凝光", "菲谢尔", "班尼特", "诺艾尔", "重云", "迪奥娜", "砂糖", "辛焱", "罗莎莉亚", "烟绯", "托马", "早柚", "五郎", "九条裟罗", "鹿野院平藏", "绮良良", "云堇", "久岐忍", "柯莱", "多莉", "莱依拉", "珐露珊", "瑶瑶", "卡维", "琳妮特", "菲米尼", "夏洛蒂", "夏沃蕾","嘉明", "赛索斯", "卡齐娜", "欧洛伦", "蓝砚", "伊安珊", "伊法", "爱诺", "雅珂达", "叶洛亚", "布伦妮", "阿罗夏", "坎蒂丝", "米卡", "塔利雅"]
gold_name = input("请输入up五星：")
purple_name1 = input("请输入up四星：")
purple_name2 = input("请输入up四星：")
purple_name3 = input("请输入up四星：")
gold = 0
purple = 0
wai = 0
purple_wai = 0
j = 1
while j:   #返回抽卡界面
    i = 1
    cishu = input("单抽还是十连？请输入数字：")
    if cishu == "1" or cishu == "10":
        print("正在祈愿")
        while(i <= int(cishu)):   #连抽循环
            if 72 <= gold <= 80 and purple != 9:   #73至81抽爆率
                a = random.random()
                if a <= 0.15 and wai == 0:
                    c = random.randint(0, 7)
                    print("\033[1;33m★★★★★"+changzhu[c]+"("+str(gold+1)+")"+"\033[0m")
                    gold = 0
                    wai = 1
                    purple = purple + 1
                elif a <= 0.3:
                    print("\033[1;33m★★★★★"+gold_name+"("+str(gold+1)+")"+"\033[0m")
                    gold = 0
                    wai = 0
                    purple = purple + 1
                elif 0.3 < a <= 0.351:
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
                            print("\033[1;35m★★★★"+purple_name1+"\033[0m")
                            purple = 0
                            gold = gold + 1
                            purple_wai = 0
                        elif d == 2:
                            print("\033[1;35m★★★★"+purple_name2+"\033[0m")
                            purple = 0
                            gold = gold + 1
                            purple_wai = 0
                        elif d == 3:
                            print("\033[1;35m★★★★"+purple_name3+"\033[0m")
                            purple = 0
                            gold = gold + 1
                            purple_wai = 0
                else:
                    e = random.randint(0, 12)
                    print("\033[1;34m★★★"+blue[e]+"\033[0m")
                    gold = gold + 1
                    purple = purple + 1
            elif 81 <= gold <= 88 and purple != 9:   #82至89抽爆率
                a = random.random()
                if a <= 0.2 and wai == 0:
                    c = random.randint(0, 7)
                    print("\033[1;33m★★★★★"+changzhu[c]+"("+str(gold+1)+")"+"\033[0m")
                    gold = 0
                    wai = 1
                    purple = purple + 1
                elif a <= 0.4:
                    print("\033[1;33m★★★★★"+gold_name+"("+str(gold+1)+")"+"\033[0m")
                    gold = 0
                    wai = 0
                    purple = purple + 1
                elif 0.4 < a <= 0.451:
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
                            print("\033[1;35m★★★★"+purple_name1+"\033[0m")
                            purple = 0
                            gold = gold + 1
                            purple_wai = 0
                        elif d == 2:
                            print("\033[1;35m★★★★"+purple_name2+"\033[0m")
                            purple = 0
                            gold = gold + 1
                            purple_wai = 0
                        elif d == 3:
                            print("\033[1;35m★★★★"+purple_name3+"\033[0m")
                            purple = 0
                            gold = gold + 1
                            purple_wai = 0
                else:
                    e = random.randint(0, 12)
                    print("\033[1;34m★★★"+blue[e]+"\033[0m")
                    gold = gold + 1
                    purple = purple + 1
            elif gold == 89:    #保底
                a = random.random()
                if a <= 0.5 and wai == 0:
                    c = random.randint(0, 7)
                    print("\033[1;33m★★★★★"+changzhu[c]+"("+str(gold+1)+")"+"\033[0m")
                    gold = 0
                    wai = 1
                else:
                    print("\033[1;33m★★★★★"+gold_name+"("+str(gold+1)+")"+"\033[0m")
                    gold = 0
                    wai = 0
            elif purple >= 9 and gold != 89:
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
                        print("\033[1;35m★★★★"+purple_name1+"\033[0m")
                        purple = 0
                        gold = gold + 1
                        purple_wai = 0
                    elif d == 2:
                        print("\033[1;35m★★★★"+purple_name2+"\033[0m")
                        purple = 0
                        gold = gold + 1
                        purple_wai = 0
                    elif d == 3:
                        print("\033[1;35m★★★★"+purple_name3+"\033[0m")
                        purple = 0
                        gold = gold + 1
                        purple_wai = 0
            else:    #1至72抽爆率
                a = random.random()
                if a <= 0.003 and wai == 0:
                    c = random.randint(0, 7)
                    print("\033[1;33m★★★★★"+changzhu[c]+"("+str(gold+1)+")"+"\033[0m")
                    gold = 0
                    wai = 1
                elif a <= 0.006:
                    print("\033[1;33m★★★★★"+gold_name+"("+str(gold+1)+")"+"\033[0m")
                    gold = 0
                    wai = 0
                elif 0.006 < a <= 0.057:
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
                            print("\033[1;35m★★★★"+purple_name1+"\033[0m")
                            purple = 0
                            gold = gold + 1
                            purple_wai = 0
                        elif d == 2:
                            print("\033[1;35m★★★★"+purple_name2+"\033[0m")
                            purple = 0
                            gold = gold + 1
                            purple_wai = 0
                        elif d == 3:
                            print("\033[1;35m★★★★"+purple_name3+"\033[0m")
                            purple = 0
                            gold = gold + 1
                            purple_wai = 0
                else:
                    e = random.randint(0, 12)
                    print("\033[1;34m★★★"+blue[e]+"\033[0m")
                    gold = gold + 1
                    purple = purple + 1
            i = i + 1    #返回小循环
        print("还有"+str(10-purple)+"抽必出四星")
        print("还有"+str(90-gold)+"抽必出五星")
    else:
        print("输入错误，请重新输入")