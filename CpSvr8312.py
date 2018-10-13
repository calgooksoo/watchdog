import win32com.client

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

objWorldCur.SetInputValue(0, 'COMP')  
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
#date = objWorldCur.GetDataValue(0, 0)
#value = objWorldCur.GetDataValue(4, 0)

#value = str(name) + " | 현재가 : " + str(cprice) + " | 대비 : " + str(diff) + " " + str(rate) + " | 거래시간 : " + str(ttime)
#value = str(name) + " | 현재가 : " + str(cprice)

#print(type(name))
print(name)
print(round(price,2))
print(round(rate, 2))
print(round(diff, 2))
