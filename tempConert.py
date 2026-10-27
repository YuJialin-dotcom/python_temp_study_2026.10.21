#Temp Convert
tempstr=input("请输入带有符号的温度")
if tempstr[-1] in ['f','F']:
    C=(eval(tempstr[0:-1])-32)/1.8
    print("转化温度为{:.2f}C".format(C))
elif tempstr[-1] in ['C','c']:
    F=(eval(tempstr[0:-1])*1.8)+32
    print("转化温度为{:.2f}F".format(F))
else:
    print("输入错误")
