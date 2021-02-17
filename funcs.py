from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

account = kiwoom.GetLoginInfo("ACCNO")[0]


def getInfos():
    df = kiwoom.block_request("opw00004",
                              계좌번호=account,
                              비밀번호='',
                              상장폐지조회구분=0,
                              비밀번호입력매체구분="00",
                              output="계좌평가현황",
                              next=0)
    return df.values.tolist()[0]


def getStocks():
    df = kiwoom.block_request("opw00018",
                              계좌번호=account,
                              비밀번호='',
                              비밀번호입력매체구분="00",
                              조회구분=2,
                              output="계좌평가잔고개별합산",
                              next=0)
    return df.values.tolist()


def increase():
    # buy(code)
    return


def order(code, goal, until):
    print(code, goal, until)


def buy(code):
    kiwoom.SendOrder("시장가매수", "0101", account, 1, code, 1, 0, "03", "")


def sell(code):
    kiwoom.SendOrder("시장가매도", "0101", account, 2, code, 1, 0, "03", "")

