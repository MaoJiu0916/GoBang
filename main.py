def msg():
    # 输出最后胜利的棋盘
    print("\033[1;30;46m-----------------------------------------")
    print('\t' + "1   2   3   4   5   6   7   8   9   10")
    for i in range(len(checkboard)):
        print(chr(i + ord('A')) + "\t", end='')
        for j in range(len(checkboard[i])):
            print(checkboard[i][j] + "\t", end='')
        print()
    print("-----------------------------------------\033[0m")
    if flagNum == 1:
        print('\033[32m*棋胜利！***[0m')
    else:
        print('\033[32mo棋胜利！***[0m')


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    finish = False
    flagNum = 1
    flagch = '*'
    x = 0
    y = 0
    print("简易五子棋游戏")
    print("-----------------------------------------\033[0m")
    checkboard = []
    for i in range(10):
        checkboard.append([])
        for j in range(10):
            checkboard[i].append('-')
    while not finish:
        # 初始化棋盘
        print('\t' + "1   2   3   4   5   6   7   8   9   10")
        for i in range(len(checkboard)):
            print(chr(i + ord('A')) + "\t", end='')
            for j in range(len(checkboard[i])):
                print(checkboard[i][j] + "\t", end='')
            print()
        print("-----------------------------------------\033[0m")
        # 判断当前下棋着
        if flagNum == 1:
            flagch = "*"
            print('\033[1;37;45m请*输入棋子坐标(例如A1):\[0330m', end='')
        else:
            flagch = "o"
            print('\033[1;30;42m请o输入棋子坐标(例如J5):\[0330m', end='')
        # 输入棋子坐标
        str1 = input()
        ch = str1[0]
        x = ord(ch) - 65
        y = int(str1[1]) - 1
        if (x < 0 or x > 9 or y < 0 or y > 9):
            print("您输入的坐标有误请重新输入！")
            continue
        # 判断坐标上是否有棋子
        if checkboard[x][y] == '-':
            if flagNum == 1:
                checkboard[x][y] = '*'
            else:
                checkboard[x][y] = 'o'
        else:
            print("您输入的位置已经有棋子，请重新输入！")
            continue
        if y - 4 >= 0:
            if (checkboard[x][y - 1] == flagch and checkboard[x][y - 2] == flagch and checkboard[x][y - 3] == flagch and
                    checkboard[x][y - 4] == flagch):
                finish = True
                msg()
        # 判断棋子右侧
        if (y + 4 <= 9):
            if (checkboard[x][y + 1] == flagch and checkboard[x][y + 2] == flagch and checkboard[x][y + 3] == flagch and
                    checkboard[x][y + 4] == flagch):
                finish = True
                msg()
        # 判断棋子上面
        if (x - 4 >= 0):
            if (checkboard[x - 1][y] == flagch and checkboard[x - 2][y] == flagch and checkboard[x - 3][y] == flagch and
                    checkboard[x - 4][y] == flagch):
                finish = True
                msg()
        # 判断棋子下方
        if (x + 4 <= 9):
            if (checkboard[x + 1][y] == flagch and checkboard[x + 2][y] == flagch and checkboard[x + 3][y] == flagch and
                    checkboard[x + 4][y] == flagch):
                finish = True
                msg()
        # 判断棋子右上方向
        if (x - 4 >= 0 and y - 4 >= 0):
            if (checkboard[x - 1][y - 1] == flagch and checkboard[x - 2][y - 2] == flagch and checkboard[x - 3][
                y - 3] == flagch and
                    checkboard[x - 4][y - 4] == flagch):
                finish = True
                msg()
        # 判断棋子右下方向
        if (x + 4 <= 9 and y - 4 >= 0):
            if (checkboard[x + 1][y - 1] == flagch and checkboard[x + 2][y - 2] == flagch and checkboard[x + 3][
                y - 3] == flagch and
                    checkboard[x + 4][y - 4] == flagch):
                finish = True
                msg()
        # 判断棋子左上方向
        if (x - 4 >= 0 and y + 4 <= 0):
            if (checkboard[x - 1][y + 1] == flagch and checkboard[x - 2][y + 2] == flagch and checkboard[x - 3][
                y + 3] == flagch and
                    checkboard[x - 4][y + 4] == flagch):
                finish = True
                msg()
        # 判断棋子左下方向
        if (x + 4 <= 9 and y + 4 <= 9):
            if (checkboard[x + 1][y + 1] == flagch and checkboard[x + 2][y + 2] == flagch and checkboard[x + 3][
                y + 3] == flagch and
                    checkboard[x + 4][y + 4] == flagch):
                finish = True
                msg()
        flagNum *= -1  # 更换下棋者标记
