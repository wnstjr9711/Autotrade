from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
print("블록킹 로그인 완료")

# user_name = kiwoom.GetLoginInfo("USER_NAME")            # 사용자명
# account_num = kiwoom.GetLoginInfo("ACCOUNT_CNT")        # 전체 계좌수
# accounts = kiwoom.GetLoginInfo("ACCNO")                 # 전체 계좌 리스트
# print(account_num)
# print(accounts)
# print(user_name)