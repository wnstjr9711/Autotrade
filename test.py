import funcs
import datetime

myStock = dict()

# 계좌 내 주식 목록
for i in funcs.getStocks():
    myStock[i[1]] = [i[0][-6:], int(i[6]), float(i[-4])]
# 계좌 내 잔고
myBalance = int(funcs.getInfos()[5])

print('예탁자산평가액: {}'.format(myBalance))
print('주식잔고: {}'.format(myStock))

while True:
    print('-'*30)
    print('1:주식주문 2:비율증액 4:종료')
    print('-'*30)
    menu = int(input())
    if menu == 4:
        break
    else:
        print("기한(금일 09:00 ~ 15:30)")
        limit = input().split(':')
        now = datetime.datetime.now()
        duration = (int(limit[0]) - now.hour) * 3600 + (int(limit[1]) - now.minute) * 60 + now.second
        if menu == 1:
            print("종목명, 목표비율")
            code, target = input().split(',')
            funcs.order(myStock[code][0], None, duration)
        if menu == 2:
            balance = dict()
            for i in myStock:
                balance[myStock[i][0]] = int(myBalance * myStock[i][2] / 100)
            for i in balance:
                funcs.order(i, balance[i], duration)
