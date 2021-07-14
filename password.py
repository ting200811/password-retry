# 密碼重試程式
password = input('請輸入密碼:')
x = 3
if password == 'a123456':
    print('密碼正確')
else:
    while x > 0:
        print('您還有', x, '次機會')
        x = x - 1
        passworkd = input('請輸入密碼')
        if x == 0:
           print('密碼錯誤次數過多, 請十分鐘後再重試')

    
    
