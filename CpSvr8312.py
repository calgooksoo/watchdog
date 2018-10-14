import win32com.client

def overseaMarket(code):
    objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
    bConnect = objCpCybos.IsConnect
    if (bConnect == 0):
        print("PLUS가 정상적으로 연결되지 않음. ")
        exit()
    else:
        print("PLUS가 정상적 연결. ")    
        # 현재가 객체 구하기
    #objWorldCur = win32com.client.Dispatch("CpSysDib.WorldCur")
    #objWorldCur.SetInputValue(0, code)  

    objWorldCur = win32com.client.Dispatch("Dscbo1.CpFore8312")

    objWorldCur.SetInputValue(0, code)  
    #objWorldCur.SetInputValue(1, ord('D'))  
    objWorldCur.SetInputValue(2, 1)  
    objWorldCur.BlockRequest()

    # 현재가 통신 및 통신 에러 처리 
    rqStatus = objWorldCur.GetDibStatus()
    rqRet = objWorldCur.GetDibMsg1()
    print(rqRet)
    if rqStatus != 0:
        print("통신상태 문제", rqStatus, rqRet)
        exit()


    name = objWorldCur.GetHeaderValue(0) # 해외지수코드
    price = objWorldCur.GetHeaderValue(4) # 현재가
    rate = objWorldCur.GetHeaderValue(6) # 등락율
    diff = objWorldCur.GetHeaderValue(5) # 등락
    ttime = objWorldCur.GetHeaderValue(14) # 거래시간

    value = str(name) + " " + str(round(price,2)) + " | " + str(round(rate, 2)) + "% | " + str(round(diff, 2)) + " | 거래시간 : " + str(ttime)
    return value


print(overseaMarket('ENXH'));

