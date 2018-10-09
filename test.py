import win32com.client
 
 
# 연결 여부 체크
objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect
if (bConnect == 0):
    print("PLUS가 정상적으로 연결되지 않음. ")
    exit()
 
# 종목코드 리스트 구하기
objCpUsCode = win32com.client.Dispatch("CpUtil.CpUsCode")
codeList = objCpUsCode.GetUsCodeList(1) #거래소
codeList2 = objCpUsCode.GetUsCodeList(2)
codeList3 = objCpUsCode.GetUsCodeList(4)
codeList4 = objCpUsCode.GetUsCodeList(7)
 
 
print("전종목", len(codeList))
for i, code in enumerate(codeList):
    name = objCpUsCode.GetNameByUsCode(code)
    print(i, name)
 
# print("코스닥 종목코드", len(codeList2))
# for i, code in enumerate(codeList2):
#     secondCode = objCpCodeMgr.GetStockSectionKind(code)
#     name = objCpCodeMgr.CodeToName(code)
#     stdPrice = objCpCodeMgr.GetStockStdPrice(code)
#     print(i, code, secondCode, stdPrice, name)
