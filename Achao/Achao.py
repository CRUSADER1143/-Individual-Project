#导入随机模块以生成随机数
import random
def CreatNew():
    Number=int(random.randint(1,100))
    return Number

def GetAnswer():
#生成随机数
    n1 = int(random.randint(1, 100))
    n2 = int(random.randint(1, 100))
    n3 = int(random.randint(1, 100))
#设置符号
    operater1 = ['+', '-']
    operater2 = ['×', '÷']
#i控制加减，j控制乘除
    i = random.randint(0, 1)
    j = random.randint(0, 1)
#除数为整数的情况
    while j == 1:
        if n2 % n3 == 0:
            break
        else:
            n3=CreatNew()
    # 打开希望写入的文件
    f = open("subject.txt", 'a')
    if i == 0 and j == 1:
        answer = n1 + n2 / n3
        print("{0}{1}{2}{3}{4}={5}".format(n1, operater1[i], n2, operater2[j], n3, answer), file=f)
        # 关闭文件以避免数据丢失
        f.close()
    elif i == 0 and j == 0:
        answer = n1 + n2 *n3
        print("{0}{1}{2}{3}{4}={5}".format(n1, operater1[i], n2, operater2[j], n3, answer), file=f)
        f.close()
    elif i == 1 and j == 0:
        answer = n1 - n2 * n3
        print("{0}{1}{2}{3}{4}={5}".format(n1, operater1[i], n2, operater2[j], n3, answer), file=f)
        f.close()
    else:
        answer = n1 - n2 / n3
        print("{0}{1}{2}{3}{4}={5}".format(n1, operater1[i], n2, operater2[j], n3, answer), file=f)
        f.close()

n = int(input("请输入想生成的题目数量"))
for i in range(0, n):
    GetAnswer()

