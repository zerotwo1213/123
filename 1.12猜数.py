import  random
a=random.randint(1,100)
c=1
while c<=10:
    b=eval(input('猜数，1——100,请输入 ：'))
    if b==a:
        print('猜对了')
        break
    elif b>a:
        print('大了')
    else:
        print('小了')
    c+=1
if c<=3:
    print('可以啊，老弟',c,'次')
elif c<=7:
    print('一般般',c,'次')
else:
    print('你不行啊',c,'次')