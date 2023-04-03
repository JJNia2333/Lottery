import random, heapq

if __name__ == '__main__':

    #---------------填写幸运数字作为随机种子：
    Luck_Number = 100; #尽量大于10
    #----------------------------------

    #程序实现---------------------------
    number_blue = []
    number_red = []

    # 最终数列
    _Blue = []
    _Red = []

    #百期内概率     #选用45%在票型内的号码
    #032 5%
    #041 1%
    #104 2%
    #113 8%
    #122 12%
    #131 5%
    #140 3%
    #203 2%
    #211 1%
    #212 17%
    #221 16%
    #230 5%
    #302 4%
    # 311 9%
    # 320 4%
    # 410 5%
    # 500 1%
    print("可选前票型共三种：122|212|221；可选后票型仅一种11;建议一次购买2注，覆盖后两种票型")
    # 1-11号数量 12个   
    number_1_12 = random.randint(1, 2)
    # 12-22号数量 12个
    if (number_1_12 == 1):
        number_13_24 = 2
    else:
        number_13_24 = random.randint(1, 2)
    # 23-33号数量 11个
    number_25_35 = random.randint(0, 5 - number_1_12 - number_13_24)
    if (number_1_12 + number_13_24 + number_25_35 < 5):
        number_25_35 = 5 - (number_1_12 + number_13_24)

    #后区号码判定
    number_after = number_before = 1

    print("此注票型：{0}{1}{2}".format(number_1_12, number_13_24, number_25_35))
    # 列表初始化
    for i in range(0, 35):
        number_blue.append(0)
    for i in range(0, 12):
        number_red.append(0)

    # 随机生成
    for i in range(0, Luck_Number):
        temp = random.randint(0, 33)
        number_blue[temp] += 1

        temp = random.randint(0, 11)
        number_red[temp] += 1

    blue_largest_vals = heapq.nlargest(35, number_blue)
    red_largest_vals = heapq.nlargest(12, number_red)

    #号码选择
    for val in blue_largest_vals:
        for i, elem in enumerate(number_blue):
            if val == elem:
                if (i + 1 <= 12 and number_1_12 > 0):
                    if (i + 1) not in _Blue:
                        _Blue.append(i + 1)
                        number_1_12 -= 1
                if (12 < i + 1 <= 24 and number_13_24 > 0):
                    if (i + 1) not in _Blue:
                        _Blue.append(i + 1)
                        number_13_24 -= 1
                if (24 < i + 1 <= 35 and number_25_35 > 0):
                    if (i + 1) not in _Blue:
                        _Blue.append(i + 1)
                        number_25_35 -= 1

    for val in red_largest_vals:
        for i, elem in enumerate(number_red):
            if val == elem:
                if(i + 1 <= 6 and number_before > 0):
                    _Red.append(i + 1)
                    number_before -= 1;
                if(i + 1 > 6 and number_after > 0):
                    _Red.append(i + 1)
                    number_after -= 1;

    _Blue = heapq.nsmallest(5, _Blue)
    _Red = heapq.nsmallest(2, _Red)

    print("前区号码：")
    print(_Blue)

    print("后区号码：")
    print(_Red)
